from pydantic import BaseModel, ConfigDict

from aelf_api_client.schemas.informations import InformationsModel
from aelf_api_client.schemas.tierce import TierceModel


class TierceResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    tierce: TierceModel
