# coding: utf-8
"""Waylay Resources api tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import re
from importlib.util import find_spec
from typing import List, Union
from urllib.parse import quote

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.resources.api import ResourceTypeApi
from waylay.services.resources.service import ResourcesService

from ..types.patch_resource_type_entity_stub import PatchResourceTypeEntityStub
from ..types.resource_constraint_with_id_entity_stub import (
    ResourceConstraintWithIdEntityStub,
)
from ..types.resource_type_change_stub import ResourceTypeChangeStub
from ..types.resource_type_creation_response_stub import (
    ResourceTypeCreationResponseStub,
)
from ..types.resource_type_id_stub import ResourceTypeIdStub
from ..types.resource_type_listing_stub import ResourceTypeListingStub
from ..types.resource_type_with_constraints_stub import ResourceTypeWithConstraintsStub
from ..types.resource_type_with_id_entity_stub import ResourceTypeWithIdEntityStub

MODELS_AVAILABLE = (
    True if find_spec("waylay.services.resources.models") is not None else False
)

if MODELS_AVAILABLE:
    from waylay.services.resources.models import (
        ResourceConstraintWithIdEntity,
        ResourceTypeChange,
        ResourceTypeCreationResponse,
        ResourceTypeListing,
        ResourceTypeWithIdEntity,
    )
    from waylay.services.resources.queries.resource_type_api import (
        GetQuery,
        ListChangesQuery,
        ListQuery,
    )


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def resource_type_api(waylay_api_client: ApiClient) -> ResourceTypeApi:
    return ResourceTypeApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that ResourceTypeApi api is registered in the sdk client."""
    assert isinstance(waylay_client.resources.resource_type, ResourceTypeApi)


def _create_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = ResourceTypeCreationResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": re.compile(f"^{gateway_url}/resources/v1/resourcetypes(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_create(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for create
    Create Resource Type
    """
    # set path params
    kwargs = {
        "json": ResourceTypeWithConstraintsStub.create_instance(),
    }
    _create_set_mock_response(httpx_mock, gateway_url)
    resp = await service.resource_type.create(**kwargs)
    check_type(resp, Union[ResourceTypeCreationResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_create_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for create with models not installed
    Create Resource Type
    """
    # set path params
    kwargs = {
        "json": ResourceTypeWithConstraintsStub.create_json(),
    }
    _create_set_mock_response(httpx_mock, gateway_url)
    resp = await service.resource_type.create(**kwargs)
    check_type(resp, Model)


def _delete_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, resourceTypeId: str
):
    mock_response = None
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": re.compile(
            f"^{gateway_url}/resources/v1/resourcetypes/{resourceTypeId}(\\?.*)?"
        ),
        "content": mock_response,
        "status_code": 204,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_delete(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for delete
    Remove Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {}
    _delete_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.delete(resourceTypeId, **kwargs)
    assert not resp


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_delete_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for delete with models not installed
    Remove Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {}
    _delete_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.delete(resourceTypeId, **kwargs)
    assert not resp


def _get_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, resourceTypeId: str
):
    mock_response = ResourceTypeWithIdEntityStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/resources/v1/resourcetypes/{resourceTypeId}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get(service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Get Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        # optionally use GetQuery to validate and reuse parameters
        "query": GetQuery(
            var_field=[""],
            fields=[],
        ),
    }
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.get(resourceTypeId, **kwargs)
    check_type(resp, Union[ResourceTypeWithIdEntity,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get with models not installed
    Get Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        "query": {
            "field": [""],
            "fields": [],
        },
    }
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.get(resourceTypeId, **kwargs)
    check_type(resp, Model)


def _list_changes_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, resourceTypeId: str
):
    mock_response = [ResourceTypeChangeStub.create_json()]
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/resources/v1/resourcetypes/{resourceTypeId}/changes(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_list_changes(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list_changes
    List Resource Type Changes
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        # optionally use ListChangesQuery to validate and reuse parameters
        "query": ListChangesQuery(
            skip=0,
            limit=100,
        ),
    }
    _list_changes_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.list_changes(resourceTypeId, **kwargs)
    check_type(resp, Union[List[ResourceTypeChange],])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_list_changes_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list_changes with models not installed
    List Resource Type Changes
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        "query": {
            "skip": 0,
            "limit": 100,
        },
    }
    _list_changes_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.list_changes(resourceTypeId, **kwargs)
    check_type(resp, Model)


