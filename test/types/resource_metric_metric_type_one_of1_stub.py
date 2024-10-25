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
    from waylay.services.resources.models.resource_metric_metric_type_one_of1 import (
        ResourceMetricMetricTypeOneOf1,
    )

    ResourceMetricMetricTypeOneOf1Adapter = TypeAdapter(ResourceMetricMetricTypeOneOf1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_metric_metric_type_one_of_1_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "A number per a given interval (such as a statsd flushInterval)",
  "enum" : [ "count" ]
}
""",
    object_hook=with_example_provider,
)
resource_metric_metric_type_one_of_1_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

resource_metric_metric_type_one_of_1_faker = JSF(
    resource_metric_metric_type_one_of_1_model_schema, allow_none_optionals=1
)


class ResourceMetricMetricTypeOneOf1Stub:
    """ResourceMetricMetricTypeOneOf1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_metric_metric_type_one_of_1_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourceMetricMetricTypeOneOf1":
        """Create ResourceMetricMetricTypeOneOf1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceMetricMetricTypeOneOf1Adapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceMetricMetricTypeOneOf1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
