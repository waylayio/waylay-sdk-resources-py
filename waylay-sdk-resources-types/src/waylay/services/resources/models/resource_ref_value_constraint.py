"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.attribute_item import AttributeItem
from ..models.resource_ref_value_constraint_type import ResourceRefValueConstraintType
from ..models.resource_type_id import ResourceTypeId


class ResourceRefValueConstraint(WaylayBaseModel):
    """Specifies that a value is an object having a required '$ref' attribute that references another _Resource_.."""

    type: ResourceRefValueConstraintType | None = None
    attributes: list[AttributeItem] | None = Field(
        default=None,
        description="Additional attributes in the reference object, describing the relation.",
    )
    resource_types: list[ResourceTypeId] | None = Field(
        default=None,
        description="The possible _Resource Types_ for the referenced _Resource_.",
        alias="resourceTypes",
    )
    exists: StrictBool | None = Field(
        default=False,
        description="Flag to indicate if the referenced _Resource_ must exist",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
