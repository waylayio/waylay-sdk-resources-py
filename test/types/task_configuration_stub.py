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
    from waylay.services.resources.models.task_configuration import TaskConfiguration

    TaskConfigurationAdapter = TypeAdapter(TaskConfiguration)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

task_configuration_model_schema = json.loads(
    r"""{
  "title" : "TaskConfiguration",
  "required" : [ "templateName" ],
  "type" : "object",
  "properties" : {
    "templateName" : {
      "title" : "Template Name",
      "type" : "string"
    },
    "type" : {
      "title" : "Task Type",
      "type" : "string",
      "enum" : [ "periodic", "onetime", "scheduled", "reactive" ]
    }
  },
  "additionalProperties" : {
    "description" : "Additional task creation attributes"
  },
  "description" : "Specification of a template and task creation attributes\nfor the task that gets instantiate when a _Resource_ created.",
  "example" : {
    "templateName" : "CheckThreshold",
    "type" : "reactive",
    "resetObservations" : false,
    "parallel" : true
  }
}
""",
    object_hook=with_example_provider,
)
task_configuration_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_configuration_faker = JSF(task_configuration_model_schema, allow_none_optionals=1)


class TaskConfigurationStub:
    """TaskConfiguration unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_configuration_faker.generate()

    @classmethod
    def create_instance(cls) -> "TaskConfiguration":
        """Create TaskConfiguration stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TaskConfigurationAdapter.validate_python(cls.create_json())
