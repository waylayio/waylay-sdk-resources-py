"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.cascade_delete_option import CascadeDeleteOption
from ..models.discovered_event_type import DiscoveredEventType
from ..models.resource_entity import ResourceEntity
from ..models.resource_metadata_event_resource import ResourceMetadataEventResource


class ResourceMetadataEvent(WaylayBaseModel):
    """ResourceMetadataEvent."""

    type: DiscoveredEventType
    object_type: ResourceMetadataEventResource = Field(alias="objectType")
    timestamp: datetime
    resource: ResourceEntity
    cascade_delete: list[CascadeDeleteOption] | None = Field(
        default=None, alias="cascadeDelete"
    )
    old_values: dict[str, Any] | None = Field(
        default=None,
        description="old values of all attributes that have changed",
        alias="oldValues",
    )
    message: dict[str, Any] | None = Field(
        default=None, description="The broker message that triggered the discovery"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
