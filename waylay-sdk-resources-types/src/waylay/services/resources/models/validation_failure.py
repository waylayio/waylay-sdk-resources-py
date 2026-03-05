"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.schema_validation_error import SchemaValidationError


class ValidationFailure(WaylayBaseModel):
    """ValidationFailure."""

    status_code: StrictInt = Field(alias="statusCode")
    error: StrictStr
    code: StrictStr | None = Field(default=None, description="Optional error code")
    details: list[SchemaValidationError] | None = Field(
        default=None, description="List of SchemaValidationErrors"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
