"""Test complines related methods."""

from datetime import datetime

import pytest

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZoneEnum, EntityEnum


@pytest.mark.asyncio
async def test_complines_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZoneEnum = ZoneEnum.FRANCE
    await client.request_complines(date, zone)


@pytest.mark.asyncio
async def test_request_endpoint():
    client: AELFClient = AELFClient()
    entity: EntityEnum = EntityEnum.COMPLINE
    date: datetime = datetime.now()
    zone: ZoneEnum = ZoneEnum.FRANCE
    await client.request(entity=entity, date=date, zone=zone)
