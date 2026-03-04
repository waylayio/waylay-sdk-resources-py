"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.resourcetype_metadata_event_resourcetype import (
        ResourcetypeMetadataEventResourcetype,
    )

    ResourcetypeMetadataEventResourcetypeAdapter = TypeAdapter(
        ResourcetypeMetadataEventResourcetype
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

resourcetype_metadata_event_resourcetype_model_schema = json.loads(
    r"""{
  "title" : "ResourcetypeMetadataEventResourcetype",
  "type" : "string",
  "enum" : [ "resourcetype" ]
}
""",
    object_hook=with_example_provider,
)
resourcetype_metadata_event_resourcetype_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

resourcetype_metadata_event_resourcetype_faker = JSF(
    resourcetype_metadata_event_resourcetype_model_schema, allow_none_optionals=1
)


class ResourcetypeMetadataEventResourcetypeStub:
    """ResourcetypeMetadataEventResourcetype unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resourcetype_metadata_event_resourcetype_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourcetypeMetadataEventResourcetype":
        """Create ResourcetypeMetadataEventResourcetype stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourcetypeMetadataEventResourcetypeAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourcetypeMetadataEventResourcetypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
