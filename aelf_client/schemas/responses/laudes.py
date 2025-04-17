from pydantic import BaseModel, ConfigDict

from aelf_client.schemas.informations import InformationsModel
from aelf_client.schemas.laudes import LaudesModel


class LaudesResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    laudes: LaudesModel
