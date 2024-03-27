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
    from waylay.services.resources.models.batch_operation_status_response import (
        BatchOperationStatusResponse,
    )

    BatchOperationStatusResponseAdapter = TypeAdapter(BatchOperationStatusResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_operation_status_response_model_schema = json.loads(
    r"""{
  "title" : "BatchOperationStatusResponse",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchOperationResult"
  }, {
    "$ref" : "#/components/schemas/BatchRunningResourceOperation"
  } ]
}
""",
    object_hook=with_example_provider,
)
batch_operation_status_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_status_response_faker = JSF(
    batch_operation_status_response_model_schema, allow_none_optionals=1
)


class BatchOperationStatusResponseStub:
    """BatchOperationStatusResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_status_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchOperationStatusResponse":
        """Create BatchOperationStatusResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchOperationStatusResponseAdapter.validate_python(cls.create_json())
