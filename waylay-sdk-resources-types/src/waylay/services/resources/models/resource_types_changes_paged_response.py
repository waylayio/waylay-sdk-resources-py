# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_type_change import ResourceTypeChange


class ResourceTypesChangesPagedResponse(WaylayBaseModel):
    """ResourceTypesChangesPagedResponse."""

    skip: StrictInt = Field(
        description="Number of items skipped before this page of results."
    )
    limit: StrictInt = Field(description="Size of one page of results.")
    total: StrictInt = Field(
        description="Total number of items matching the query of which this is one page of results."
    )
    values: List[ResourceTypeChange] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
