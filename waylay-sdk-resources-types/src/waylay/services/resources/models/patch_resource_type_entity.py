"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_type_id import ResourceTypeId


class PatchResourceTypeEntity(WaylayBaseModel):
    """PatchResourceTypeEntity."""

    id: ResourceTypeId | None = None
    name: Any | None = None
    icon: Any | None = None
    templates: Any | None = None
    provider: Any | None = None
    provider_id: Any | None = Field(default=None, alias="providerId")
    customer: Any | None = None
    firmware: Any | None = None
    location: Any | None = None
    metrics: Any | None = None
    sensors: Any | None = None
    constraints: list[Annotated[str, Field(strict=True)]] | None = Field(
        default=None,
        description="Validation constraint to be applied to each _Resource_ that has its `resourceTypeId` attribute set to the `id` of this _Resource Type_.",
        alias="$constraints",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
