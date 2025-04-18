"""Test the AELFClient request_vepres method."""

from datetime import datetime

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZonesEnum
from aelf_api_client.schemas.responses import VepresResponseModel


@pytest.mark.asyncio
async def test_vepres_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    vepres: VepresResponseModel = await client.request_vepres(date, zone)
