import typing as t

from pydantic import BaseModel, ConfigDict, Field

from .text import TextModel


class LecturesModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    introduction: str
    hymne: TextModel
    antienne_1: str
    psaume_1: TextModel
    antienne_2: str | None = Field(default=None)
    psaume_2: TextModel
    antienne_3: str | None = Field(default=None)
    psaume_3: TextModel
    verset_psaume: str
    lecture: TextModel
    repons_lecture: str
    titre_patristique: str
    texte_patristique: str
    repons_patristique: str
    te_deum: t.List[str]
    oraison: str
