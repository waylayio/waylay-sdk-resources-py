"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_resource_delete_operation_action import (
    BatchResourceDeleteOperationAction,
)
from ..models.cascade_delete_option import CascadeDeleteOption


class DeletedResourceEvent(WaylayBaseModel):
    """DeletedResourceEvent."""

    type: BatchResourceDeleteOperationAction | None = None
    cascade_delete: list[CascadeDeleteOption] | None = Field(
        default=None, alias="cascadeDelete"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
