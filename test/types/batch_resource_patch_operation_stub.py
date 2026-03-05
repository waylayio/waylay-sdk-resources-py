"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.batch_resource_patch_operation import (
        BatchResourcePatchOperation,
    )

    BatchResourcePatchOperationAdapter = TypeAdapter(BatchResourcePatchOperation)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_resource_patch_operation_model_schema = json.loads(
    r"""{
  "title" : "BatchResourcePatchOperation",
  "required" : [ "action", "entity", "query" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchResourcePatchOperation_entity"
    },
    "action" : {
      "$ref" : "#/components/schemas/BatchResourcePatchOperation_action"
    },
    "query" : {
      "$ref" : "#/components/schemas/BatchResourcePatchOperationQuery"
    },
    "actionParameters" : {
      "$ref" : "#/components/schemas/BatchResourcePatchOperationActionParameters"
    }
  }
}
""",
    object_hook=with_example_provider,
)
batch_resource_patch_operation_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_resource_patch_operation_faker = JSF(
    batch_resource_patch_operation_model_schema, allow_none_optionals=1
)


class BatchResourcePatchOperationStub:
    """BatchResourcePatchOperation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_resource_patch_operation_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchResourcePatchOperation":
        """Create BatchResourcePatchOperation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchResourcePatchOperationAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchResourcePatchOperationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
