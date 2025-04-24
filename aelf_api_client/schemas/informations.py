from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import ColorEnum, ZoneEnum


class InformationsModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    date: datetime
    zone: ZoneEnum
    couleur: ColorEnum
    annee: str | None = Field(default=None)
    temps_liturgique: str | None = Field(default=None)
    semaine: str | None = Field(default=None)
    jour: str | None = Field(default=None)
    jour_liturgique_nom: str
    fete: str
    degre: str
    ligne1: str
    ligne2: str
    ligne3: str
    couleur2: ColorEnum | None = Field(default=None)
    couleur3: ColorEnum | None = Field(default=None)
