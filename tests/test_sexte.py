"""Test the AELFClient request_sexte method."""

from datetime import datetime

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZonesEnum
from aelf_api_client.schemas.responses import SexteResponseModel


@pytest.mark.asyncio
async def test_sexte_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    sexte: SexteResponseModel = await client.request_sexte(date, zone)
