"""Waylay Resources models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.task_configuration_type import TaskConfigurationType


class TaskConfiguration(WaylayBaseModel):
    """Specification of a template and task creation attributes for the task that gets instantiate when a _Resource_ created.."""

    template_name: StrictStr = Field(alias="templateName")
    type: TaskConfigurationType | None = None
    diagnostic_template: StrictBool | None = Field(
        default=False,
        description="flag indicating if template is diagnostic. No managed task will be created if that flag set to true.",
        alias="diagnosticTemplate",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
