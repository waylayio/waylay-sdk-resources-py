"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.metric_type_counter import MetricTypeCounter

    MetricTypeCounterAdapter = TypeAdapter(MetricTypeCounter)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

metric_type_counter_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Keeps increasing over time (but might wrap/reset at some point) i.e. a gauge with the added notion of “i usually want to derive this to see the rate”",
  "enum" : [ "counter" ]
}
""",
    object_hook=with_example_provider,
)
metric_type_counter_model_schema.update({"definitions": MODEL_DEFINITIONS})

metric_type_counter_faker = JSF(
    metric_type_counter_model_schema, allow_none_optionals=1
)


class MetricTypeCounterStub:
    """MetricTypeCounter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return metric_type_counter_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "MetricTypeCounter":
        """Create MetricTypeCounter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                MetricTypeCounterAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return MetricTypeCounterAdapter.validate_python(
            json, context={"skip_validation": True}
        )
