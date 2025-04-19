import typing as t
from datetime import datetime

import aiohttp
import async_timeout
from pydantic import BaseModel

from .schemas.enums import EntityEnum, ZoneEnum
from .schemas.responses import (
    ComplinesResponseModel,
    InformationsResponseModel,
    LaudsResponseModel,
    MassesResponseModel,
    NoneResponseModel,
    ReadingsResponseModel,
    SextResponseModel,
    TerceResponseModel,
    VespersResponseModel,
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

    def __build_url(self, date: datetime, zone: ZoneEnum, entity: EntityEnum) -> str:
        """Build the URL for the AELF API endpoint.

        Args:
            date (datetime): Date to fetch information for.
            zone (ZonesEnum): Liturgical zone to fetch information for.
            entity (EntityEnum): The liturgical entity to fetch information for.

        Returns:
            str: The constructed URL.
        """
        fr_entity_mapping: t.Dict[EntityEnum, str] = {
            EntityEnum.INFORMATIONS: "informations",
            EntityEnum.MASS: "messes",
            EntityEnum.COMPLINE: "complies",
            EntityEnum.LAUDS: "laudes",
            EntityEnum.READINGS: "lectures",
            EntityEnum.NONE: "none",
            EntityEnum.SEXT: "sexte",
            EntityEnum.TERCE: "tierce",
            EntityEnum.VESPERS: "vepres",
        }
        return f"{self.base_url}/v1/{fr_entity_mapping[entity]}/{date.strftime('%Y-%m-%d')}/{zone.value}"  # pylint: disable=line-too-long

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
        self, date: datetime, zone: ZoneEnum
    ) -> InformationsResponseModel:
        """Fetch liturgical information for a given date and zone.

        Args:
            date (datetime): Date to fetch information for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            InformationsResponseModel: Liturgical information for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.INFORMATIONS),
            model=InformationsResponseModel,
        )

    async def request_masses(self, date: datetime, zone: ZoneEnum) -> MassesResponseModel:
        """Fetch masses for a given date and zone.

        Args:
            date (datetime): Date to fetch masses for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            MassesResponseModel: Masses for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.MASS), model=MassesResponseModel
        )

    async def request_complines(self, date: datetime, zone: ZoneEnum) -> ComplinesResponseModel:
        """Fetch complines for a given date and zone.

        Args:
            date (datetime): Date to fetch complines for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            ComplinesResponseModel: Complines for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.COMPLINE), model=ComplinesResponseModel
        )

    async def request_lauds(self, date: datetime, zone: ZoneEnum) -> LaudsResponseModel:
        """Fetch lauds for a given date and zone.

        Args:
            date (datetime): Date to fetch lauds for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            LaudsResponseModel: Lauds for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.LAUDS), model=LaudsResponseModel
        )

    async def request_readings(self, date: datetime, zone: ZoneEnum) -> ReadingsResponseModel:
        """Fetch readings for a given date and zone.

        Args:
            date (datetime): Date to fetch readings for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            ReadingsResponseModel: Readings for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.READINGS), model=ReadingsResponseModel
        )

    async def request_none(self, date: datetime, zone: ZoneEnum) -> NoneResponseModel:
        """Fetch none for a given date and zone.

        Args:
            date (datetime): Date to fetch none for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            NoneResponseModel: none for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.NONE), model=NoneResponseModel
        )

    async def request_sext(self, date: datetime, zone: ZoneEnum) -> SextResponseModel:
        """Fetch sext for a given date and zone.

        Args:
            date (datetime): Date to fetch sext for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            SextResponseModel: Sext for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.SEXT), model=SextResponseModel
        )

    async def request_terce(self, date: datetime, zone: ZoneEnum) -> TerceResponseModel:
        """Fetch terce for a given date and zone.

        Args:
            date (datetime): Date to fetch terce for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            TerceResponseModel: Terce for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.TERCE), model=TerceResponseModel
        )

    async def request_vespers(self, date: datetime, zone: ZoneEnum) -> VespersResponseModel:
        """Fetch vespers for a given date and zone.

        Args:
            date (datetime): Date to fetch vespers for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            VespersResponseModel: Vespers for the given date and zone.
        """
        return await self.__request(
            url=self.__build_url(date, zone, EntityEnum.VESPERS), model=VespersResponseModel
        )

    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.INFORMATIONS], date: datetime, zone: ZoneEnum
    ) -> InformationsResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.MASS], date: datetime, zone: ZoneEnum
    ) -> MassesResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.COMPLINE], date: datetime, zone: ZoneEnum
    ) -> ComplinesResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.LAUDS], date: datetime, zone: ZoneEnum
    ) -> LaudsResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.READINGS], date: datetime, zone: ZoneEnum
    ) -> ReadingsResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.NONE], date: datetime, zone: ZoneEnum
    ) -> NoneResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.SEXT], date: datetime, zone: ZoneEnum
    ) -> SextResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.TERCE], date: datetime, zone: ZoneEnum
    ) -> TerceResponseModel: ...
    @t.overload
    async def request(
        self, entity: t.Literal[EntityEnum.VESPERS], date: datetime, zone: ZoneEnum
    ) -> VespersResponseModel: ...
    async def request(  # pylint: disable=too-many-return-statements
        self, entity: EntityEnum, date: datetime, zone: ZoneEnum
    ) -> (
        InformationsResponseModel
        | MassesResponseModel
        | ComplinesResponseModel
        | LaudsResponseModel
        | ReadingsResponseModel
        | NoneResponseModel
        | SextResponseModel
        | TerceResponseModel
        | VespersResponseModel
    ):
        """Fetch vespers for a given date and zone.

        Args:
            entity (EntityEnum): The liturgical entity to fetch information for.
            date (datetime): Date to fetch vespers for.
            zone (ZonesEnum): Liturgical zone to fetch information for.

        Returns:
            ResponseModel: Response model for the given entity.
        """
        match entity:
            case EntityEnum.INFORMATIONS:
                return await self.request_informations(date, zone)
            case EntityEnum.MASS:
                return await self.request_masses(date, zone)
            case EntityEnum.COMPLINE:
                return await self.request_complines(date, zone)
            case EntityEnum.LAUDS:
                return await self.request_lauds(date, zone)
            case EntityEnum.READINGS:
                return await self.request_readings(date, zone)
            case EntityEnum.NONE:
                return await self.request_none(date, zone)
            case EntityEnum.SEXT:
                return await self.request_sext(date, zone)
            case EntityEnum.TERCE:
                return await self.request_terce(date, zone)
            case EntityEnum.VESPERS:
                return await self.request_vespers(date, zone)
            case _:
                raise ValueError(f"Unknown entity: {entity}")
