# coding: utf-8
"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.constraint_status import ConstraintStatus

    ConstraintStatusAdapter = TypeAdapter(ConstraintStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

constraint_status_model_schema = json.loads(
    r"""{
  "title" : "ConstraintStatus",
  "required" : [ "constraintId", "status" ],
  "type" : "object",
  "properties" : {
    "status" : {
      "title" : "status",
      "type" : "string",
      "example" : "failed",
      "enum" : [ "applying", "ineffect", "failed" ]
    },
    "constraintId" : {
      "$ref" : "#/components/schemas/ResourceConstraintId"
    },
    "errors" : {
      "title" : "errors",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ConstraintError"
      }
    }
  },
  "description" : "Reference to a _Resource Constraint_s and its validation status."
}
""",
    object_hook=with_example_provider,
)
constraint_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

constraint_status_faker = JSF(constraint_status_model_schema, allow_none_optionals=1)


class ConstraintStatusStub:
    """ConstraintStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return constraint_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "ConstraintStatus":
        """Create ConstraintStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ConstraintStatusAdapter.validate_python(cls.create_json())