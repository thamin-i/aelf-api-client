import typing as t

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .text import TextModel


class ComplinesModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    introduction: str
    hymne: TextModel
    antienne_1: str
    psaume_1: TextModel
    antienne_2: str | None = Field(default=None)
    psaume_2: TextModel | None = Field(default=None)
    pericope: TextModel
    repons: str
    antienne_symeon: str
    cantique_symeon: TextModel
    oraison: str
    benediction: str
    hymne_mariale: TextModel

    @field_validator("psaume_2", mode="before")
    @classmethod
    def list_to_none(cls, value: t.Any) -> t.Any:
        """Convert value to None if value is an empty list.

        Args:
            value (t.Any): Value to convert.

        Returns:
            t.Any: Converted value.
        """
        if isinstance(value, list):
            if len(value) == 0:
                return None
            raise ValueError("Invalid value type")
        return value
