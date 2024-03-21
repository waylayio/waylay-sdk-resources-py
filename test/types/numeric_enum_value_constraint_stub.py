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
    from waylay.services.resources.models.numeric_enum_value_constraint import (
        NumericEnumValueConstraint,
    )

    NumericEnumValueConstraintAdapter = TypeAdapter(NumericEnumValueConstraint)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

numeric_enum_value_constraint_model_schema = json.loads(
    r"""{
  "title" : "NumericEnumValueConstraint",
  "required" : [ "enumType", "items", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "type",
      "type" : "string",
      "enum" : [ "enum" ]
    },
    "enumType" : {
      "title" : "enumType",
      "type" : "string",
      "enum" : [ "numeric" ]
    },
    "items" : {
      "title" : "items",
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "type" : "number"
      }
    }
  },
  "description" : "Specifies that a value must be one of the given numbers."
}
""",
    object_hook=with_example_provider,
)
numeric_enum_value_constraint_model_schema.update({"definitions": MODEL_DEFINITIONS})

numeric_enum_value_constraint_faker = JSF(
    numeric_enum_value_constraint_model_schema, allow_none_optionals=1
)


class NumericEnumValueConstraintStub:
    """NumericEnumValueConstraint unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return numeric_enum_value_constraint_faker.generate()

    @classmethod
    def create_instance(cls) -> "NumericEnumValueConstraint":
        """Create NumericEnumValueConstraint stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return NumericEnumValueConstraintAdapter.validate_python(cls.create_json())
