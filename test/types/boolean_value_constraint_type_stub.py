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
    from waylay.services.resources.models.boolean_value_constraint_type import (
        BooleanValueConstraintType,
    )

    BooleanValueConstraintTypeAdapter = TypeAdapter(BooleanValueConstraintType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

boolean_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "BooleanValueConstraint_type",
  "type" : "string",
  "enum" : [ "boolean" ]
}
""",
    object_hook=with_example_provider,
)
boolean_value_constraint_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

boolean_value_constraint_type_faker = JSF(
    boolean_value_constraint_type_model_schema, allow_none_optionals=1
)


class BooleanValueConstraintTypeStub:
    """BooleanValueConstraintType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return boolean_value_constraint_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BooleanValueConstraintType":
        """Create BooleanValueConstraintType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BooleanValueConstraintTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BooleanValueConstraintTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