def _list_constraints_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, resourceTypeId: str
):
    mock_response = ResourceConstraintWithIdEntityStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/resources/v1/resourcetypes/{resourceTypeId}/constraints(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_list_constraints(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list_constraints
    Get Resource Type Constraints
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {}
    _list_constraints_set_mock_response(
        httpx_mock, gateway_url, quote(str(resourceTypeId))
    )
    resp = await service.resource_type.list_constraints(resourceTypeId, **kwargs)
    check_type(resp, Union[ResourceConstraintWithIdEntity,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_list_constraints_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list_constraints with models not installed
    Get Resource Type Constraints
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {}
    _list_constraints_set_mock_response(
        httpx_mock, gateway_url, quote(str(resourceTypeId))
    )
    resp = await service.resource_type.list_constraints(resourceTypeId, **kwargs)
    check_type(resp, Model)


def _list_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = ResourceTypeListingStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/resources/v1/resourcetypes(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_list(service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for list
    List Resource Types
    """
    # set path params
    kwargs = {
        # optionally use ListQuery to validate and reuse parameters
        "query": ListQuery(
            skip=0,
            limit=100,
            var_field=[],
            fields=[],
            filter="needle",
            query="address.city:in(Ghent,Brussels)",
            id=[],
            template="MonitoringTemplate_3443",
        ),
    }
    _list_set_mock_response(httpx_mock, gateway_url)
    resp = await service.resource_type.list(**kwargs)
    check_type(resp, Union[ResourceTypeListing,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_list_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list with models not installed
    List Resource Types
    """
    # set path params
    kwargs = {
        "query": {
            "skip": 0,
            "limit": 100,
            "field": [],
            "fields": [],
            "filter": "needle",
            "query": "address.city:in(Ghent,Brussels)",
            "id": [],
            "template": "MonitoringTemplate_3443",
        },
    }
    _list_set_mock_response(httpx_mock, gateway_url)
    resp = await service.resource_type.list(**kwargs)
    check_type(resp, Model)


def _patch_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, resourceTypeId: str
):
    mock_response = ResourceTypeCreationResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PATCH",
        "url": re.compile(
            f"^{gateway_url}/resources/v1/resourcetypes/{resourceTypeId}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_patch(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for patch
    Create Or Update Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        "json": PatchResourceTypeEntityStub.create_instance(),
    }
    _patch_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.patch(resourceTypeId, **kwargs)
    check_type(
        resp,
        Union[
            ResourceTypeCreationResponse,
            ResourceTypeWithIdEntity,
        ],
    )


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_patch_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for patch with models not installed
    Create Or Update Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        "json": PatchResourceTypeEntityStub.create_json(),
    }
    _patch_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.patch(resourceTypeId, **kwargs)
    check_type(resp, Model)


def _replace_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, resourceTypeId: str
):
    mock_response = ResourceTypeWithIdEntityStub.create_json()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": re.compile(
            f"^{gateway_url}/resources/v1/resourcetypes/{resourceTypeId}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 202,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_replace(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for replace
    Update Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        "json": ResourceTypeWithConstraintsStub.create_instance(),
    }
    _replace_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.replace(resourceTypeId, **kwargs)
    check_type(resp, Union[ResourceTypeWithIdEntity,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_replace_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for replace with models not installed
    Update Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {
        "json": ResourceTypeWithConstraintsStub.create_json(),
    }
    _replace_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.replace(resourceTypeId, **kwargs)
    check_type(resp, Model)


def _revalidate_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, resourceTypeId: str
):
    mock_response = ResourceTypeWithIdEntityStub.create_json()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": re.compile(
            f"^{gateway_url}/resources/v1/resourcetypes/{resourceTypeId}/revalidate(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 202,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_revalidate(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for revalidate
    Revalidate Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {}
    _revalidate_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.revalidate(resourceTypeId, **kwargs)
    check_type(resp, Union[ResourceTypeWithIdEntity,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_revalidate_without_types(
    service: ResourcesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for revalidate with models not installed
    Revalidate Resource Type
    """
    # set path params
    resourceTypeId = ResourceTypeIdStub.create_json()

    kwargs = {}
    _revalidate_set_mock_response(httpx_mock, gateway_url, quote(str(resourceTypeId)))
    resp = await service.resource_type.revalidate(resourceTypeId, **kwargs)
    check_type(resp, Model)
