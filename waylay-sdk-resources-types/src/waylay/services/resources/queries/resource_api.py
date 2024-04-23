# coding: utf-8
"""Waylay Resources query parameters.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_id import ResourceId


def _create_query_alias_for(field_name: str) -> str:
    return field_name


class CreateQuery(WaylayBaseModel):
    """Model for `create` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_create_query_alias_for,
        populate_by_name=True,
    )


def _delete_query_alias_for(field_name: str) -> str:
    return field_name


class DeleteQuery(WaylayBaseModel):
    """Model for `delete` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_delete_query_alias_for,
        populate_by_name=True,
    )


def _get_query_alias_for(field_name: str) -> str:
    if field_name == "denormalized":
        return "denormalized"
    if field_name == "field":
        return "field"
    if field_name == "fields":
        return "fields"
    return field_name


class GetQuery(WaylayBaseModel):
    """Model for `get` query parameters."""

    denormalized: Annotated[
        StrictBool | None,
        Field(
            description="Unless explicitly set to `false`, attributes inherited from a linked _Resource Type_ will be included in the representation."
        ),
    ] = None
    field: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (repeated)."
        ),
    ] = None
    fields: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (comma-separated)."
        ),
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_query_alias_for,
        populate_by_name=True,
    )


def _list_changes_query_alias_for(field_name: str) -> str:
    if field_name == "skip":
        return "skip"
    if field_name == "limit":
        return "limit"
    return field_name


class ListChangesQuery(WaylayBaseModel):
    """Model for `list_changes` query parameters."""

    skip: Annotated[
        StrictInt | None, Field(description="(Paging) items to skip in the listing")
    ] = None
    limit: Annotated[
        StrictInt | None, Field(description="(Paging) maximal number of items returned")
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_changes_query_alias_for,
        populate_by_name=True,
    )


def _list_children_query_alias_for(field_name: str) -> str:
    if field_name == "denormalized":
        return "denormalized"
    if field_name == "field":
        return "field"
    if field_name == "fields":
        return "fields"
    if field_name == "skip":
        return "skip"
    if field_name == "limit":
        return "limit"
    return field_name


class ListChildrenQuery(WaylayBaseModel):
    """Model for `list_children` query parameters."""

    denormalized: Annotated[
        StrictBool | None,
        Field(
            description="Unless explicitly set to `false`, attributes inherited from a linked _Resource Type_ will be included in the representation."
        ),
    ] = None
    field: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (repeated)."
        ),
    ] = None
    fields: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (comma-separated)."
        ),
    ] = None
    skip: Annotated[
        StrictInt | None, Field(description="(Paging) items to skip in the listing")
    ] = None
    limit: Annotated[
        StrictInt | None, Field(description="(Paging) maximal number of items returned")
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_children_query_alias_for,
        populate_by_name=True,
    )


def _list_referrers_query_alias_for(field_name: str) -> str:
    if field_name == "field":
        return "field"
    if field_name == "fields":
        return "fields"
    if field_name == "skip":
        return "skip"
    if field_name == "limit":
        return "limit"
    return field_name


class ListReferrersQuery(WaylayBaseModel):
    """Model for `list_referrers` query parameters."""

    field: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (repeated)."
        ),
    ] = None
    fields: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (comma-separated)."
        ),
    ] = None
    skip: Annotated[
        StrictInt | None, Field(description="(Paging) items to skip in the listing")
    ] = None
    limit: Annotated[
        StrictInt | None, Field(description="(Paging) maximal number of items returned")
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_referrers_query_alias_for,
        populate_by_name=True,
    )


def _list_query_alias_for(field_name: str) -> str:
    if field_name == "skip":
        return "skip"
    if field_name == "limit":
        return "limit"
    if field_name == "field":
        return "field"
    if field_name == "fields":
        return "fields"
    if field_name == "filter":
        return "filter"
    if field_name == "query":
        return "query"
    if field_name == "tag":
        return "tag"
    if field_name == "id":
        return "id"
    if field_name == "provider":
        return "provider"
    if field_name == "customer":
        return "customer"
    if field_name == "resource_type_id":
        return "resourceTypeId"
    if field_name == "lat":
        return "lat"
    if field_name == "lon":
        return "lon"
    if field_name == "distance":
        return "distance"
    if field_name == "toplevel_only":
        return "toplevelOnly"
    return field_name


class ListQuery(WaylayBaseModel):
    """Model for `list` query parameters."""

    skip: Annotated[
        StrictInt | None, Field(description="(Paging) items to skip in the listing")
    ] = None
    limit: Annotated[
        StrictInt | None, Field(description="(Paging) maximal number of items returned")
    ] = None
    field: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (repeated)."
        ),
    ] = None
    fields: Annotated[
        List[StrictStr] | None,
        Field(
            description="Select which attributes to render for each matching _Resource_ (comma-separated)."
        ),
    ] = None
    filter: Annotated[
        StrictStr | None, Field(description="(Filter) fuzzy search on multiple fields.")
    ] = None
    query: Annotated[
        StrictStr | None,
        Field(
            description="Search string using a query language consisting of > `<metadata key>:<operation>(<arguments>)`  Supported operations are - `eq`: equals - exact match - `in`: in - exact match - arguments are a (comma-separated) list of values - `lt`: smaller then - `lte`: smaller then or equal - `gt`: greater then - `gte`: greater then or equal - `ref`: references - argument should be uri /resources/<resourceId> - `exists`: check if the _Resource_ has the specified metadata key - no argument allowed - `like`: wildcard search - argument should contain * and/or ?  For more info see [Waylay Docs](/#/api/resources/?id=metadata-query-language)"
        ),
    ] = None
    tag: List[StrictStr] | None = None
    id: List[ResourceId] | None = None
    provider: StrictStr | None = None
    customer: StrictStr | None = None
    resource_type_id: StrictStr | None = None
    lat: StrictFloat | StrictInt | None = None
    lon: StrictFloat | StrictInt | None = None
    distance: StrictStr | None = None
    toplevel_only: Annotated[
        StrictBool | None,
        Field(description="If true, search only for _Resources_ without parent."),
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_query_alias_for,
        populate_by_name=True,
    )


def _patch_query_alias_for(field_name: str) -> str:
    return field_name


class PatchQuery(WaylayBaseModel):
    """Model for `patch` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_patch_query_alias_for,
        populate_by_name=True,
    )


def _replace_query_alias_for(field_name: str) -> str:
    return field_name


class ReplaceQuery(WaylayBaseModel):
    """Model for `replace` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_replace_query_alias_for,
        populate_by_name=True,
    )
