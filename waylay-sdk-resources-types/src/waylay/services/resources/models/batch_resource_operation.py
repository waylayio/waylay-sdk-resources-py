# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

from ..models.batch_resource_delete_operation import BatchResourceDeleteOperation
from ..models.batch_resource_type_delete_operation import (
    BatchResourceTypeDeleteOperation,
)

BatchResourceOperation = Union[
    Annotated[BatchResourceDeleteOperation, ""],
    Annotated[BatchResourceTypeDeleteOperation, ""],
]
"""BatchResourceOperation."""
