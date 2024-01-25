import datetime as dt
from pydantic import BaseModel, Field, ConfigDict


class CommentBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )
    created_at: dt.datetime = Field(default_factory=dt.datetime.now)
    content: str


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    post_id: int
