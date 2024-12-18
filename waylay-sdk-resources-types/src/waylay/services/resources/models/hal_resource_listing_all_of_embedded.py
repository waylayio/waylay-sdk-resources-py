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
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.hal_resource_entity import HALResourceEntity


class HALResourceListingAllOfEmbedded(WaylayBaseModel):
    """HALResourceListingAllOfEmbedded."""

    values: List[HALResourceEntity] = Field(
        description="_Resource_ entities in HAL format"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
