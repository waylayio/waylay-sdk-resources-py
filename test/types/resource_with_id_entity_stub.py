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
    from waylay.services.resources.models.resource_with_id_entity import (
        ResourceWithIdEntity,
    )

    ResourceWithIdEntityAdapter = TypeAdapter(ResourceWithIdEntity)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_with_id_entity_model_schema = json.loads(
    r"""{
  "title" : "ResourceWithIdEntity",
  "allOf" : [ {
    "$ref" : "#/components/schemas/WithIdRequired"
  }, {
    "$ref" : "#/components/schemas/ResourceEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
resource_with_id_entity_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_with_id_entity_faker = JSF(
    resource_with_id_entity_model_schema, allow_none_optionals=1
)


class ResourceWithIdEntityStub:
    """ResourceWithIdEntity unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_with_id_entity_faker.generate()

    @classmethod
    def create_instance(cls) -> "ResourceWithIdEntity":
        """Create ResourceWithIdEntity stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ResourceWithIdEntityAdapter.validate_python(cls.create_json())
