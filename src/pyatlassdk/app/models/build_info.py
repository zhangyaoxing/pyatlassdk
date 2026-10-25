"""Generated model for BuildInfo. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class BuildInfo(BaseModel):
    """Generated model for BuildInfo."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    version: str | None = Field(default=None, description="Human-readable version information about the mongod instance. This\nstring will take the format `<major>.<minor>.<patch>`.")
    git_version: str | None = Field(default=None, alias="gitVersion", description="The commit identifier that identifies the state of the code use to build\nthe mongod.")
    version_array: list[int] | None = Field(default=None, alias="versionArray", description="An array that conveys version information about the mongod instance. See\nversion for a more readable version of this string.")
    javascript_engine: str | None = Field(default=None, alias="javascriptEngine", description="A string that reports the JavaScript engine used in the mongod instance.\nBy default, this is `mozjs` after version `3.2`, and previously `V8`.")
    bits: str | None = Field(default=None, description="A number that reflects the target processor architecture of the mongod\nbinary.")
    debug: bool | None = Field(default=None, description="A boolean that reflects whether or not the `mongod` instance was built\nwith debugging options.")
    max_bson_object_size: int | None = Field(default=None, alias="maxBsonObjectSize", description="A number that reports the [Maximum BSON Document\nSize](https://www.mongodb.com/docs/manual/reference/limits#std-label-limit-bson-document-size)")
