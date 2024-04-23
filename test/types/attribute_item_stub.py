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
    from waylay.services.resources.models.attribute_item import AttributeItem

    AttributeItemAdapter = TypeAdapter(AttributeItem)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

attribute_item_model_schema = json.loads(
    r"""{
  "title" : "AttributeItem",
  "required" : [ "name", "required", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "name of the attribute",
      "example" : "name"
    },
    "required" : {
      "title" : "required",
      "type" : "boolean",
      "description" : "Indicates if the attribute must be present or is optional",
      "example" : true
    },
    "type" : {
      "$ref" : "#/components/schemas/ValueConstraint"
    }
  },
  "description" : "Constraint on the presence and value of a single named _Resource_ attribute."
}
""",
    object_hook=with_example_provider,
)
attribute_item_model_schema.update({"definitions": MODEL_DEFINITIONS})

attribute_item_faker = JSF(attribute_item_model_schema, allow_none_optionals=1)


class AttributeItemStub:
    """AttributeItem unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return attribute_item_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AttributeItem":
        """Create AttributeItem stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AttributeItemAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AttributeItemAdapter.validate_python(
            json, context={"skip_validation": True}
        )
