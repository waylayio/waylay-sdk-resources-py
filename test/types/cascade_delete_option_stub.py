"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.cascade_delete_option import (
        CascadeDeleteOption,
    )

    CascadeDeleteOptionAdapter = TypeAdapter(CascadeDeleteOption)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

cascade_delete_option_model_schema = json.loads(
    r"""{
  "title" : "CascadeDeleteOption",
  "type" : "string",
  "enum" : [ "alarms", "measurements", "tasks" ]
}
""",
    object_hook=with_example_provider,
)
cascade_delete_option_model_schema.update({"definitions": MODEL_DEFINITIONS})

cascade_delete_option_faker = JSF(
    cascade_delete_option_model_schema, allow_none_optionals=1
)


class CascadeDeleteOptionStub:
    """CascadeDeleteOption unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return cascade_delete_option_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "CascadeDeleteOption":
        """Create CascadeDeleteOption stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                CascadeDeleteOptionAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return CascadeDeleteOptionAdapter.validate_python(
            json, context={"skip_validation": True}
        )
