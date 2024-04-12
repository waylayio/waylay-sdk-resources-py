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
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel
from waylay.sdk.api._models import Model as GenericModel


class AttributeItem(WaylayBaseModel):
    """Constraint on the presence and value of a single named _Resource_ attribute.."""

    name: StrictStr = Field(description="name of the attribute")
    required: StrictBool = Field(
        description="Indicates if the attribute must be present or is optional"
    )
    type: GenericModel

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
