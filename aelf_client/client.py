import typing as t
from datetime import datetime

import aiohttp
import async_timeout
from pydantic import BaseModel

from .schemas.enums import ZonesEnum
from .schemas.responses import (
    CompliesResponseModel,
    InformationsResponseModel,
    LaudesResponseModel,
    LecturesResponseModel,
    MessesResponseModel,
    NoneResponseModel,
    SexteResponseModel,
    TierceResponseModel,
    VepresResponseModel,
)

ResponseModel = t.TypeVar("ResponseModel", bound=BaseModel)


class AELFClient:
    """Client for the AELF public API."""

    base_url: str = "https://api.aelf.org"
    default_timeout: int
    default_headers: t.Dict[str, str] = {
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
    }

    def __init__(self, default_timeout: int = 10) -> None:
        """Initialize the AELF client.

        Args:
            default_timeout (int, optional):
                Default timeout for requests in seconds.
                Defaults to 10.
        """
        self.default_timeout = default_timeout

    def __build_url(self, date: datetime, zone: ZonesEnum, endpoint: str) -> str:
        """Build the URL for the AELF API endpoint.

        Args:
            date (datetime): Date to fetch information for.
            zone (ZonesEnum): Liturgical zone to fetch information for.
            endpoint (str): The API endpoint to call.

        Returns:
            str: The constructed URL.
        """
        return f"{self.base_url}/v1/{endpoint}/{date.strftime('%Y-%m-%d')}/{zone.value}"

    async def __request(self, url: str, model: t.Type[ResponseModel]) -> ResponseModel:
        """Request the AELF API and return the response model.

        Args:
            date (datetime): Date to fetch information for.
            zone (ZonesEnum): Liturgical zone to fetch information for.
            model (t.Type[ResponseModel]): The response model to validate against.

        Returns:
            ResponseModel: Response for the given endpoint.
        """
        async with async_timeout.timeout(self.default_timeout):
            async with aiohttp.ClientSession(headers=self.default_headers) as session:
                async with session.get(url=url) as response:
                    response.raise_for_status()
                    return model.model_validate(await response.json())

    async def request_informations(
        self, date: datetime, zone: ZonesEnum
    ) -> InformationsResponseModel:
        """Fetch liturgical information for a given date and zone.

        Args:
            date (datetime): Date to fetch information for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            InformationsResponseModel: Liturgical information for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "informations"), model=InformationsResponseModel
        )

    async def request_messes(self, date: datetime, zone: ZonesEnum) -> MessesResponseModel:
        """Fetch messes for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            MessesResponseModel: Messes for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "messes"), model=MessesResponseModel
        )

    async def request_complies(self, date: datetime, zone: ZonesEnum) -> CompliesResponseModel:
        """Fetch complies for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            CompliesResponseModel: Complies for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "complies"), model=CompliesResponseModel
        )

    async def request_laudes(self, date: datetime, zone: ZonesEnum) -> LaudesResponseModel:
        """Fetch laudes for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            LaudesResponseModel: Laudes for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "laudes"), model=LaudesResponseModel
        )

    async def request_lectures(self, date: datetime, zone: ZonesEnum) -> LecturesResponseModel:
        """Fetch lectures for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            LecturesResponseModel: Lectures for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "lectures"), model=LecturesResponseModel
        )

    async def request_none(self, date: datetime, zone: ZonesEnum) -> NoneResponseModel:
        """Fetch none for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            NoneResponseModel: none for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "none"), model=NoneResponseModel
        )

    async def request_sexte(self, date: datetime, zone: ZonesEnum) -> SexteResponseModel:
        """Fetch sexte for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            SexteResponseModel: Sexte for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "sexte"), model=SexteResponseModel
        )

    async def request_tierce(self, date: datetime, zone: ZonesEnum) -> TierceResponseModel:
        """Fetch tierce for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            TierceResponseModel: Tierce for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "tierce"), model=TierceResponseModel
        )

    async def request_vepres(self, date: datetime, zone: ZonesEnum) -> VepresResponseModel:
        """Fetch vepres for a given date and zone.

        Args:
            date (datetime): Date to fetch messes for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            VepresResponseModel: Vepres for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, "vepres"), model=VepresResponseModel
        )
