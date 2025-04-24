from pydantic import BaseModel, ConfigDict, Field

from .text import TextModel


class VespersModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    introduction: str
    hymne: TextModel
    antienne_1: str
    psaume_1: TextModel
    antienne_2: str
    psaume_2: TextModel
    antienne_3: str | None = Field(default=None)
    psaume_3: TextModel
    pericope: TextModel
    repons: str
    antienne_magnificat: str
    cantique_mariale: TextModel
    intercession: str
    notre_pere: str
    oraison: str
