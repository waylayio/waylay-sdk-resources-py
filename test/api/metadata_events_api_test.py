# coding: utf-8
"""Waylay Resources api tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import re
from importlib.util import find_spec
from typing import AsyncIterator, Union, get_args

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.resources.api import MetadataEventsApi
from waylay.services.resources.service import ResourcesService

from ..types.nd_json_response_stream_stub import NdJsonResponseStreamStub

MODELS_AVAILABLE = (
    True if find_spec("waylay.services.resources.models") is not None else False
)

if MODELS_AVAILABLE:
    from waylay.services.resources.models import NdJsonResponseStream
    from waylay.services.resources.queries.metadata_events_api import GetStreamQuery


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def metadata_events_api(waylay_api_client: ApiClient) -> MetadataEventsApi:
    return MetadataEventsApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that MetadataEventsApi api is registered in the sdk client."""
    assert isinstance(waylay_client.resources.metadata_events, MetadataEventsApi)


def _get_stream_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = NdJsonResponseStreamStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/resources/v1/events(\\?.*)?"),
        "content": json.dumps(mock_response, default=str) + "\n",
        "status_code": 200,
        "headers": {"content-type": "application/x-ndjson"},
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get_stream(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get_stream
    Events
    """
    # set path params
    kwargs = {
        # optionally use GetStreamQuery to validate and reuse parameters
        "query": GetStreamQuery(
            event_format="application/cloudevents+json",
        ),
    }
    _get_stream_set_mock_response(httpx_mock, gateway_url)
    resp = await service.metadata_events.get_stream(**kwargs)
    check_type(resp, Union[AsyncIterator[NdJsonResponseStream],])
    async for item in resp:
        check_type(item, get_args(Union[AsyncIterator[NdJsonResponseStream],])[0])
        break  # Test only the first value


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_stream_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get_stream with models not installed
    Events
    """
    # set path params
    kwargs = {
        "query": {
            "eventFormat": "application/cloudevents+json",
        },
    }
    _get_stream_set_mock_response(httpx_mock, gateway_url)
    resp = await service.metadata_events.get_stream(**kwargs)
    check_type(resp, Model)
    async for item in resp:
        check_type(item, Model)
        break  # Test only the first value
