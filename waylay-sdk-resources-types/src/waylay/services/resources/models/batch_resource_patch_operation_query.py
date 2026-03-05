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

from ..models.patch_resource_entity import PatchResourceEntity


class BatchResourcePatchOperationQuery(WaylayBaseModel):
    """BatchResourcePatchOperationQuery."""

    resources: Annotated[list[PatchResourceEntity], Field(min_length=1)] = Field(
        description="Array of resource objects to patch or insert"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
