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
    from waylay.services.resources.models.resource_entity import ResourceEntity

    ResourceEntityAdapter = TypeAdapter(ResourceEntity)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Representation of a Waylay Resource",
  "allOf" : [ {
    "properties" : {
      "id" : {
        "$ref" : "#/components/schemas/ResourceId"
      },
      "resourceTypeId" : {
        "$ref" : "#/components/schemas/Resource_Type"
      },
      "parentId" : {
        "$ref" : "#/components/schemas/Resource_Parent"
      },
      "name" : {
        "title" : "Name",
        "type" : "string",
        "description" : "Name for the _Resource_",
        "example" : "testresource"
      },
      "alias" : {
        "type" : "string",
        "description" : "Alias for the name of the _Resource_",
        "example" : "testresource-alias"
      },
      "lastMessageTimestamp" : {
        "$ref" : "#/components/schemas/ResourceEntity_allOf_lastMessageTimestamp"
      },
      "owner" : {
        "type" : "string",
        "description" : "Owner of the _Resource_"
      },
      "tags" : {
        "$ref" : "#/components/schemas/Tags"
      }
    }
  }, {
    "$ref" : "#/components/schemas/MetadataEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
resource_entity_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_entity_faker = JSF(resource_entity_model_schema, allow_none_optionals=1)


class ResourceEntityStub:
    """ResourceEntity unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_entity_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ResourceEntity":
        """Create ResourceEntity stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceEntityAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceEntityAdapter.validate_python(
            json, context={"skip_validation": True}
        )
