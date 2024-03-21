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

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from ..models.metadata_entity_location import MetadataEntityLocation
from ..models.resource_metric import ResourceMetric
from ..models.resource_sensor import ResourceSensor


class MetadataEntity(BaseModel):
    """Common attributes for _Resource_ or _Resource Type_."""

    provider: StrictStr | None = None
    provider_id: StrictStr | None = Field(default=None, alias="providerId")
    customer: StrictStr | None = Field(default=None, description="Customer name")
    firmware: StrictStr | None = None
    location: MetadataEntityLocation | None = None
    metrics: List[ResourceMetric] | None = Field(
        default=None,
        description="A documentation of possible measurements that are to be expected on _Waylay Events_ associated with this _Resource_.",
    )
    sensors: List[ResourceSensor] | None = Field(
        default=None,
        description="Set of sensors that are applicable for a given _Resource_. Please note that there is no explicit action taken by the Waylay platform on this meta key. The idea behind this abstraction is to assist integrations where an architect of the digital twin can specify which sensors from waylay library are applicable for a given _Resource_ (or _Resource Type_).",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
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
        """Convert the MetadataEntity instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the MetadataEntity instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a MetadataEntity instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: str | bytes | bytearray) -> Self:
        """Create a MetadataEntity instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)