from pydantic import BaseModel, ConfigDict, Field


class LectureModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: str
    refrain_psalmique: str | None = Field(default=None)
    ref_refrain: str | None = Field(default=None)
    titre: str | None = Field(default=None)
    contenu: str
    ref: str
    intro_lue: str | None = Field(default=None)
    verset_evangile: str | None = Field(default=None)
    ref_verset: str | None = Field(default=None)
