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


class HALSelfLinksLinksValue(WaylayBaseModel):
    """HALSelfLinksLinksValue."""

    href: StrictStr = Field(description="(Relative) URL of the entity.")
    id: StrictStr = Field(description="Unique identifier of the linked item")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
