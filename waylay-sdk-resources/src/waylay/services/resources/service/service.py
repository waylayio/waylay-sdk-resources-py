"""Resources Service."""

from waylay.sdk import ApiClient, WaylayService

from ..api.batch_operations_api import BatchOperationsApi
from ..api.metadata_events_api import MetadataEventsApi
from ..api.resource_api import ResourceApi
from ..api.resource_constraint_api import ResourceConstraintApi
from ..api.resource_type_api import ResourceTypeApi
from ..api.version_api import VersionApi


class ResourcesService(WaylayService):
    """Resources Service Class."""

    name = "resources"
    title = "Resources Service"

    batch_operations: BatchOperationsApi
    metadata_events: MetadataEventsApi
    resource: ResourceApi
    resource_constraint: ResourceConstraintApi
    resource_type: ResourceTypeApi
    version: VersionApi

    def __init__(self, api_client: ApiClient):
        """Create the resources service."""

        super().__init__(api_client)
        self.batch_operations = BatchOperationsApi(api_client)
        self.metadata_events = MetadataEventsApi(api_client)
        self.resource = ResourceApi(api_client)
        self.resource_constraint = ResourceConstraintApi(api_client)
        self.resource_type = ResourceTypeApi(api_client)
        self.version = VersionApi(api_client)
