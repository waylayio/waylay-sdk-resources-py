# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from pydantic_core import from_json
from typing import Callable, Union
from typing import cast
from typing_extensions import (
    Self,  # >=3.11
)

from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from ..models.resource_metric_metric_type import ResourceMetricMetricType


class ResourceMetric(BaseModel):
    """Describes a value that is expected to be present in the events sent to Waylay on behalf of this _Resource (Type)_. By default, such values will end up in the time series database, where each time series is identified by the _resource id_ and the _metric name_.  > Note: The Waylay System does not enforce any of the statements made in a _Resource Metric_ when > processing or retrieving data. As long as a user does not explicitly use this metadata to configure > behaviour, a _Resource Metric_ is purely a documentation entity.."""

    name: StrictStr = Field(
        description="The key under which values of this metric are present in the root of a Waylay Event. Also the _metric_ identifier in the timeseries database for these values when stored."
    )
    value_type: StrictStr | None = Field(
        default=None, description="Type of the value", alias="valueType"
    )
    value_choices: List[StrictStr] | None = Field(
        default=None,
        description="Enumeration of the possible values for a metric",
        alias="valueChoices",
    )
    metric_type: ResourceMetricMetricType | None = Field(
        default=None, alias="metricType"
    )
    unit: StrictStr | None = Field(
        default=None,
        description="Physical measurement unit, preferentially SI unit, for the numerical values of this metric",
    )
    maximum: StrictFloat | StrictInt | None = Field(
        default=None, description="Expected maximum value for this metric."
    )
    minimum: StrictFloat | StrictInt | None = Field(
        default=None, description="Expected minimum value for this metric."
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )

    @model_serializer(mode="wrap")
    def serializer(
        self, handler: Callable, info: SerializationInfo
    ) -> Dict[StrictStr, Any]:
        """The default serializer of the model.

        * Excludes `None` fields that were not set at model initialization.
        """
        model_dict = handler(self, info)
        return {
            k: v
            for k, v in model_dict.items()
            if v is not None or k in self.model_fields_set
        }

    def to_dict(self) -> dict[str, Any]:
        """Convert the ResourceMetric instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the ResourceMetric instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a ResourceMetric instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: str | bytes | bytearray) -> Self:
        """Create a ResourceMetric instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)
