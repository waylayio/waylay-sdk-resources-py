# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

import re
from typing import List

from pydantic import (
    ConfigDict,
    Field,
    field_validator,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.constraint_error import ConstraintError
from ..models.constraint_status_status import ConstraintStatusStatus


class ConstraintStatus(WaylayBaseModel):
    """Reference to a _Resource Constraint_s and its validation status.."""

    status: ConstraintStatusStatus
    constraint_id: Annotated[str, Field(strict=True)] = Field(
        description="A unique _Resource Constraint_ id generated by the Waylay System",
        alias="constraintId",
    )
    errors: List[ConstraintError] | None = None

    @field_validator("constraint_id")
    @classmethod
    def constraint_id_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", value
        ):
            raise ValueError(
                r"must validate the regular expression /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/"
            )
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
