# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from rlink_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from rlink_client import schemas  # noqa: F401

from . import path

# Query params
AppBinaryChecksumSchema = schemas.IntSchema
CallNumSchema = schemas.IntSchema
DataChecksumSchema = schemas.IntSchema
LastCallTimeSchema = schemas.StrSchema
MatchTypeIdSchema = schemas.IntSchema
ModDLLChecksumSchema = schemas.IntSchema
ModDLLFileSchema = schemas.StrSchema
ModNameSchema = schemas.StrSchema
ModVersionSchema = schemas.StrSchema
ProfileIdsSchema = schemas.IntSchema
RaceIdsSchema = schemas.IntSchema
StatGroupIdsSchema = schemas.IntSchema
VersionFlagsSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'appBinaryChecksum': typing.Union[AppBinaryChecksumSchema, decimal.Decimal, int, ],
        'callNum': typing.Union[CallNumSchema, decimal.Decimal, int, ],
        'dataChecksum': typing.Union[DataChecksumSchema, decimal.Decimal, int, ],
        'lastCallTime': typing.Union[LastCallTimeSchema, str, ],
        'matchType_id': typing.Union[MatchTypeIdSchema, decimal.Decimal, int, ],
        'modDLLChecksum': typing.Union[ModDLLChecksumSchema, decimal.Decimal, int, ],
        'modDLLFile': typing.Union[ModDLLFileSchema, str, ],
        'modName': typing.Union[ModNameSchema, str, ],
        'modVersion': typing.Union[ModVersionSchema, str, ],
        'profile_ids': typing.Union[ProfileIdsSchema, decimal.Decimal, int, ],
        'race_ids': typing.Union[RaceIdsSchema, decimal.Decimal, int, ],
        'statGroup_ids': typing.Union[StatGroupIdsSchema, decimal.Decimal, int, ],
        'versionFlags': typing.Union[VersionFlagsSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_app_binary_checksum = api_client.QueryParameter(
    name="appBinaryChecksum",
    style=api_client.ParameterStyle.FORM,
    schema=AppBinaryChecksumSchema,
    required=True,
    explode=True,
)
request_query_call_num = api_client.QueryParameter(
    name="callNum",
    style=api_client.ParameterStyle.FORM,
    schema=CallNumSchema,
    required=True,
    explode=True,
)
request_query_data_checksum = api_client.QueryParameter(
    name="dataChecksum",
    style=api_client.ParameterStyle.FORM,
    schema=DataChecksumSchema,
    required=True,
    explode=True,
)
request_query_last_call_time = api_client.QueryParameter(
    name="lastCallTime",
    style=api_client.ParameterStyle.FORM,
    schema=LastCallTimeSchema,
    required=True,
    explode=True,
)
request_query_match_type_id = api_client.QueryParameter(
    name="matchType_id",
    style=api_client.ParameterStyle.FORM,
    schema=MatchTypeIdSchema,
    required=True,
    explode=True,
)
request_query_mod_dll_checksum = api_client.QueryParameter(
    name="modDLLChecksum",
    style=api_client.ParameterStyle.FORM,
    schema=ModDLLChecksumSchema,
    required=True,
    explode=True,
)
request_query_mod_dll_file = api_client.QueryParameter(
    name="modDLLFile",
    style=api_client.ParameterStyle.FORM,
    schema=ModDLLFileSchema,
    required=True,
    explode=True,
)
request_query_mod_name = api_client.QueryParameter(
    name="modName",
    style=api_client.ParameterStyle.FORM,
    schema=ModNameSchema,
    required=True,
    explode=True,
)
request_query_mod_version = api_client.QueryParameter(
    name="modVersion",
    style=api_client.ParameterStyle.FORM,
    schema=ModVersionSchema,
    required=True,
    explode=True,
)
request_query_profile_ids = api_client.QueryParameter(
    name="profile_ids",
    style=api_client.ParameterStyle.FORM,
    schema=ProfileIdsSchema,
    required=True,
    explode=True,
)
request_query_race_ids = api_client.QueryParameter(
    name="race_ids",
    style=api_client.ParameterStyle.FORM,
    schema=RaceIdsSchema,
    required=True,
    explode=True,
)
request_query_stat_group_ids = api_client.QueryParameter(
    name="statGroup_ids",
    style=api_client.ParameterStyle.FORM,
    schema=StatGroupIdsSchema,
    required=True,
    explode=True,
)
request_query_version_flags = api_client.QueryParameter(
    name="versionFlags",
    style=api_client.ParameterStyle.FORM,
    schema=VersionFlagsSchema,
    required=True,
    explode=True,
)
_auth = [
    'sessionID',
    'connectID',
]
SchemaFor200ResponseBodyApplicationJson = schemas.AnyTypeSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _game_advertisement_find_advertisements_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _game_advertisement_find_advertisements_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _game_advertisement_find_advertisements_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _game_advertisement_find_advertisements_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_app_binary_checksum,
            request_query_call_num,
            request_query_data_checksum,
            request_query_last_call_time,
            request_query_match_type_id,
            request_query_mod_dll_checksum,
            request_query_mod_dll_file,
            request_query_mod_name,
            request_query_mod_version,
            request_query_profile_ids,
            request_query_race_ids,
            request_query_stat_group_ids,
            request_query_version_flags,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GameAdvertisementFindAdvertisements(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def game_advertisement_find_advertisements(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def game_advertisement_find_advertisements(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def game_advertisement_find_advertisements(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def game_advertisement_find_advertisements(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._game_advertisement_find_advertisements_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._game_advertisement_find_advertisements_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


