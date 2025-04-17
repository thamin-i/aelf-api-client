from pydantic import BaseModel, ConfigDict

from aelf_api_client.schemas.informations import InformationsModel


class InformationsResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
