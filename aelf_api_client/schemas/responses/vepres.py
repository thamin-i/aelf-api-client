from pydantic import BaseModel, ConfigDict

from aelf_api_client.schemas.informations import InformationsModel
from aelf_api_client.schemas.vepres import VepresModel


class VepresResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    vepres: VepresModel
