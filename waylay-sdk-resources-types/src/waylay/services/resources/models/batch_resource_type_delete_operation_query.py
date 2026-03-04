"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_type_id import ResourceTypeId


class BatchResourceTypeDeleteOperationQuery(WaylayBaseModel):
    """BatchResourceTypeDeleteOperationQuery."""

    ids: Annotated[list[ResourceTypeId], Field(min_length=1)]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
