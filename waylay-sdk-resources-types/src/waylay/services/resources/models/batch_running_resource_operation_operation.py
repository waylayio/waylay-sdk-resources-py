# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_resource_operation_action import BatchResourceOperationAction
from ..models.batch_running_resource_operation_operation_entity import (
    BatchRunningResourceOperationOperationEntity,
)


class BatchRunningResourceOperationOperation(WaylayBaseModel):
    """Queued operation summary."""

    entity: BatchRunningResourceOperationOperationEntity
    action: BatchResourceOperationAction
    description: StrictStr

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
