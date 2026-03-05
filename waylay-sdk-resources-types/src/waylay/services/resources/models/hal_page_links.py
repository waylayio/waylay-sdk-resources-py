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

from ..models.pagination_links import PaginationLinks


class HALPageLinks(WaylayBaseModel):
    """HALPageLinks."""

    links: PaginationLinks | None = Field(default=None, alias="_links")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
