import typing as t

from pydantic import BaseModel, ConfigDict, Field

from .reading import LectureModel


class MassModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nom: str
    lectures: t.List[LectureModel] = Field(default=[])
