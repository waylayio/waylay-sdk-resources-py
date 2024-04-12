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
    from waylay.services.resources.models.validation_failure import ValidationFailure

    ValidationFailureAdapter = TypeAdapter(ValidationFailure)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

validation_failure_model_schema = json.loads(
    r"""{
  "title" : "Validation Failure",
  "allOf" : [ {
    "$ref" : "#/components/schemas/ErrorResponse"
  }, {
    "type" : "object",
    "properties" : {
      "details" : {
        "$ref" : "#/components/schemas/SchemaValidationErrors"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
validation_failure_model_schema.update({"definitions": MODEL_DEFINITIONS})

validation_failure_faker = JSF(validation_failure_model_schema, allow_none_optionals=1)


class ValidationFailureStub:
    """ValidationFailure unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return validation_failure_faker.generate()

    @classmethod
    def create_instance(cls) -> "ValidationFailure":
        """Create ValidationFailure stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ValidationFailureAdapter.validate_python(cls.create_json())
