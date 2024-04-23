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
    from waylay.services.resources.models.failure_operation_result_value import (
        FailureOperationResultValue,
    )

    FailureOperationResultValueAdapter = TypeAdapter(FailureOperationResultValue)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

failure_operation_result_value_model_schema = json.loads(
    r"""{
  "title" : "FailureOperationResult_value",
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "statusCode",
      "type" : "integer",
      "description" : "The statusCode of the operation"
    },
    "error" : {
      "title" : "error",
      "type" : "string",
      "description" : "Error description of what went wrong."
    }
  },
  "description" : "The keys will be resource ids or resource type ids."
}
""",
    object_hook=with_example_provider,
)
failure_operation_result_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

failure_operation_result_value_faker = JSF(
    failure_operation_result_value_model_schema, allow_none_optionals=1
)


class FailureOperationResultValueStub:
    """FailureOperationResultValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return failure_operation_result_value_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "FailureOperationResultValue":
        """Create FailureOperationResultValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                FailureOperationResultValueAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return FailureOperationResultValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
