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
    from waylay.services.resources.models.resource_ref_value_constraint import (
        ResourceRefValueConstraint,
    )

    ResourceRefValueConstraintAdapter = TypeAdapter(ResourceRefValueConstraint)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_ref_value_constraint_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/ResourceRefValueConstraint_type"
    },
    "attributes" : {
      "type" : "array",
      "description" : "Additional attributes in the reference object, describing the relation.",
      "items" : {
        "$ref" : "#/components/schemas/AttributeItem"
      }
    },
    "resourceTypes" : {
      "type" : "array",
      "description" : "The possible _Resource Types_ for the referenced _Resource_.",
      "items" : {
        "$ref" : "#/components/schemas/ResourceTypeId"
      }
    },
    "exists" : {
      "type" : "boolean",
      "description" : "Flag to indicate if the referenced _Resource_ must exist",
      "default" : false
    }
  },
  "description" : "Specifies that a value is an object having a required '$ref' attribute\nthat references another _Resource_."
}
""",
    object_hook=with_example_provider,
)
resource_ref_value_constraint_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_ref_value_constraint_faker = JSF(
    resource_ref_value_constraint_model_schema, allow_none_optionals=1
)


class ResourceRefValueConstraintStub:
    """ResourceRefValueConstraint unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_ref_value_constraint_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourceRefValueConstraint":
        """Create ResourceRefValueConstraint stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceRefValueConstraintAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceRefValueConstraintAdapter.validate_python(
            json, context={"skip_validation": True}
        )
