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

from ..models.batch_resource_patch_operation_action import (
    BatchResourcePatchOperationAction,
)
from ..models.batch_resource_patch_operation_action_parameters import (
    BatchResourcePatchOperationActionParameters,
)
from ..models.batch_resource_patch_operation_entity import (
    BatchResourcePatchOperationEntity,
)
from ..models.batch_resource_patch_operation_query import (
    BatchResourcePatchOperationQuery,
)


class BatchResourcePatchOperation(WaylayBaseModel):
    """BatchResourcePatchOperation."""

    entity: BatchResourcePatchOperationEntity
    action: BatchResourcePatchOperationAction
    query: BatchResourcePatchOperationQuery
    action_parameters: BatchResourcePatchOperationActionParameters | None = Field(
        default=None, alias="actionParameters"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
