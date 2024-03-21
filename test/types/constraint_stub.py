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
    from waylay.services.resources.models.constraint import Constraint

    ConstraintAdapter = TypeAdapter(Constraint)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

constraint_model_schema = json.loads(
    r"""{
  "title" : "Constraint",
  "required" : [ "attributes", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "minLength" : 1,
      "type" : "string",
      "description" : "Name for the _Resource Constraint_",
      "example" : "Mandatory name"
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "A description for the _Resource Constraint_",
      "example" : "Makes the name attribute mandatory"
    },
    "attributes" : {
      "title" : "attributes",
      "type" : "array",
      "description" : "List of attribute descriptions",
      "items" : {
        "$ref" : "#/components/schemas/AttributeItem"
      }
    }
  },
  "description" : "Constraint on the attributes of a Resource"
}
""",
    object_hook=with_example_provider,
)
constraint_model_schema.update({"definitions": MODEL_DEFINITIONS})

constraint_faker = JSF(constraint_model_schema, allow_none_optionals=1)


class ConstraintStub:
    """Constraint unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return constraint_faker.generate()

    @classmethod
    def create_instance(cls) -> "Constraint":
        """Create Constraint stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ConstraintAdapter.validate_python(cls.create_json())
