from pydantic import BaseModel, ConfigDict

from aelf_api_client.schemas.informations import InformationsModel
from aelf_api_client.schemas.sexte import SexteModel


class SexteResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    sexte: SexteModel
