"""Test the AELFClient request_tierce method."""

from datetime import datetime

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZonesEnum
from aelf_api_client.schemas.responses import TierceResponseModel


@pytest.mark.asyncio
async def test_tierce_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    tierce: TierceResponseModel = await client.request_tierce(date, zone)
