from pydantic import BaseModel, ConfigDict

from .text import TextModel


class LaudsModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    introduction: str
    antienne_invitatoire: str
    psaume_invitatoire: TextModel
    hymne: TextModel
    antienne_1: str
    psaume_1: TextModel
    antienne_2: str
    psaume_2: TextModel
    antienne_3: str
    psaume_3: TextModel
    pericope: TextModel
    repons: str
    antienne_zacharie: str
    cantique_zacharie: TextModel
    intercession: str
    notre_pere: str
    oraison: str
