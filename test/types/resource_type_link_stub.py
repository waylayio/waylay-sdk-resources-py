"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.resource_type_link import ResourceTypeLink

    ResourceTypeLinkAdapter = TypeAdapter(ResourceTypeLink)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

resource_type_link_model_schema = json.loads(
    r"""{
  "title" : "ResourceTypeLink",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALIdLink"
  }, {
    "description" : "Link to the resourceType for the resource",
    "example" : {
      "href" : "/resources/v1/resourcetypes/17b8b6ea-0573-4381-8088-8692f7938165",
      "id" : "17b8b6ea-0573-4381-8088-8692f7938165"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
resource_type_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_type_link_faker = JSF(resource_type_link_model_schema, allow_none_optionals=1)


class ResourceTypeLinkStub:
    """ResourceTypeLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_type_link_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ResourceTypeLink":
        """Create ResourceTypeLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceTypeLinkAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceTypeLinkAdapter.validate_python(
            json, context={"skip_validation": True}
        )
