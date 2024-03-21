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
    from waylay.services.resources.models.changed_event import ChangedEvent

    ChangedEventAdapter = TypeAdapter(ChangedEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

changed_event_model_schema = json.loads(
    r"""{
  "properties" : {
    "type" : {
      "type" : "string",
      "enum" : [ "update" ]
    },
    "oldValues" : {
      "type" : "object",
      "description" : "old values of all attributes that have changed"
    }
  }
}
""",
    object_hook=with_example_provider,
)
changed_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

changed_event_faker = JSF(changed_event_model_schema, allow_none_optionals=1)


class ChangedEventStub:
    """ChangedEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return changed_event_faker.generate()

    @classmethod
    def create_instance(cls) -> "ChangedEvent":
        """Create ChangedEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ChangedEventAdapter.validate_python(cls.create_json())