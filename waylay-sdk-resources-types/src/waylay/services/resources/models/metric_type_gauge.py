"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class MetricTypeGauge(str, Enum):
    """Values at each point in time."""

    GAUGE = "gauge"

    def __str__(self) -> str:
        return str(self.value)
