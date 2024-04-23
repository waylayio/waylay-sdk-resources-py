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
    from waylay.services.resources.models.halid_link import HALIdLink

    HALIdLinkAdapter = TypeAdapter(HALIdLink)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

halid_link_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "required" : [ "id" ],
    "type" : "object",
    "properties" : {
      "id" : {
        "type" : "string",
        "description" : "Unique identifier of the linked item"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
halid_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

halid_link_faker = JSF(halid_link_model_schema, allow_none_optionals=1)


class HALIdLinkStub:
    """HALIdLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return halid_link_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "HALIdLink":
        """Create HALIdLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(HALIdLinkAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return HALIdLinkAdapter.validate_python(json, context={"skip_validation": True})
