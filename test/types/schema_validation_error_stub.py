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
    from waylay.services.resources.models.schema_validation_error import (
        SchemaValidationError,
    )

    SchemaValidationErrorAdapter = TypeAdapter(SchemaValidationError)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

schema_validation_error_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "schemaPath" : {
      "type" : "string",
      "example" : "#"
    },
    "errors" : {
      "type" : "object",
      "example" : { }
    },
    "keyword" : {
      "type" : "string",
      "example" : "required"
    },
    "msgs" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "example" : "Property address missing."
      }
    },
    "value" : {
      "type" : "object",
      "example" : {
        "id" : "714bbf92-5dfc-4c42-9623-1c6e72708126",
        "resourceTypeId" : "bruno",
        "name" : "bruno",
        "customer" : "bruno_customer",
        "array" : [ {
          "coucou" : true,
          "customer" : "bravo"
        }, {
          "coucou" : false
        } ]
      }
    },
    "instancePath" : {
      "type" : "string",
      "example" : "/address"
    }
  }
}
""",
    object_hook=with_example_provider,
)
schema_validation_error_model_schema.update({"definitions": MODEL_DEFINITIONS})

schema_validation_error_faker = JSF(
    schema_validation_error_model_schema, allow_none_optionals=1
)


class SchemaValidationErrorStub:
    """SchemaValidationError unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return schema_validation_error_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "SchemaValidationError":
        """Create SchemaValidationError stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SchemaValidationErrorAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SchemaValidationErrorAdapter.validate_python(
            json, context={"skip_validation": True}
        )
