"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ResourceMetadataEventResource(str, Enum):
    """ResourceMetadataEventResource."""

    RESOURCE = "resource"

    def __str__(self) -> str:
        return str(self.value)
