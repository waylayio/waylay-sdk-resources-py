"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.batch_operation_result import BatchOperationResult
from ..models.batch_running_resource_operation import BatchRunningResourceOperation

BatchOperationStatusResponse: TypeAlias = BatchOperationResult | BatchRunningResourceOperation
"""BatchOperationStatusResponse."""
