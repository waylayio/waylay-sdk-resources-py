"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.discovered_event_type import DiscoveredEventType


class DiscoveredEvent(WaylayBaseModel):
    """DiscoveredEvent."""

    type: DiscoveredEventType | None = None
    message: dict[str, Any] | None = Field(
        default=None, description="The broker message that triggered the discovery"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
