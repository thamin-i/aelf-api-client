"""Test the AELFClient request_laudes method."""

from datetime import datetime

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZonesEnum
from aelf_api_client.schemas.responses import LaudesResponseModel


@pytest.mark.asyncio
async def test_laudes_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    laudes: LaudesResponseModel = await client.request_laudes(date, zone)
