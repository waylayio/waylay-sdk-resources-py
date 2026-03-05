"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class GenericMetadataEvent(WaylayBaseModel):
    """GenericMetadataEvent."""

    type: StrictStr
    object_type: StrictStr = Field(alias="objectType")
    timestamp: datetime

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
