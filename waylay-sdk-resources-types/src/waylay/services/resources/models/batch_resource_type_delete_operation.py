# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

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
from ..models.batch_resource_type_delete_operation_entity import (
    BatchResourceTypeDeleteOperationEntity,
)
from ..models.batch_resource_type_delete_operation_query import (
    BatchResourceTypeDeleteOperationQuery,
)


class BatchResourceTypeDeleteOperation(WaylayBaseModel):
    """BatchResourceTypeDeleteOperation."""

    entity: BatchResourceTypeDeleteOperationEntity
    action: BatchResourceDeleteOperationAction
    query: BatchResourceTypeDeleteOperationQuery

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
