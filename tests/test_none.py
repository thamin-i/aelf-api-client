"""Test the AELFClient request_none method."""

from datetime import datetime

import pytest

from aelf_client import AELFClient
from aelf_client.schemas.enums import ZonesEnum
from aelf_client.schemas.responses import NoneResponseModel


@pytest.mark.asyncio
async def test_none_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    none: NoneResponseModel = await client.request_none(date, zone)
