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
    from waylay.services.resources.models.hal_resource_entity_all_of_links_resource_type import (
        HALResourceEntityAllOfLinksResourceType,
    )

    HALResourceEntityAllOfLinksResourceTypeAdapter = TypeAdapter(
        HALResourceEntityAllOfLinksResourceType
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

hal_resource_entity_all_of__links_resource_type_model_schema = json.loads(
    r"""{
  "title" : "HALResourceEntity_allOf__links_resourceType",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALIdLink"
  }, {
    "description" : "Link to the resourceType for the resource",
    "example" : {
      "href" : "/resources/v1/resourcetypes/17b8b6ea-0573-4381-8088-8692f7938165",
      "id" : "17b8b6ea-0573-4381-8088-8692f7938165"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
hal_resource_entity_all_of__links_resource_type_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

hal_resource_entity_all_of__links_resource_type_faker = JSF(
    hal_resource_entity_all_of__links_resource_type_model_schema, allow_none_optionals=1
)


class HALResourceEntityAllOfLinksResourceTypeStub:
    """HALResourceEntityAllOfLinksResourceType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return hal_resource_entity_all_of__links_resource_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "HALResourceEntityAllOfLinksResourceType":
        """Create HALResourceEntityAllOfLinksResourceType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return HALResourceEntityAllOfLinksResourceTypeAdapter.validate_python(
            cls.create_json()
        )
