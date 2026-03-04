"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.cloud_metadata_event import CloudMetadataEvent
from ..models.metadata_event import MetadataEvent

NdJsonResponseStream: TypeAlias = MetadataEvent | CloudMetadataEvent
"""NdJsonResponseStream."""
