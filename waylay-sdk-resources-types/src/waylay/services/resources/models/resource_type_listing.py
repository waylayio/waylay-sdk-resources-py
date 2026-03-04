"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_type_with_id_entity import ResourceTypeWithIdEntity


class ResourceTypeListing(WaylayBaseModel):
    """A listing of _Resource Type_ entities."""

    skip: StrictInt = Field(
        description="Number of items skipped before this page of results."
    )
    limit: StrictInt = Field(description="Size of one page of results.")
    total: StrictInt = Field(
        description="Total number of items matching the query of which this is one page of results."
    )
    values: list[ResourceTypeWithIdEntity]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
