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

from ..models.children_resource_link import ChildrenResourceLink
from ..models.parent_resource_link import ParentResourceLink
from ..models.resource_type_link import ResourceTypeLink


class ResourceHALLinks(WaylayBaseModel):
    """ResourceHALLinks."""

    parent: ParentResourceLink | None = None
    children: ChildrenResourceLink | None = None
    resource_type: ResourceTypeLink | None = Field(
        default=None, alias="resourceType"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
