"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_id import ResourceId


class ConstraintError(WaylayBaseModel):
    """Validation Error report of a Resource Constraint."""

    error: StrictStr = Field(description="User error message")
    error_path: StrictStr = Field(description="Attribute path", alias="errorPath")
    resources: list[ResourceId] = Field(
        description="Ids of the _Resources_ that fail the constraint"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
