# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, List

from pydantic import (
    ConfigDict,
    Field,
)
from typing_extensions import (
    Annotated,  # >=3.11
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_type_id import ResourceTypeId


class PatchResourceTypeEntity(WaylayBaseModel):
    """PatchResourceTypeEntity."""

    id: ResourceTypeId | None = None
    name: Any | None = None
    templates: Any | None = None
    provider: Any | None = None
    provider_id: Any | None = Field(default=None, alias="providerId")
    customer: Any | None = None
    firmware: Any | None = None
    location: Any | None = None
    metrics: Any | None = None
    sensors: Any | None = None
    constraints: List[Annotated[str, Field(strict=True)]] | None = Field(
        default=None,
        description="Validation constraint to be applied to each _Resource_ that has its `resourceTypeId` attribute set to the `id` of this _Resource Type_.",
        alias="$constraints",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
