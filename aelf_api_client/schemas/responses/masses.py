import typing as t

from pydantic import BaseModel, ConfigDict, Field

from aelf_api_client.schemas.informations import InformationsModel
from aelf_api_client.schemas.mass import MassModel


class MassesResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    messes: t.List[MassModel] = Field(default=[])
