"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class MetricTypeCounter(str, Enum):
    """Keeps increasing over time (but might wrap/reset at some point) i.e. a gauge with the added notion of “i usually want to derive this to see the rate”."""

    COUNTER = "counter"

    def __str__(self) -> str:
        return str(self.value)
