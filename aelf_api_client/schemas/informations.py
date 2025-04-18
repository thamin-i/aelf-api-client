from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import CouleursEnum, ZonesEnum


class InformationsModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    date: datetime
    zone: ZonesEnum
    couleur: CouleursEnum
    annee: str | None = Field(default=None)
    temps_liturgique: str
    semaine: str | None = Field(default=None)
    jour: str
    jour_liturgique_nom: str
    fete: str
    degre: str
    ligne1: str
    ligne2: str
    ligne3: str
    couleur2: CouleursEnum | None = Field(default=None)
    couleur3: CouleursEnum | None = Field(default=None)
