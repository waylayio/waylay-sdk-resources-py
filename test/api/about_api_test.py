# coding: utf-8
"""Waylay Resources api tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import re
from importlib.util import find_spec
from typing import Union

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.resources.api import AboutApi
from waylay.services.resources.service import ResourcesService

from ..types.version_response_stub import VersionResponseStub

MODELS_AVAILABLE = (
    True if find_spec("waylay.services.resources.models") is not None else False
)

if MODELS_AVAILABLE:
    from waylay.services.resources.models import VersionResponse


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def about_api(waylay_api_client: ApiClient) -> AboutApi:
    return AboutApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that AboutApi api is registered in the sdk client."""
    assert isinstance(waylay_client.resources.about, AboutApi)


def _get_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = VersionResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/resources/v1/(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get(service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Get Service Information
    """
    # set path params
    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url)
    resp = await service.about.get(**kwargs)
    check_type(resp, Union[VersionResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get with models not installed
    Get Service Information
    """
    # set path params
    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url)
    resp = await service.about.get(**kwargs)
    check_type(resp, Model)
