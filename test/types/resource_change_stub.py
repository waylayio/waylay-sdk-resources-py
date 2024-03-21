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
    from waylay.services.resources.models.resource_change import ResourceChange

    ResourceChangeAdapter = TypeAdapter(ResourceChange)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_change_model_schema = json.loads(
    r"""{
  "required" : [ "change", "resourceId", "time", "userId" ],
  "type" : "object",
  "properties" : {
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "resourceId" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "userId" : {
      "$ref" : "#/components/schemas/UserId"
    },
    "change" : {
      "type" : "string",
      "enum" : [ "created", "updated", "deleted" ]
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
resource_change_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_change_faker = JSF(resource_change_model_schema, allow_none_optionals=1)


class ResourceChangeStub:
    """ResourceChange unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_change_faker.generate()

    @classmethod
    def create_instance(cls) -> "ResourceChange":
        """Create ResourceChange stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ResourceChangeAdapter.validate_python(cls.create_json())
