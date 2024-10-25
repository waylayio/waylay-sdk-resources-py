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
    from waylay.services.resources.models.batch_operation_enqueued import (
        BatchOperationEnqueued,
    )

    BatchOperationEnqueuedAdapter = TypeAdapter(BatchOperationEnqueued)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_operation_enqueued_model_schema = json.loads(
    r"""{
  "title" : "Batch operation enqueued",
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 202
    },
    "uri" : {
      "type" : "string",
      "description" : "URI where the batch operation status can be followed",
      "format" : "uri",
      "example" : "/resources/v1/batch/afcea5a1-81df-44f6-bd34-e0b602a2cf3d"
    },
    "entity" : {
      "$ref" : "#/components/schemas/BatchRunningResourceOperation"
    }
  }
}
""",
    object_hook=with_example_provider,
)
batch_operation_enqueued_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_enqueued_faker = JSF(
    batch_operation_enqueued_model_schema, allow_none_optionals=1
)


class BatchOperationEnqueuedStub:
    """BatchOperationEnqueued unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_enqueued_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchOperationEnqueued":
        """Create BatchOperationEnqueued stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchOperationEnqueuedAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchOperationEnqueuedAdapter.validate_python(
            json, context={"skip_validation": True}
        )
