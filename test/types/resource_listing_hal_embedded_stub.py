"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.resource_listing_hal_embedded import (
        ResourceListingHALEmbedded,
    )

    ResourceListingHALEmbeddedAdapter = TypeAdapter(ResourceListingHALEmbedded)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

resource_listing_hal_embedded_model_schema = json.loads(
    r"""{
  "title" : "ResourceListingHALEmbedded",
  "required" : [ "values" ],
  "type" : "object",
  "properties" : {
    "values" : {
      "title" : "values",
      "type" : "array",
      "description" : "_Resource_ entities in HAL format",
      "items" : {
        "$ref" : "#/components/schemas/HALResourceEntity"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
resource_listing_hal_embedded_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_listing_hal_embedded_faker = JSF(
    resource_listing_hal_embedded_model_schema, allow_none_optionals=1
)


class ResourceListingHALEmbeddedStub:
    """ResourceListingHALEmbedded unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_listing_hal_embedded_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourceListingHALEmbedded":
        """Create ResourceListingHALEmbedded stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceListingHALEmbeddedAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceListingHALEmbeddedAdapter.validate_python(
            json, context={"skip_validation": True}
        )
