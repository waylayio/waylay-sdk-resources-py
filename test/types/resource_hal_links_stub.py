"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.resource_hal_links import ResourceHALLinks

    ResourceHALLinksAdapter = TypeAdapter(ResourceHALLinks)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

resource_hal_links_model_schema = json.loads(
    r"""{
  "title" : "ResourceHALLinks",
  "type" : "object",
  "properties" : {
    "parent" : {
      "$ref" : "#/components/schemas/ParentResourceLink"
    },
    "children" : {
      "$ref" : "#/components/schemas/ChildrenResourceLink"
    },
    "resourceType" : {
      "$ref" : "#/components/schemas/ResourceTypeLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
resource_hal_links_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_hal_links_faker = JSF(resource_hal_links_model_schema, allow_none_optionals=1)


class ResourceHALLinksStub:
    """ResourceHALLinks unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_hal_links_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ResourceHALLinks":
        """Create ResourceHALLinks stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceHALLinksAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceHALLinksAdapter.validate_python(
            json, context={"skip_validation": True}
        )
