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
    from waylay.services.resources.models.task_configuration_type import (
        TaskConfigurationType,
    )

    TaskConfigurationTypeAdapter = TypeAdapter(TaskConfigurationType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

task_configuration_type_model_schema = json.loads(
    r"""{
  "title" : "TaskConfiguration_type",
  "type" : "string",
  "enum" : [ "periodic", "onetime", "scheduled", "reactive" ]
}
""",
    object_hook=with_example_provider,
)
task_configuration_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_configuration_type_faker = JSF(
    task_configuration_type_model_schema, allow_none_optionals=1
)


class TaskConfigurationTypeStub:
    """TaskConfigurationType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_configuration_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "TaskConfigurationType":
        """Create TaskConfigurationType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TaskConfigurationTypeAdapter.validate_python(cls.create_json())
