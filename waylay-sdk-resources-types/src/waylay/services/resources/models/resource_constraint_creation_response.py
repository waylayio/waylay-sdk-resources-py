"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

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

from ..models.resource_constraint_with_id_entity import ResourceConstraintWithIdEntity


class ResourceConstraintCreationResponse(WaylayBaseModel):
    """ResourceConstraintCreationResponse."""

    status_code: StrictInt = Field(alias="statusCode")
    uri: StrictStr
    entity: ResourceConstraintWithIdEntity

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
