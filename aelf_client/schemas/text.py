from pydantic import BaseModel, ConfigDict, Field


class TextModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    auteur: str | None = Field(default=None)
    editeur: str | None = Field(default=None)
    reference: str | None = Field(default=None)
    titre: str | None = Field(default=None)
    texte: str
