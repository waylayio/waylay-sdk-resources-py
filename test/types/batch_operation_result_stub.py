# coding: utf-8
"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.batch_operation_result import (
        BatchOperationResult,
    )

    BatchOperationResultAdapter = TypeAdapter(BatchOperationResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_operation_result_model_schema = json.loads(
    r"""{
  "example" : {
    "id" : "afcea5a1-81df-44f6-bd34-e0b602a2cf3d",
    "user" : "4b6c0c68-7c5f-4ad8-a138-e5d9d96242ed",
    "operation" : {
      "entity" : "resource",
      "action" : "delete",
      "description" : "deleting 3 resources"
    },
    "queueTime" : "2020-04-27T09:54:44.051Z",
    "finishedTime" : "2020-04-27T09:54:44.129Z",
    "results" : {
      "success" : {
        "d3d823f5-f214-4de8-7c0-f2c8c4db5ee1" : {
          "statusCode" : 204
        }
      },
      "failure" : {
        "82af367c-dffc-48d6-aea2-bfc699047174" : {
          "statusCode" : "404,",
          "error" : "No resource with id 82af367c-dffc-48d6-aea2-bfc699047174"
        },
        "e64de65c-e3ef-482d-9eb7-32ca17d1e147" : {
          "statusCode" : "400,",
          "error" : "Resource is still parent of or referenced by 2 resource(s)"
        }
      }
    }
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchRunningResourceOperation"
  }, {
    "$ref" : "#/components/schemas/OperationResultObject"
  } ]
}
""",
    object_hook=with_example_provider,
)
batch_operation_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_result_faker = JSF(
    batch_operation_result_model_schema, allow_none_optionals=1
)


class BatchOperationResultStub:
    """BatchOperationResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_result_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchOperationResult":
        """Create BatchOperationResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchOperationResultAdapter.validate_python(cls.create_json())