"""Test the AELFClient request_messes method."""

from datetime import datetime

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZonesEnum
from aelf_api_client.schemas.responses import MessesResponseModel


@pytest.mark.asyncio
async def test_messes_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    messes: MessesResponseModel = await client.request_messes(date, zone)
