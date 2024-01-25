import contextlib
from fastapi import FastAPI
from asyncsql import routers
from asyncsql.database import create_all_tables


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    """
     * Parameter for `app` argument is passed automatically during application startup.
     * That is, although it may seem redundant to put argument not used within the method, it is still required.
    """
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=routers.posts_router, prefix="/posts", tags=["posts"])
app.include_router(router=routers.comments_router, prefix="/comments", tags=["comments"])
