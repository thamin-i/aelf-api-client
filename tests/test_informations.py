"""Test the AELFClient request_informations method."""

from datetime import datetime

import pytest

from aelf_client import AELFClient
from aelf_client.schemas.enums import ZonesEnum
from aelf_client.schemas.responses import InformationsResponseModel


@pytest.mark.asyncio
async def test_informations_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    informations: InformationsResponseModel = await client.request_informations(date, zone)
