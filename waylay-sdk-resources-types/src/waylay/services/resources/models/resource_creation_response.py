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
    StrictFloat,
    StrictInt,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_with_id_entity import ResourceWithIdEntity


class ResourceCreationResponse(WaylayBaseModel):
    """ResourceCreationResponse."""

    status_code: StrictFloat | StrictInt = Field(alias="statusCode")
    uri: StrictStr
    entity: ResourceWithIdEntity

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
