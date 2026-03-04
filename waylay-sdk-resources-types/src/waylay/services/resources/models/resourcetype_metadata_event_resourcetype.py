"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ResourcetypeMetadataEventResourcetype(str, Enum):
    """ResourcetypeMetadataEventResourcetype."""

    RESOURCETYPE = "resourcetype"

    def __str__(self) -> str:
        return str(self.value)
