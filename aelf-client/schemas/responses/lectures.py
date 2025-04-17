from pydantic import BaseModel, ConfigDict

from aelf_client.schemas.informations import InformationsModel
from aelf_client.schemas.lectures import LecturesModel


class LecturesResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    informations: InformationsModel
    lectures: LecturesModel
