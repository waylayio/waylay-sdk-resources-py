# coding: utf-8
"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.string_value_constraint import (
        StringValueConstraint,
    )

    StringValueConstraintAdapter = TypeAdapter(StringValueConstraint)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

string_value_constraint_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/StringValueConstraint_type"
    },
    "minLength" : {
      "minimum" : 0,
      "type" : "integer",
      "description" : "Minimum length a value must have",
      "example" : 1
    },
    "maxLength" : {
      "minimum" : 0,
      "type" : "integer",
      "description" : "Maximum length a value can have",
      "example" : 255
    }
  },
  "description" : "Specifies that a value must be a string."
}
""",
    object_hook=with_example_provider,
)
string_value_constraint_model_schema.update({"definitions": MODEL_DEFINITIONS})

string_value_constraint_faker = JSF(
    string_value_constraint_model_schema, allow_none_optionals=1
)


class StringValueConstraintStub:
    """StringValueConstraint unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return string_value_constraint_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "StringValueConstraint":
        """Create StringValueConstraint stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                StringValueConstraintAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return StringValueConstraintAdapter.validate_python(
            json, context={"skip_validation": True}
        )
