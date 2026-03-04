"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class GetStreamEventFormatParameter(str, Enum):
    """GetStreamEventFormatParameter."""

    APPLICATION_SLASH_CLOUDEVENTS_PLUS_JSON = "application/cloudevents+json"

    def __str__(self) -> str:
        return str(self.value)
