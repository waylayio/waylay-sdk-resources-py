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
    from waylay.services.resources.models.hal_resource_entity_all_of_links_children import (
        HALResourceEntityAllOfLinksChildren,
    )

    HALResourceEntityAllOfLinksChildrenAdapter = TypeAdapter(
        HALResourceEntityAllOfLinksChildren
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

hal_resource_entity_all_of__links_children_model_schema = json.loads(
    r"""{
  "title" : "HALResourceEntity_allOf__links_children",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to fetch the children of the resource",
    "example" : {
      "href" : "/resources/v1/resources/d3d823f5-f214-4de8-7c0-f2c8c4db5ee1/children"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
hal_resource_entity_all_of__links_children_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

hal_resource_entity_all_of__links_children_faker = JSF(
    hal_resource_entity_all_of__links_children_model_schema, allow_none_optionals=1
)


class HALResourceEntityAllOfLinksChildrenStub:
    """HALResourceEntityAllOfLinksChildren unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return hal_resource_entity_all_of__links_children_faker.generate()

    @classmethod
    def create_instance(cls) -> "HALResourceEntityAllOfLinksChildren":
        """Create HALResourceEntityAllOfLinksChildren stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return HALResourceEntityAllOfLinksChildrenAdapter.validate_python(
            cls.create_json()
        )