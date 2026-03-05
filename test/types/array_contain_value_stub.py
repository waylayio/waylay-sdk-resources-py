"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.array_contain_value import ArrayContainValue

    ArrayContainValueAdapter = TypeAdapter(ArrayContainValue)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

array_contain_value_model_schema = json.loads(
    r"""{
  "title" : "ArrayContainValue",
  "oneOf" : [ {
    "type" : "boolean"
  }, {
    "type" : "number"
  }, {
    "type" : "string"
  } ]
}
""",
    object_hook=with_example_provider,
)
array_contain_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

array_contain_value_faker = JSF(
    array_contain_value_model_schema, allow_none_optionals=1
)


class ArrayContainValueStub:
    """ArrayContainValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return array_contain_value_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ArrayContainValue":
        """Create ArrayContainValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ArrayContainValueAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ArrayContainValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
