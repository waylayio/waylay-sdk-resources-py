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
    from waylay.services.resources.models.resource_type_change import ResourceTypeChange

    ResourceTypeChangeAdapter = TypeAdapter(ResourceTypeChange)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_type_change_model_schema = json.loads(
    r"""{
  "required" : [ "change", "resourceTypeId", "time", "userId" ],
  "type" : "object",
  "properties" : {
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "resourceTypeId" : {
      "$ref" : "#/components/schemas/ResourceTypeId"
    },
    "userId" : {
      "$ref" : "#/components/schemas/UserId"
    },
    "change" : {
      "$ref" : "#/components/schemas/ResourceChange_change"
    },
    "resourceType" : {
      "$ref" : "#/components/schemas/ResourceTypeWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
resource_type_change_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_type_change_faker = JSF(
    resource_type_change_model_schema, allow_none_optionals=1
)


class ResourceTypeChangeStub:
    """ResourceTypeChange unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_type_change_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ResourceTypeChange":
        """Create ResourceTypeChange stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceTypeChangeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceTypeChangeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
