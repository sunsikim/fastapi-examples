from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from asyncsql.models import Base

DATABASE_URL = "sqlite+aiosqlite:///asyncsql.db"
engine = create_async_engine(DATABASE_URL)  # object to manage the connection between application and DB
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)  # creates actual connection


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
     * Session refers to the unit of request that is opened when request is started and closed when answered
     * FastAPI requires special session maker that would create session to every asynchronous request
     * If `return` is used instead of `yield`, session will be closed as soon as it opened
    """
    async with async_session_maker() as session:
        yield session


async def create_all_tables():
    """
     * This creates schema of every table that is visible from predefined base class
     * However, this kind of initialization is only plausible for simple example like this.
     * For more realistic migration system that ensures larger database schema to be in sync, check out `alembic`.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
