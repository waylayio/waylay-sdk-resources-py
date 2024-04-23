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
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.hal_resource_type_entity import HALResourceTypeEntity


class HALResourceEntityAllOfEmbedded(WaylayBaseModel):
    """HALResourceEntityAllOfEmbedded."""

    resource_type: HALResourceTypeEntity | None = Field(
        default=None, alias="resourceType"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
