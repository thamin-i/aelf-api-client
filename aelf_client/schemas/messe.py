import typing as t

from pydantic import BaseModel, ConfigDict, Field

from .lecture import LectureModel


class MesseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nom: str
    lectures: t.List[LectureModel] = Field(default=[])
