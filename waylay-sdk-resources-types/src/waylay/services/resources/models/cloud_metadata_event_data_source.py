# coding: utf-8
"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class CloudMetadataEventDataSource(str, Enum):
    """CloudMetadataEventDataSource."""

    SLASH_RESOURCES_SLASH_V1_SLASH_RESOURCES = "/resources/v1/resources"
    SLASH_RESOURCES_SLASH_V1_SLASH_RESOURCETYPES = "/resources/v1/resourcetypes"

    def __str__(self) -> str:
        return str(self.value)
