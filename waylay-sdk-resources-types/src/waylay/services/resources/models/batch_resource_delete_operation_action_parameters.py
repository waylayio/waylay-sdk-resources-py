"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.cascade_delete_option import CascadeDeleteOption


class BatchResourceDeleteOperationActionParameters(WaylayBaseModel):
    """BatchResourceDeleteOperationActionParameters."""

    cascade: list[CascadeDeleteOption]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
