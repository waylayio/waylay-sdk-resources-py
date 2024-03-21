# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from pydantic import Field
from typing_extensions import Annotated

from typing import (
    Union,
    Any,
    List,
    TYPE_CHECKING,
    Optional,
    Dict,
    Literal,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)

from pydantic import StrictStr, Field, ConfigDict

ResourceTypeId = Union[
    Annotated[str, "A Resource Type id generated by the Waylay System"],
    Annotated[str, "A _Resource Type_ id assigned by the user upon creation"],
]
"""Primary identifier of a _Resource Type_."""
