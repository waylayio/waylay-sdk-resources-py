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
    from waylay.services.resources.models.object_value_constraint import (
        ObjectValueConstraint,
    )

    ObjectValueConstraintAdapter = TypeAdapter(ObjectValueConstraint)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

object_value_constraint_model_schema = json.loads(
    r"""{
  "required" : [ "attributes", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/ObjectValueConstraint_type"
    },
    "attributes" : {
      "type" : "array",
      "description" : "Attributes descriptions",
      "items" : {
        "$ref" : "#/components/schemas/AttributeItem"
      }
    }
  },
  "description" : "Specifies that a value must be an object and which attributes it needs to have"
}
""",
    object_hook=with_example_provider,
)
object_value_constraint_model_schema.update({"definitions": MODEL_DEFINITIONS})

object_value_constraint_faker = JSF(
    object_value_constraint_model_schema, allow_none_optionals=1
)


class ObjectValueConstraintStub:
    """ObjectValueConstraint unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return object_value_constraint_faker.generate()

    @classmethod
    def create_instance(cls) -> "ObjectValueConstraint":
        """Create ObjectValueConstraint stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ObjectValueConstraintAdapter.validate_python(cls.create_json())
