# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class FailureOperationResultValue(WaylayBaseModel):
    """The keys will be resource ids or resource type ids.."""

    status_code: StrictInt = Field(
        description="The statusCode of the operation", alias="statusCode"
    )
    error: StrictStr = Field(description="Error description of what went wrong.")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
