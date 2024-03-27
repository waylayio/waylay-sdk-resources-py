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
    from waylay.services.resources.models.string_value_constraint_type import (
        StringValueConstraintType,
    )

    StringValueConstraintTypeAdapter = TypeAdapter(StringValueConstraintType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

string_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "StringValueConstraint_type",
  "type" : "string",
  "enum" : [ "string" ]
}
""",
    object_hook=with_example_provider,
)
string_value_constraint_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

string_value_constraint_type_faker = JSF(
    string_value_constraint_type_model_schema, allow_none_optionals=1
)


class StringValueConstraintTypeStub:
    """StringValueConstraintType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return string_value_constraint_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "StringValueConstraintType":
        """Create StringValueConstraintType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return StringValueConstraintTypeAdapter.validate_python(cls.create_json())
