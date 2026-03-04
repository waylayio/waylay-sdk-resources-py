"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.string_value_constraint_type import StringValueConstraintType


class StringValueConstraint(WaylayBaseModel):
    """Specifies that a value must be a string.."""

    type: StringValueConstraintType | None = None
    min_length: Annotated[int, Field(strict=True, ge=0)] | None = Field(
        default=None, description="Minimum length a value must have", alias="minLength"
    )
    max_length: Annotated[int, Field(strict=True, ge=0)] | None = Field(
        default=None, description="Maximum length a value can have", alias="maxLength"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
