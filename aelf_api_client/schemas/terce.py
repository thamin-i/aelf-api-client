from pydantic import BaseModel, ConfigDict, Field

from .text import TextModel


class TerceModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    introduction: str
    hymne: TextModel
    antienne_1: str
    psaume_1: TextModel
    antienne_2: str | None = Field(default=None)
    psaume_2: TextModel
    antienne_3: str | None = Field(default=None)
    psaume_3: TextModel
    pericope: TextModel
    repons: str
    oraison: str
