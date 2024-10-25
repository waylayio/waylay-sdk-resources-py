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
    from waylay.services.resources.models.batch_resource_delete_operation_action_parameters import (
        BatchResourceDeleteOperationActionParameters,
    )

    BatchResourceDeleteOperationActionParametersAdapter = TypeAdapter(
        BatchResourceDeleteOperationActionParameters
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_resource_delete_operation_action_parameters_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceDeleteOperation_actionParameters",
  "required" : [ "cascade" ],
  "type" : "object",
  "properties" : {
    "cascade" : {
      "$ref" : "#/components/schemas/CascadeDeleteValues"
    }
  }
}
""",
    object_hook=with_example_provider,
)
batch_resource_delete_operation_action_parameters_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

batch_resource_delete_operation_action_parameters_faker = JSF(
    batch_resource_delete_operation_action_parameters_model_schema,
    allow_none_optionals=1,
)


class BatchResourceDeleteOperationActionParametersStub:
    """BatchResourceDeleteOperationActionParameters unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_resource_delete_operation_action_parameters_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchResourceDeleteOperationActionParameters":
        """Create BatchResourceDeleteOperationActionParameters stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchResourceDeleteOperationActionParametersAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchResourceDeleteOperationActionParametersAdapter.validate_python(
            json, context={"skip_validation": True}
        )
