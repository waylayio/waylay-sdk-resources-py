"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class SchemaValidationError(WaylayBaseModel):
    """SchemaValidationError."""

    schema_path: StrictStr | None = Field(default=None, alias="schemaPath")
    errors: dict[str, Any] | None = None
    keyword: StrictStr | None = None
    msgs: list[StrictStr] | None = None
    value: dict[str, Any] | None = None
    instance_path: StrictStr | None = Field(default=None, alias="instancePath")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
