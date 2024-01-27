import datetime as dt
from sqlalchemy import DateTime, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from asyncsql.models import Base


class Comment(Base):
    """
     * `sqlalchemy.orm` maps this class into actual table in a SQL database
     * Class property defined using `mapped_column` with optional type annotation corresponds to column of the table
     * `relationship` does not create a column, but it is used to define how models relate to each other to ORM
     * As a result, post linked to a comment is directly approachable using comment.post
     * `back_populates="comments"` ensures the opposite also holds(i.e. get comment by referencing post.comments)
     * Finally, to avoid circular import, 'forward reference' is used to make type hints for Post(i.e. Mapped["Post"])
    """
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)  # SQL part of foreign key definition
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=False, default=dt.datetime.now)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    post: Mapped["Post"] = relationship("Post", back_populates="comments")  # ORM part of foreign key definition
