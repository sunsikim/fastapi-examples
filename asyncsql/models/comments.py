import datetime as dt
from sqlalchemy import DateTime, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from asyncsql.models import Base


class Comment(Base):
    """
     * `sqlalchemy.orm` maps this class into actual table in a SQL database
     * Class property defined using `mapped_column` with optional type annotation corresponds to column of the table
    """
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=False, default=dt.datetime.now)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    post: Mapped["Post"] = relationship("Post", back_populates="comments")
