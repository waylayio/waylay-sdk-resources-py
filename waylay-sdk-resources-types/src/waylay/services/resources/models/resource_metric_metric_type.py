"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.metric_type_count import MetricTypeCount
from ..models.metric_type_counter import MetricTypeCounter
from ..models.metric_type_gauge import MetricTypeGauge
from ..models.metric_type_rate import MetricTypeRate
from ..models.metric_type_timestamp import MetricTypeTimestamp

ResourceMetricMetricType: TypeAlias = MetricTypeRate | MetricTypeCount | MetricTypeGauge | MetricTypeCounter | MetricTypeTimestamp
"""How measurements should be treated as a time series.."""
