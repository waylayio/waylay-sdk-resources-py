"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class PagingCount(WaylayBaseModel):
    """PagingCount."""

    count: StrictInt | None = Field(
        default=None, description="The number of items in this result page."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
