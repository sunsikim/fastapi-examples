import datetime as dt
from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from asyncsql.models import Base
from asyncsql.models.comments import Comment


class Post(Base):
    """
     * As back referenced name of comment was `comments`, set the property name as `comments` as well
     * cascase="all, delete" ensures that related comments are all deleted if the post is deleted
     * Note that it is done by ORM, not by SQL(i.e. it doesn't mean that CASCADE DELETE construct is used internally)
    """
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=False, default=dt.datetime.now)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    comments: Mapped[list[Comment]] = relationship("Comment", cascade="all, delete")
