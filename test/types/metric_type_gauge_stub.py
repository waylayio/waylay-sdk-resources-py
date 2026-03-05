"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.metric_type_gauge import MetricTypeGauge

    MetricTypeGaugeAdapter = TypeAdapter(MetricTypeGauge)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

metric_type_gauge_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Values at each point in time",
  "enum" : [ "gauge" ]
}
""",
    object_hook=with_example_provider,
)
metric_type_gauge_model_schema.update({"definitions": MODEL_DEFINITIONS})

metric_type_gauge_faker = JSF(metric_type_gauge_model_schema, allow_none_optionals=1)


class MetricTypeGaugeStub:
    """MetricTypeGauge unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return metric_type_gauge_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "MetricTypeGauge":
        """Create MetricTypeGauge stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                MetricTypeGaugeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return MetricTypeGaugeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
