import datetime as dt
from pydantic import BaseModel, Field, ConfigDict, field_validator, ValidationInfo


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

    @field_validator("title", "content")
    @classmethod
    def text_validator(cls, value: str, info: ValidationInfo):
        """
        this function will be used to validate values of both title and content field

        decorated function should either
         1. raise ValueError or AssertionError
         2. return value that should be assigned to the field
        """
        if not value.isalnum():
            raise ValueError(f"{info.field_name} contains non-alphanumeric character(s)")
        else:
            return value



class PostCreate(PostBase):
    """
    Although such definition seems redundant, best practice is to define separate data model for different requests
    """
    pass


class PostRead(PostBase):
    id: int = Field(..., ge=0)


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
