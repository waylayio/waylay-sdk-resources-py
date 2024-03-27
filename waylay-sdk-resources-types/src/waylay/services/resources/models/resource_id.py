# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

ResourceId = Union[
    Annotated[str, "A _Resource_ id generated by the Waylay System"],
    Annotated[str, "A _Resource_ id assigned by the user upon creation"],
]
"""Primary identifier of a _Resource_."""
