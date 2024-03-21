# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from pydantic_core import from_json
from typing import Callable, Union
from typing import cast
from typing_extensions import (
    Self,  # >=3.11
)

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field


class ChangedEvent(BaseModel):
    """ChangedEvent."""

    type: StrictStr | None = None
    old_values: Dict[str, Any] | None = Field(
        default=None,
        description="old values of all attributes that have changed",
        alias="oldValues",
    )

    @field_validator("type")
    @classmethod
    def type_validate_enum(cls, value):
        """Validate the enum."""
        if value is None:
            return value
        if value not in ("update"):
            raise ValueError("must be one of enum values ('update')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )

    @model_serializer(mode="wrap")
    def serializer(
        self, handler: Callable, info: SerializationInfo
    ) -> Dict[StrictStr, Any]:
        """The default serializer of the model.

        * Excludes `None` fields that were not set at model initialization.
        """
        model_dict = handler(self, info)
        return {
            k: v
            for k, v in model_dict.items()
            if v is not None or k in self.model_fields_set
        }

    def to_dict(self) -> dict[str, Any]:
        """Convert the ChangedEvent instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the ChangedEvent instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a ChangedEvent instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: str | bytes | bytearray) -> Self:
        """Create a ChangedEvent instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)