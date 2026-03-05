"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.batch_resource_delete_operation import BatchResourceDeleteOperation
from ..models.batch_resource_patch_operation import BatchResourcePatchOperation
from ..models.batch_resource_type_delete_operation import (
    BatchResourceTypeDeleteOperation,
)

BatchResourceOperation: TypeAlias = BatchResourceDeleteOperation | BatchResourceTypeDeleteOperation | BatchResourcePatchOperation
"""BatchResourceOperation."""
