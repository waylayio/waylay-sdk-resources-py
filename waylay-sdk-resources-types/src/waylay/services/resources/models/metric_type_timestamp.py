"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class MetricTypeTimestamp(str, Enum):
    """Value represents a unix timestamp. so basically a gauge or counter but we know we can also render the “age” at each point.."""

    TIMESTAMP = "timestamp"

    def __str__(self) -> str:
        return str(self.value)
