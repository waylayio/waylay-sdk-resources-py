# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict

from pydantic import (
    ConfigDict,
    Field,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.changed_event_type import ChangedEventType


class ChangedEvent(WaylayBaseModel):
    """ChangedEvent."""

    type: ChangedEventType | None = None
    old_values: Dict[str, Any] | None = Field(
        default=None,
        description="old values of all attributes that have changed",
        alias="oldValues",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
