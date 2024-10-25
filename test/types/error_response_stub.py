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
    from waylay.services.resources.models.error_response import ErrorResponse

    ErrorResponseAdapter = TypeAdapter(ErrorResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

error_response_model_schema = json.loads(
    r"""{
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 400
    },
    "error" : {
      "type" : "string",
      "example" : "/address <- Property address missing."
    },
    "code" : {
      "type" : "string",
      "description" : "Optional error code"
    }
  }
}
""",
    object_hook=with_example_provider,
)
error_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

error_response_faker = JSF(error_response_model_schema, allow_none_optionals=1)


class ErrorResponseStub:
    """ErrorResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return error_response_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ErrorResponse":
        """Create ErrorResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ErrorResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ErrorResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
