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
    from waylay.services.resources.models.cloud_metadata_event_data_type import (
        CloudMetadataEventDataType,
    )

    CloudMetadataEventDataTypeAdapter = TypeAdapter(CloudMetadataEventDataType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

cloud_metadata_event_data_type_model_schema = json.loads(
    r"""{
  "title" : "CloudMetadataEventData_type",
  "type" : "string",
  "enum" : [ "io.waylay.resources.v1.resourcetype.created", "io.waylay.resources.v1.resourcetype.updated", "io.waylay.resources.v1.resourcetype.deleted", "io.waylay.resources.v1.resource.created", "io.waylay.resources.v1.resource.updated", "io.waylay.resources.v1.resource.deleted", "io.waylay.resources.v1.resource.discovered" ]
}
""",
    object_hook=with_example_provider,
)
cloud_metadata_event_data_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

cloud_metadata_event_data_type_faker = JSF(
    cloud_metadata_event_data_type_model_schema, allow_none_optionals=1
)


class CloudMetadataEventDataTypeStub:
    """CloudMetadataEventDataType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return cloud_metadata_event_data_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "CloudMetadataEventDataType":
        """Create CloudMetadataEventDataType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                CloudMetadataEventDataTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return CloudMetadataEventDataTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
