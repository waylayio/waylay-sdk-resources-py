"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_resource_delete_operation_action import (
    BatchResourceDeleteOperationAction,
)


class DeletedEvent(WaylayBaseModel):
    """DeletedEvent."""

    type: BatchResourceDeleteOperationAction | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
