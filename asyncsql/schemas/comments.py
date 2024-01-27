import datetime as dt
from pydantic import BaseModel, Field, ConfigDict, field_validator, ValidationInfo


class CommentBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )
    created_at: dt.datetime = Field(default_factory=dt.datetime.now)
    content: str

    @field_validator("content")
    @classmethod
    def text_validator(cls, value: str):
        if not value.isalnum():
            raise ValueError(f"content contains non-alphanumeric character(s)")
        else:
            return value


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    post_id: int
