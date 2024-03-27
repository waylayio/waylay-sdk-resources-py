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
    from waylay.services.resources.models.resource_type_entity import ResourceTypeEntity

    ResourceTypeEntityAdapter = TypeAdapter(ResourceTypeEntity)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_type_entity_model_schema = json.loads(
    r"""{
  "description" : "Representation of a _Resource Type_",
  "allOf" : [ {
    "properties" : {
      "id" : {
        "$ref" : "#/components/schemas/ResourceTypeId"
      },
      "name" : {
        "title" : "Name",
        "type" : "string",
        "description" : "Name for the _Resource Type_",
        "example" : "MyDeviceType"
      },
      "templates" : {
        "title" : "Managed Task Templates",
        "type" : "array",
        "description" : "Templates for task that is automatically created whenever a new \n_Resource_ of this _Resource Type_ is created.",
        "items" : {
          "$ref" : "#/components/schemas/TaskConfiguration"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/MetadataEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
resource_type_entity_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_type_entity_faker = JSF(
    resource_type_entity_model_schema, allow_none_optionals=1
)


class ResourceTypeEntityStub:
    """ResourceTypeEntity unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_type_entity_faker.generate()

    @classmethod
    def create_instance(cls) -> "ResourceTypeEntity":
        """Create ResourceTypeEntity stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ResourceTypeEntityAdapter.validate_python(cls.create_json())
