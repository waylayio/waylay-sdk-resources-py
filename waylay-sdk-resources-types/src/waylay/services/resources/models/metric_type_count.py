"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class MetricTypeCount(str, Enum):
    """A number per a given interval (such as a statsd flushInterval)."""

    COUNT = "count"

    def __str__(self) -> str:
        return str(self.value)
