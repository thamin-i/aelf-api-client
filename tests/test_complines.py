"""Test complines related methods."""

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZoneEnum, EntityEnum

from conftest import get_all_days_this_month


@pytest.mark.asyncio
async def test_complines_endpoint():
    client: AELFClient = AELFClient()
    zone: ZoneEnum = ZoneEnum.FRANCE
    for date in get_all_days_this_month():
        await client.request_complines(date, zone)


@pytest.mark.asyncio
async def test_request_endpoint():
    client: AELFClient = AELFClient()
    entity: EntityEnum = EntityEnum.COMPLINE
    zone: ZoneEnum = ZoneEnum.FRANCE
    for date in get_all_days_this_month():
        await client.request(entity=entity, date=date, zone=zone)
