# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_id import ResourceId


class PatchResourceEntity(WaylayBaseModel):
    """PatchResourceEntity."""

    id: ResourceId | None = None
    resource_type_id: Any | None = Field(default=None, alias="resourceTypeId")
    parent_id: Any | None = Field(default=None, alias="parentId")
    name: Any | None = None
    alias: Any | None = None
    last_message_timestamp: Any | None = Field(
        default=None, alias="lastMessageTimestamp"
    )
    owner: Any | None = None
    tags: Any | None = None
    provider: Any | None = None
    provider_id: Any | None = Field(default=None, alias="providerId")
    customer: Any | None = None
    firmware: Any | None = None
    location: Any | None = None
    metrics: Any | None = None
    sensors: Any | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
