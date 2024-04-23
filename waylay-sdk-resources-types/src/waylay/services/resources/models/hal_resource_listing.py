# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.hal_resource_listing_all_of_embedded import (
    HALResourceListingAllOfEmbedded,
)
from ..models.pagination_links import PaginationLinks


class HALResourceListing(WaylayBaseModel):
    """Listing of _Resource_ entities in HAL format."""

    skip: StrictInt = Field(
        description="Number of items skipped before this page of results."
    )
    limit: StrictInt = Field(description="Size of one page of results.")
    total: StrictInt = Field(
        description="Total number of items matching the query of which this is one page of results."
    )
    count: StrictInt = Field(description="The number of items in this result page.")
    links: PaginationLinks = Field(alias="_links")
    embedded: HALResourceListingAllOfEmbedded = Field(alias="_embedded")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
