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
    from waylay.services.resources.models.batch_resource_operation_action import (
        BatchResourceOperationAction,
    )

    BatchResourceOperationActionAdapter = TypeAdapter(BatchResourceOperationAction)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_resource_operation_action_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceOperation_action",
  "type" : "string",
  "enum" : [ "delete" ]
}
""",
    object_hook=with_example_provider,
)
batch_resource_operation_action_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_resource_operation_action_faker = JSF(
    batch_resource_operation_action_model_schema, allow_none_optionals=1
)


class BatchResourceOperationActionStub:
    """BatchResourceOperationAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_resource_operation_action_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchResourceOperationAction":
        """Create BatchResourceOperationAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchResourceOperationActionAdapter.validate_python(cls.create_json())
