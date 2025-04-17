"""Test the AELFClient request_lectures method."""

from datetime import datetime

import pytest

from aelf_client import AELFClient
from aelf_client.schemas.enums import ZonesEnum
from aelf_client.schemas.responses import LecturesResponseModel


@pytest.mark.asyncio
async def test_lectures_endpoint():
    client: AELFClient = AELFClient()
    date: datetime = datetime.now()
    zone: ZonesEnum = ZonesEnum.FRANCE
    lectures: LecturesResponseModel = await client.request_lectures(date, zone)
