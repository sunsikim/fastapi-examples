import asyncsql.schemas as schemas

from collections.abc import Sequence
from fastapi import Depends, HTTPException, status, APIRouter, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from asyncsql.database import get_async_session
from asyncsql.models.posts import Post
from asyncsql.models.comments import Comment

router = APIRouter()


async def get_post_or_404(
    id: int,
    session: AsyncSession = Depends(get_async_session)
) -> Post:
    """
     * Dependency injection is programming style to determine and create objects at runtime
     * In FastAPI, `Depends` takes callable as parameter and execute it when the endpoint is called(i.e. at runtime)
     * It can be function, instance with __call__ method defined, and certain method of an instance
     * This isolates specific logic as separate method or function, so it can be reused everywhere in the application
     * In async application, developer has to make explicit queries to get relations of an ORM object
    """
    select_query = (
        select(Post)
        .options(selectinload(Post.comments))  # eager loading
        .where(Post.id == id)
    )
    result = await session.execute(select_query)
    post = result.scalar_one_or_none()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id = {id} is not found in the database"
        )
    return post


async def pagination(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0),
) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return skip, capped_limit


@router.post(
    path="/",
    response_model=schemas.posts.PostRead,
    status_code=status.HTTP_201_CREATED,
    # response_class=fastapi.responses.JSONResponse  # default(other options include PlainTextResponse, ... etc)
)
async def create_post(
    post_create: schemas.posts.PostCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Post:
    """
     * Response Body will contain a JSON with exactly same schema as defined in PostRead(i.e. id, created_at, ...)
     * This is because FastAPI transformed result as ORM into Pydantic model
    """
    post = Post(**post_create.model_dump())
    session.add(post)  # post is not yet created in the database
    await session.commit()  # the point where actual transaction is made(otherwise, it disappears when session ends)
    return post


@router.get(path="/", response_model=list[schemas.posts.PostRead])
async def list_posts(
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[Post]:
    """
     * According to `pagination` implementation, "?skip=0&limit=10" will be requested by default
     * `Depends(pagination)` executes pagination method and returns skip, capped_limit as a tuple(`pagination`)
    """
    skip, limit = pagination
    select_query = (
        select(Post)
        .options(selectinload(Post.comments))
        .offset(skip)
        .limit(limit)
    )
    result = await session.execute(select_query)  # not actual result; just a representation of query results
    return (
        result
        .scalars()  # where actual Post objects are fetched
        .all()  # where Posts objects are returned as sequence
    )


@router.get(path="/{id}", response_model=schemas.posts.PostRead)
async def get_post(post: Post = Depends(get_post_or_404)) -> Post:
    """
     path variable `id` will be consumed as a parameter of injected function `get_post_or_404`
    """
    return post


@router.patch(path="/{id}", response_model=schemas.posts.PostRead)
async def update_post(
        post_update: schemas.posts.PostPartialUpdate,
        post: Post = Depends(get_post_or_404),
        session: AsyncSession = Depends(get_async_session),
) -> Post:
    post_update_dict = post_update.model_dump(exclude_unset=True)
    for key, value in post_update_dict.items():
        setattr(post, key, value)
    session.add(post)
    await session.commit()
    return post


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
        post: Post = Depends(get_post_or_404),
        session: AsyncSession = Depends(get_async_session),
):
    await session.delete(post)
    await session.commit()


@router.post(
    path="/{id}/comments",
    response_model=schemas.comments.CommentRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_comment(
        comment_create: schemas.comments.CommentCreate,
        post: Post = Depends(get_post_or_404),
        session: AsyncSession = Depends(get_async_session),
) -> Comment:
    comment = Comment(**comment_create.model_dump(), post=post)
    session.add(comment)
    await session.commit()
    return comment
