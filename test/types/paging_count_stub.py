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
    from waylay.services.resources.models.paging_count import PagingCount

    PagingCountAdapter = TypeAdapter(PagingCount)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

paging_count_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "count" : {
      "title" : "Page Count",
      "type" : "integer",
      "description" : "The number of items in this result page.",
      "example" : 10
    }
  }
}
""",
    object_hook=with_example_provider,
)
paging_count_model_schema.update({"definitions": MODEL_DEFINITIONS})

paging_count_faker = JSF(paging_count_model_schema, allow_none_optionals=1)


class PagingCountStub:
    """PagingCount unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return paging_count_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "PagingCount":
        """Create PagingCount stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(PagingCountAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PagingCountAdapter.validate_python(
            json, context={"skip_validation": True}
        )
