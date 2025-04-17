"""Test the AELFClient request_complies method."""

from datetime import datetime

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZonesEnum
from aelf_api_client.schemas.responses import CompliesResponseModel


@pytest.mark.asyncio
async def test_complies_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    complies: CompliesResponseModel = await client.request_complies(date, zone)
