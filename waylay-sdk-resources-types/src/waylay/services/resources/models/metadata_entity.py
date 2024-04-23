# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.metadata_entity_location import MetadataEntityLocation
from ..models.resource_metric import ResourceMetric
from ..models.resource_sensor import ResourceSensor


class MetadataEntity(WaylayBaseModel):
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
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
