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
    from waylay.services.resources.models.resource_creation_response import (
        ResourceCreationResponse,
    )

    ResourceCreationResponseAdapter = TypeAdapter(ResourceCreationResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_creation_response_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "number",
      "example" : 201
    },
    "uri" : {
      "type" : "string",
      "format" : "uri",
      "example" : "/resources/v1/resources/d3d823f5-f214-4de8-7c0-f2c8c4db5ee1"
    },
    "entity" : {
      "$ref" : "#/components/schemas/ResourceWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
resource_creation_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_creation_response_faker = JSF(
    resource_creation_response_model_schema, allow_none_optionals=1
)


class ResourceCreationResponseStub:
    """ResourceCreationResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_creation_response_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourceCreationResponse":
        """Create ResourceCreationResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceCreationResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceCreationResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
