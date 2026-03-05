"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.hal_resource_entity import HALResourceEntity


class ResourceListingHALEmbedded(WaylayBaseModel):
    """ResourceListingHALEmbedded."""

    values: list[HALResourceEntity] = Field(
        description="_Resource_ entities in HAL format"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
