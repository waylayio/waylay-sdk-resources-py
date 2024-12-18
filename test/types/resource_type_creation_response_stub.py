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
    from waylay.services.resources.models.resource_type_creation_response import (
        ResourceTypeCreationResponse,
    )

    ResourceTypeCreationResponseAdapter = TypeAdapter(ResourceTypeCreationResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_type_creation_response_model_schema = json.loads(
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
      "example" : "/resources/v1/resourcetypes/17b8b6ea-0573-4381-8088-8692f7938165"
    },
    "entity" : {
      "$ref" : "#/components/schemas/ResourceTypeWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
resource_type_creation_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_type_creation_response_faker = JSF(
    resource_type_creation_response_model_schema, allow_none_optionals=1
)


class ResourceTypeCreationResponseStub:
    """ResourceTypeCreationResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_type_creation_response_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourceTypeCreationResponse":
        """Create ResourceTypeCreationResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceTypeCreationResponseAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceTypeCreationResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
