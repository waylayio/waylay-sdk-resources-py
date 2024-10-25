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
    from waylay.services.resources.models.pagination_links_next import (
        PaginationLinksNext,
    )

    PaginationLinksNextAdapter = TypeAdapter(PaginationLinksNext)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

pagination_links_next_model_schema = json.loads(
    r"""{
  "title" : "Pagination_links_next",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to the next page of the results (if available)",
    "example" : {
      "href" : "/resources/v1/resources?skip=400"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
pagination_links_next_model_schema.update({"definitions": MODEL_DEFINITIONS})

pagination_links_next_faker = JSF(
    pagination_links_next_model_schema, allow_none_optionals=1
)


class PaginationLinksNextStub:
    """PaginationLinksNext unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return pagination_links_next_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PaginationLinksNext":
        """Create PaginationLinksNext stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PaginationLinksNextAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PaginationLinksNextAdapter.validate_python(
            json, context={"skip_validation": True}
        )
