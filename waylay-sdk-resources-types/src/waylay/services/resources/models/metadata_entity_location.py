"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class MetadataEntityLocation(WaylayBaseModel):
    """A global location, expressed as a longitude-latitude pair.."""

    lat: StrictFloat | StrictInt = Field(
        description="The latitude degrees of a location."
    )
    lon: StrictFloat | StrictInt = Field(
        description="The longitudinal degrees of a location."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
