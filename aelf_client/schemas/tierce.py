from pydantic import BaseModel, ConfigDict

from .text import TextModel


class TierceModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    introduction: str
    hymne: TextModel
    antienne_1: str
    psaume_1: TextModel
    antienne_2: str
    psaume_2: TextModel
    antienne_3: str
    psaume_3: TextModel
    pericope: TextModel
    repons: str
    oraison: str
