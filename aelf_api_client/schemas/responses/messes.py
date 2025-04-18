import typing as t

from pydantic import BaseModel, ConfigDict, Field

from aelf_api_client.schemas.informations import InformationsModel
from aelf_api_client.schemas.messe import MesseModel


class MessesResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    messes: t.List[MesseModel] = Field(default=[])
