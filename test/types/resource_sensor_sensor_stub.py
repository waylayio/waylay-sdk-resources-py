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
    from waylay.services.resources.models.resource_sensor_sensor import (
        ResourceSensorSensor,
    )

    ResourceSensorSensorAdapter = TypeAdapter(ResourceSensorSensor)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_sensor_sensor_model_schema = json.loads(
    r"""{
  "title" : "ResourceSensor_sensor",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The identifying name of the _Waylay Sensor_"
    },
    "version" : {
      "title" : "version",
      "pattern" : "\\d+\\.\\d+\\.\\d+",
      "type" : "string",
      "description" : "The sensor version"
    },
    "properties" : {
      "title" : "properties",
      "type" : "object",
      "description" : "Default sensor property configuration."
    }
  }
}
""",
    object_hook=with_example_provider,
)
resource_sensor_sensor_model_schema.update({"definitions": MODEL_DEFINITIONS})

resource_sensor_sensor_faker = JSF(
    resource_sensor_sensor_model_schema, allow_none_optionals=1
)


class ResourceSensorSensorStub:
    """ResourceSensorSensor unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_sensor_sensor_faker.generate()

    @classmethod
    def create_instance(cls) -> "ResourceSensorSensor":
        """Create ResourceSensorSensor stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ResourceSensorSensorAdapter.validate_python(cls.create_json())
