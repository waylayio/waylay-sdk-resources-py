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
    from waylay.services.resources.models.boolean_value_constraint import (
        BooleanValueConstraint,
    )

    BooleanValueConstraintAdapter = TypeAdapter(BooleanValueConstraint)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

boolean_value_constraint_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/BooleanValueConstraint_type"
    }
  },
  "description" : "Specifies that the value must be a boolean"
}
""",
    object_hook=with_example_provider,
)
boolean_value_constraint_model_schema.update({"definitions": MODEL_DEFINITIONS})

boolean_value_constraint_faker = JSF(
    boolean_value_constraint_model_schema, allow_none_optionals=1
)


class BooleanValueConstraintStub:
    """BooleanValueConstraint unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return boolean_value_constraint_faker.generate()

    @classmethod
    def create_instance(cls) -> "BooleanValueConstraint":
        """Create BooleanValueConstraint stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BooleanValueConstraintAdapter.validate_python(cls.create_json())
