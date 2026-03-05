"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.resource_metadata_event import ResourceMetadataEvent
from ..models.resourcetype_metadata_event import ResourcetypeMetadataEvent

MetadataEvent: TypeAlias = ResourceMetadataEvent | ResourcetypeMetadataEvent
"""MetadataEvent."""
