# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.hal_self_links_links_self import HALSelfLinksLinksSelf


class HALSelfLinksLinks(WaylayBaseModel):
    """Links to related objects."""

    var_self: HALSelfLinksLinksSelf = Field(alias="self")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
