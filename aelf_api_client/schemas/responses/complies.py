from pydantic import BaseModel, ConfigDict

from aelf_api_client.schemas.complies import CompliesModel
from aelf_api_client.schemas.informations import InformationsModel


class CompliesResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    complies: CompliesModel
