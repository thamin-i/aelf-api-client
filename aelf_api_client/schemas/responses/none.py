from pydantic import BaseModel, ConfigDict

from aelf_api_client.schemas.informations import InformationsModel
from aelf_api_client.schemas.none import NoneModel


class NoneResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    none: NoneModel
