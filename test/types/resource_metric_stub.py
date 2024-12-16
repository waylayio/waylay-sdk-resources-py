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
    from waylay.services.resources.models.resource_metric import ResourceMetric

    ResourceMetricAdapter = TypeAdapter(ResourceMetric)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_metric_model_schema = json.loads(
    r"""{
  "title" : "ResourceMetric",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "Metric name",
      "type" : "string",
      "description" : "The key under which values of this metric are present in the root of a Waylay Event.\nAlso the _metric_ identifier in the timeseries database for these values when stored.",
      "example" : "temperature"
    },
    "valueType" : {
      "title" : "Value type",
      "type" : "string",
      "description" : "Type of the value",
      "example" : "integer"
    },
    "valueChoices" : {
      "title" : "Value Choice",
      "type" : "array",
      "description" : "Enumeration of the possible values for a metric",
      "items" : {
        "type" : "string"
      }
    },
    "metricType" : {
      "$ref" : "#/components/schemas/ResourceMetric_metricType"
    },
    "unit" : {
      "title" : "unit",
      "type" : "string",
      "description" : "Physical measurement unit, preferentially SI unit, for the numerical values of this metric",
      "example" : "m^3/s"
    },
    "maximum" : {
      "title" : "maximum",
      "type" : "number",
      "description" : "Expected maximum value for this metric.",
      "example" : 200.01
    },
    "minimum" : {
      "title" : "minimum",
      "type" : "number",
      "description" : "Expected minimum value for this metric.",
      "example" : -0.0000010
    }
  },
  "description" : "Describes a value that is expected to be present in the events sent to Waylay on behalf of this _Resource (Type)_.\nBy default, such values will end up in the time series database, where each time series is identified by the\n_resource id_ and the _metric name_.\n\n> Note: The Waylay System does not enforce any of the statements made in a _Resource Metric_ when\n> processing or retrieving data. As long as a user does not explicitly use this metadata to configure\n> behaviour, a _Resource Metric_ is purely a documentation entity."
}
""",
    object_hook=with_example_provider,
)
resource_metric_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_metric_faker = JSF(resource_metric_model_schema, allow_none_optionals=1)


class ResourceMetricStub:
    """ResourceMetric unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_metric_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ResourceMetric":
        """Create ResourceMetric stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceMetricAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceMetricAdapter.validate_python(
            json, context={"skip_validation": True}
        )
