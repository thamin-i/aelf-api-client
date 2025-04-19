from pydantic import BaseModel, ConfigDict

from aelf_api_client.schemas.complines import ComplinesModel
from aelf_api_client.schemas.informations import InformationsModel


class ComplinesResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    complies: ComplinesModel
