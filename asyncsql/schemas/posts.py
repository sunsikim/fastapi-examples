import datetime as dt
from pydantic import BaseModel, Field, ConfigDict


class PostBase(BaseModel):
    """
     * Arguments of `ConfigDict`(or, list of adjustable model configuration) : https://docs.pydantic.dev/2.5/api/config/
     * Only define common fields required among several other fields. Do not put every field in base model.
    """
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )
    title: str
    content: str
    created_at: dt.datetime = Field(default_factory=dt.datetime.now)


class PostCreate(PostBase):
    """
    Although such definition seems redundant, best practice is to define separate data model for different requests
    """
    pass


class PostRead(PostBase):
    id: int


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
