"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.children_resource_link import (
        ChildrenResourceLink,
    )

    ChildrenResourceLinkAdapter = TypeAdapter(ChildrenResourceLink)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

children_resource_link_model_schema = json.loads(
    r"""{
  "title" : "ChildrenResourceLink",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to fetch the children of the resource",
    "example" : {
      "href" : "/resources/v1/resources/d3d823f5-f214-4de8-7c0-f2c8c4db5ee1/children"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
children_resource_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

children_resource_link_faker = JSF(
    children_resource_link_model_schema, allow_none_optionals=1
)


class ChildrenResourceLinkStub:
    """ChildrenResourceLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return children_resource_link_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ChildrenResourceLink":
        """Create ChildrenResourceLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ChildrenResourceLinkAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ChildrenResourceLinkAdapter.validate_python(
            json, context={"skip_validation": True}
        )
