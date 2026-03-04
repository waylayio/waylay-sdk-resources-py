"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class MetricTypeRate(str, Enum):
    """A number per second (implies that unit ends on ‘/s’)."""

    RATE = "rate"

    def __str__(self) -> str:
        return str(self.value)
