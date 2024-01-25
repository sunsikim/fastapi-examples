import asyncsql.schemas.comments as schemas

from fastapi import Depends, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from asyncsql.database import get_async_session
from asyncsql.models.comments import Comment
from asyncsql.models.posts import Post
from asyncsql.routers.posts import get_post_or_404

router = APIRouter()


@router.post(
    path="/posts/{id}/comments",
    response_model=schemas.CommentRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_comment(
        comment_create: schemas.CommentCreate,
        post: Post = Depends(get_post_or_404),
        session: AsyncSession = Depends(get_async_session),
) -> Comment:
    comment = Comment(**comment_create.model_dump(), post=post)
    session.add(comment)
    await session.commit()
    return comment
