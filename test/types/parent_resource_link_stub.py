"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.parent_resource_link import ParentResourceLink

    ParentResourceLinkAdapter = TypeAdapter(ParentResourceLink)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

parent_resource_link_model_schema = json.loads(
    r"""{
  "title" : "ParentResourceLink",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALIdLink"
  }, {
    "description" : "Link to the parent resource",
    "example" : {
      "href" : "/resources/v1/resources/658c4fb3-d25a-4bfa-aeca-3fb0009e9a8a",
      "id" : "658c4fb3-d25a-4bfa-aeca-3fb0009e9a8a"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
parent_resource_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

parent_resource_link_faker = JSF(
    parent_resource_link_model_schema, allow_none_optionals=1
)


class ParentResourceLinkStub:
    """ParentResourceLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return parent_resource_link_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ParentResourceLink":
        """Create ParentResourceLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ParentResourceLinkAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ParentResourceLinkAdapter.validate_python(
            json, context={"skip_validation": True}
        )
