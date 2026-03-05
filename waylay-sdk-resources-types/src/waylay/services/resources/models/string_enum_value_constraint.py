"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.numeric_enum_value_constraint_type import NumericEnumValueConstraintType
from ..models.string_value_constraint_type import StringValueConstraintType


class StringEnumValueConstraint(WaylayBaseModel):
    """Specifies that a value must be one of the given strings.."""

    type: NumericEnumValueConstraintType
    enum_type: StringValueConstraintType = Field(alias="enumType")
    items: Annotated[list[StrictStr], Field(min_length=1)]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
