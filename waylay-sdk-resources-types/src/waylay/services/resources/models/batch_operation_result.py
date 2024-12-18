# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

import re
from datetime import datetime

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
    field_validator,
)
from typing_extensions import (
    Annotated,  # >=3.11
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_running_resource_operation_operation import (
    BatchRunningResourceOperationOperation,
)
from ..models.operation_result_object_results import OperationResultObjectResults


class BatchOperationResult(WaylayBaseModel):
    """BatchOperationResult."""

    id: StrictStr
    user: Annotated[str, Field(strict=True)] = Field(
        description="User subject id in the Waylay Accounts database"
    )
    queue_time: datetime = Field(alias="queueTime")
    operation: BatchRunningResourceOperationOperation
    finished_time: datetime = Field(alias="finishedTime")
    results: OperationResultObjectResults

    @field_validator("user")
    @classmethod
    def user_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", value
        ):
            raise ValueError(
                r"must validate the regular expression /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/"
            )
        return value

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
