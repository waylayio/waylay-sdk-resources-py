import json

import yaml


def with_example_provider(dct):
    has_example = False
    if "example" in dct:
        example, has_example = dct["example"], True
    elif "examples" in dct:
        examples = dct["examples"]
        if isinstance(examples, list) and list:
            example, has_example = examples[0], True
    elif "default" in dct:
        example, has_example = dct["default"], True

    if has_example:
        provider = (
            example
            if example is None or isinstance(example, (dict, list, int, float, bool))
            else f"'{example}'"
        )
        dct.update({"$provider": f"lambda: {provider}"})
    return dct


with open("openapi/resources.transformed.openapi.yaml", "r") as file:
    OPENAPI_SPEC = yaml.safe_load(file)

MODEL_DEFINITIONS = OPENAPI_SPEC["components"]["schemas"]

_array_must_contain_inner_model_schema = json.loads(
    r"""{
  "title" : "Array_Must_Contain_inner",
  "oneOf" : [ {
    "type" : "boolean"
  }, {
    "type" : "number"
  }, {
    "type" : "string"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Array_Must_Contain_inner": _array_must_contain_inner_model_schema
})

_array_value_constraint_model_schema = json.loads(
    r"""{
  "required" : [ "elementType", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/ArrayValueConstraint_type"
    },
    "elementType" : {
      "$ref" : "#/components/schemas/ValueConstraint"
    },
    "minLength" : {
      "minimum" : 0,
      "type" : "integer"
    },
    "maxLength" : {
      "minimum" : 0,
      "type" : "integer"
    },
    "uniqueValues" : {
      "type" : "boolean",
      "description" : "If true, all values in the array must be unique.",
      "default" : false
    },
    "contains" : {
      "title" : "Array Must Contain",
      "type" : "array",
      "description" : "Only supported if the `elementType` is `boolean`, `numeric` or `string`.\nSpecifies values the array attribute must contain.",
      "items" : {
        "$ref" : "#/components/schemas/Array_Must_Contain_inner"
      }
    }
  },
  "description" : "Specifies that a value must be an array and what type of elements it contains"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ArrayValueConstraint": _array_value_constraint_model_schema})

_array_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "ArrayValueConstraint_type",
  "type" : "string",
  "enum" : [ "array" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ArrayValueConstraint_type": _array_value_constraint_type_model_schema
})

_attribute_item_model_schema = json.loads(
    r"""{
  "title" : "AttributeItem",
  "required" : [ "name", "required", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "name of the attribute",
      "example" : "name"
    },
    "required" : {
      "title" : "required",
      "type" : "boolean",
      "description" : "Indicates if the attribute must be present or is optional",
      "example" : true
    },
    "type" : {
      "$ref" : "#/components/schemas/ValueConstraint"
    }
  },
  "description" : "Constraint on the presence and value of a single named _Resource_ attribute."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AttributeItem": _attribute_item_model_schema})

_batch_operation_enqueued_model_schema = json.loads(
    r"""{
  "title" : "Batch operation enqueued",
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 202
    },
    "uri" : {
      "type" : "string",
      "description" : "URI where the batch operation status can be followed",
      "format" : "uri",
      "example" : "/resources/v1/batch/afcea5a1-81df-44f6-bd34-e0b602a2cf3d"
    },
    "entity" : {
      "$ref" : "#/components/schemas/BatchRunningResourceOperation"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Batch_operation_enqueued": _batch_operation_enqueued_model_schema
})

_batch_operation_result_model_schema = json.loads(
    r"""{
  "example" : {
    "id" : "afcea5a1-81df-44f6-bd34-e0b602a2cf3d",
    "user" : "4b6c0c68-7c5f-4ad8-a138-e5d9d96242ed",
    "operation" : {
      "entity" : "resource",
      "action" : "delete",
      "description" : "deleting 3 resources"
    },
    "queueTime" : "2020-04-27T09:54:44.051Z",
    "finishedTime" : "2020-04-27T09:54:44.129Z",
    "results" : {
      "success" : {
        "d3d823f5-f214-4de8-7c0-f2c8c4db5ee1" : {
          "statusCode" : 204
        }
      },
      "failure" : {
        "82af367c-dffc-48d6-aea2-bfc699047174" : {
          "statusCode" : "404,",
          "error" : "No resource with id 82af367c-dffc-48d6-aea2-bfc699047174"
        },
        "e64de65c-e3ef-482d-9eb7-32ca17d1e147" : {
          "statusCode" : "400,",
          "error" : "Resource is still parent of or referenced by 2 resource(s)"
        }
      }
    }
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchRunningResourceOperation"
  }, {
    "$ref" : "#/components/schemas/OperationResultObject"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchOperationResult": _batch_operation_result_model_schema})

_batch_operation_status_response_model_schema = json.loads(
    r"""{
  "title" : "BatchOperationStatusResponse",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchOperationResult"
  }, {
    "$ref" : "#/components/schemas/BatchRunningResourceOperation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchOperationStatusResponse": _batch_operation_status_response_model_schema
})

_batch_resource_delete_operation_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceDeleteOperation",
  "required" : [ "action", "entity", "query" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchResourceDeleteOperation_entity"
    },
    "action" : {
      "$ref" : "#/components/schemas/BatchResourceDeleteOperation_action"
    },
    "query" : {
      "$ref" : "#/components/schemas/BatchResourceDeleteOperation_query"
    },
    "actionParameters" : {
      "$ref" : "#/components/schemas/BatchResourceDeleteOperation_actionParameters"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceDeleteOperation": _batch_resource_delete_operation_model_schema
})

_batch_resource_delete_operation_action_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceDeleteOperation_action",
  "type" : "string",
  "enum" : [ "delete" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceDeleteOperation_action": _batch_resource_delete_operation_action_model_schema
})

_batch_resource_delete_operation_action_parameters_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceDeleteOperation_actionParameters",
  "required" : [ "cascade" ],
  "type" : "object",
  "properties" : {
    "cascade" : {
      "$ref" : "#/components/schemas/CascadeDeleteValues"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceDeleteOperation_actionParameters": _batch_resource_delete_operation_action_parameters_model_schema
})

_batch_resource_delete_operation_entity_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceDeleteOperation_entity",
  "type" : "string",
  "description" : "Type of entities to remove",
  "enum" : [ "resource" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceDeleteOperation_entity": _batch_resource_delete_operation_entity_model_schema
})

_batch_resource_delete_operation_query_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceDeleteOperation_query",
  "required" : [ "ids" ],
  "type" : "object",
  "properties" : {
    "ids" : {
      "title" : "ids",
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ResourceId"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceDeleteOperation_query": _batch_resource_delete_operation_query_model_schema
})

_batch_resource_operation_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchResourceDeleteOperation"
  }, {
    "$ref" : "#/components/schemas/BatchResourceTypeDeleteOperation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceOperation": _batch_resource_operation_model_schema
})

_batch_resource_type_delete_operation_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceTypeDeleteOperation",
  "required" : [ "action", "entity", "query" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchResourceTypeDeleteOperation_entity"
    },
    "action" : {
      "$ref" : "#/components/schemas/BatchResourceDeleteOperation_action"
    },
    "query" : {
      "$ref" : "#/components/schemas/BatchResourceTypeDeleteOperation_query"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceTypeDeleteOperation": _batch_resource_type_delete_operation_model_schema
})

_batch_resource_type_delete_operation_entity_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceTypeDeleteOperation_entity",
  "type" : "string",
  "description" : "Type of entities to remove",
  "enum" : [ "resourcetype" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceTypeDeleteOperation_entity": _batch_resource_type_delete_operation_entity_model_schema
})

_batch_resource_type_delete_operation_query_model_schema = json.loads(
    r"""{
  "title" : "BatchResourceTypeDeleteOperation_query",
  "required" : [ "ids" ],
  "type" : "object",
  "properties" : {
    "ids" : {
      "title" : "ids",
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ResourceTypeId"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchResourceTypeDeleteOperation_query": _batch_resource_type_delete_operation_query_model_schema
})

_batch_running_resource_operation_model_schema = json.loads(
    r"""{
  "required" : [ "id", "operation", "queueTime", "user" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/BatchId"
    },
    "user" : {
      "$ref" : "#/components/schemas/UserId"
    },
    "queueTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "operation" : {
      "$ref" : "#/components/schemas/BatchRunningResourceOperation_operation"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchRunningResourceOperation": _batch_running_resource_operation_model_schema
})

_batch_running_resource_operation_operation_model_schema = json.loads(
    r"""{
  "title" : "BatchRunningResourceOperation_operation",
  "required" : [ "action", "description", "entity" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchRunningResourceOperation_operation_entity"
    },
    "action" : {
      "$ref" : "#/components/schemas/BatchResourceDeleteOperation_action"
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "example" : "deleting 2 resources"
    }
  },
  "description" : "Queued operation summary"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchRunningResourceOperation_operation": _batch_running_resource_operation_operation_model_schema
})

_batch_running_resource_operation_operation_entity_model_schema = json.loads(
    r"""{
  "title" : "BatchRunningResourceOperation_operation_entity",
  "type" : "string",
  "enum" : [ "resource", "resourcetype" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchRunningResourceOperation_operation_entity": _batch_running_resource_operation_operation_entity_model_schema
})

_boolean_value_constraint_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/BooleanValueConstraint_type"
    }
  },
  "description" : "Specifies that the value must be a boolean"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BooleanValueConstraint": _boolean_value_constraint_model_schema
})

_boolean_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "BooleanValueConstraint_type",
  "type" : "string",
  "enum" : [ "boolean" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BooleanValueConstraint_type": _boolean_value_constraint_type_model_schema
})

_cascade_delete_values_inner_model_schema = json.loads(
    r"""{
  "title" : "CascadeDeleteValues_inner",
  "type" : "string",
  "enum" : [ "alarms", "measurements", "tasks" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CascadeDeleteValues_inner": _cascade_delete_values_inner_model_schema
})

_changed_event_model_schema = json.loads(
    r"""{
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/ChangedEvent_type"
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
MODEL_DEFINITIONS.update({"ChangedEvent": _changed_event_model_schema})

_changed_event_type_model_schema = json.loads(
    r"""{
  "title" : "ChangedEvent_type",
  "type" : "string",
  "enum" : [ "update" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ChangedEvent_type": _changed_event_type_model_schema})

_cloud_metadata_event_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "./cloudevents.schema.yaml#/definitions/cloudevent_json"
  }, {
    "$ref" : "#/components/schemas/CloudMetadataEventData"
  }, {
    "required" : [ "id", "source", "specversion", "subject", "time", "type" ]
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CloudMetadataEvent": _cloud_metadata_event_model_schema})

_cloud_metadata_event_data_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "id" : {
      "example" : "dd59d2d9-9657-4d36-b045-ef97315f2d20"
    },
    "source" : {
      "$ref" : "#/components/schemas/CloudMetadataEventData_source"
    },
    "subject" : {
      "example" : "289dd1a3-35a7-44fa-8596-9aee3ad0b36f/2c49e3bf-547b-42bc-a5e9-9193155ec03d"
    },
    "type" : {
      "$ref" : "#/components/schemas/CloudMetadataEventData_type"
    },
    "data" : {
      "$ref" : "#/components/schemas/MetadataEvent"
    },
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CloudMetadataEventData": _cloud_metadata_event_data_model_schema
})

_cloud_metadata_event_data_source_model_schema = json.loads(
    r"""{
  "title" : "CloudMetadataEventData_source",
  "type" : "string",
  "example" : "/resources/v1/resources",
  "enum" : [ "/resources/v1/resources", "/resources/v1/resourcetypes" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CloudMetadataEventData_source": _cloud_metadata_event_data_source_model_schema
})

_cloud_metadata_event_data_type_model_schema = json.loads(
    r"""{
  "title" : "CloudMetadataEventData_type",
  "type" : "string",
  "enum" : [ "io.waylay.resources.v1.resourcetype.created", "io.waylay.resources.v1.resourcetype.updated", "io.waylay.resources.v1.resourcetype.deleted", "io.waylay.resources.v1.resource.created", "io.waylay.resources.v1.resource.updated", "io.waylay.resources.v1.resource.deleted", "io.waylay.resources.v1.resource.discovered" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CloudMetadataEventData_type": _cloud_metadata_event_data_type_model_schema
})

_constraint_model_schema = json.loads(
    r"""{
  "title" : "Constraint",
  "required" : [ "attributes", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "minLength" : 1,
      "type" : "string",
      "description" : "Name for the _Resource Constraint_",
      "example" : "Mandatory name"
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "A description for the _Resource Constraint_",
      "example" : "Makes the name attribute mandatory"
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "example" : [ "technology", "myTag" ],
      "items" : {
        "type" : "string"
      }
    },
    "attributes" : {
      "title" : "attributes",
      "type" : "array",
      "description" : "List of attribute descriptions",
      "items" : {
        "$ref" : "#/components/schemas/AttributeItem"
      }
    }
  },
  "description" : "Constraint on the attributes of a Resource"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Constraint": _constraint_model_schema})

_constraint_error_model_schema = json.loads(
    r"""{
  "title" : "ConstraintError",
  "required" : [ "error", "errorPath", "resources" ],
  "type" : "object",
  "properties" : {
    "error" : {
      "title" : "error",
      "type" : "string",
      "description" : "User error message",
      "example" : "Property address missing."
    },
    "errorPath" : {
      "title" : "errorPath",
      "type" : "string",
      "description" : "Attribute path",
      "example" : "/address"
    },
    "resources" : {
      "title" : "resources",
      "type" : "array",
      "description" : "Ids of the _Resources_ that fail the constraint",
      "example" : [ "d3d823f5-f214-4de8-7c0-f2c8c4db5ee1", "36bac1e0-841f-4085-804d-5ad304fef395" ],
      "items" : {
        "$ref" : "#/components/schemas/ResourceId"
      }
    }
  },
  "description" : "Validation Error report of a Resource Constraint"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ConstraintError": _constraint_error_model_schema})

_constraint_status_model_schema = json.loads(
    r"""{
  "title" : "ConstraintStatus",
  "required" : [ "constraintId", "status" ],
  "type" : "object",
  "properties" : {
    "status" : {
      "$ref" : "#/components/schemas/ConstraintStatus_status"
    },
    "constraintId" : {
      "$ref" : "#/components/schemas/ResourceConstraintId"
    },
    "errors" : {
      "title" : "errors",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ConstraintError"
      }
    }
  },
  "description" : "Reference to a _Resource Constraint_s and its validation status."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ConstraintStatus": _constraint_status_model_schema})

_constraint_status_status_model_schema = json.loads(
    r"""{
  "title" : "ConstraintStatus_status",
  "type" : "string",
  "example" : "failed",
  "enum" : [ "applying", "ineffect", "failed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ConstraintStatus_status": _constraint_status_status_model_schema
})

_create_event_model_schema = json.loads(
    r"""{
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/CreateEvent_type"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CreateEvent": _create_event_model_schema})

_create_event_type_model_schema = json.loads(
    r"""{
  "title" : "CreateEvent_type",
  "type" : "string",
  "enum" : [ "create" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CreateEvent_type": _create_event_type_model_schema})

_deleted_event_model_schema = json.loads(
    r"""{
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/BatchResourceDeleteOperation_action"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DeletedEvent": _deleted_event_model_schema})

_deleted_resource_event_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/DeletedEvent"
  }, {
    "properties" : {
      "cascadeDelete" : {
        "$ref" : "#/components/schemas/CascadeDeleteValues"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DeletedResourceEvent": _deleted_resource_event_model_schema})

_discovered_event_model_schema = json.loads(
    r"""{
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/DiscoveredEvent_type"
    },
    "message" : {
      "type" : "object",
      "description" : "The broker message that triggered the discovery"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DiscoveredEvent": _discovered_event_model_schema})

_discovered_event_type_model_schema = json.loads(
    r"""{
  "title" : "DiscoveredEvent_type",
  "type" : "string",
  "enum" : [ "discovered" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DiscoveredEvent_type": _discovered_event_type_model_schema})

_error_response_model_schema = json.loads(
    r"""{
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 400
    },
    "error" : {
      "type" : "string",
      "example" : "/address <- Property address missing."
    },
    "code" : {
      "type" : "string",
      "description" : "Optional error code"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ErrorResponse": _error_response_model_schema})

_failure_operation_result_value_model_schema = json.loads(
    r"""{
  "title" : "FailureOperationResult_value",
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "statusCode",
      "type" : "integer",
      "description" : "The statusCode of the operation"
    },
    "error" : {
      "title" : "error",
      "type" : "string",
      "description" : "Error description of what went wrong."
    }
  },
  "description" : "The keys will be resource ids or resource type ids."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "FailureOperationResult_value": _failure_operation_result_value_model_schema
})

_generic_metadata_event_model_schema = json.loads(
    r"""{
  "required" : [ "objectType", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "type" : "string"
    },
    "objectType" : {
      "type" : "string"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GenericMetadataEvent": _generic_metadata_event_model_schema})

_get_stream_event_format_parameter_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "application/cloudevents+json" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getStream_eventFormat_parameter": _get_stream_event_format_parameter_model_schema
})

_halid_link_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "required" : [ "id" ],
    "type" : "object",
    "properties" : {
      "id" : {
        "type" : "string",
        "description" : "Unique identifier of the linked item"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALIdLink": _halid_link_model_schema})

_hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "type" : "string",
      "description" : "(Relative) URL of the entity.",
      "format" : "uri",
      "example" : "/resources/v1/resources/d3d823f5-f214-4de8-7c0-f2c8c4db5ee1"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLink": _hal_link_model_schema})

_hal_page_links_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/Pagination_links"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALPageLinks": _hal_page_links_model_schema})

_hal_resource_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "HAL Representation of a Waylay _Resource_",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALSelfLinks"
  }, {
    "properties" : {
      "_links" : {
        "$ref" : "#/components/schemas/HALResourceEntity_allOf__links"
      },
      "_embedded" : {
        "$ref" : "#/components/schemas/HALResourceEntity_allOf__embedded"
      }
    }
  }, {
    "$ref" : "#/components/schemas/ResourceWithIdEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALResourceEntity": _hal_resource_entity_model_schema})

_hal_resource_entity_all_of__embedded_model_schema = json.loads(
    r"""{
  "title" : "HALResourceEntity_allOf__embedded",
  "type" : "object",
  "properties" : {
    "resourceType" : {
      "$ref" : "#/components/schemas/HALResourceTypeEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALResourceEntity_allOf__embedded": _hal_resource_entity_all_of__embedded_model_schema
})

_hal_resource_entity_all_of__links_model_schema = json.loads(
    r"""{
  "title" : "HALResourceEntity_allOf__links",
  "type" : "object",
  "properties" : {
    "parent" : {
      "$ref" : "#/components/schemas/HALResourceEntity_allOf__links_parent"
    },
    "children" : {
      "$ref" : "#/components/schemas/HALResourceEntity_allOf__links_children"
    },
    "resourceType" : {
      "$ref" : "#/components/schemas/HALResourceEntity_allOf__links_resourceType"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALResourceEntity_allOf__links": _hal_resource_entity_all_of__links_model_schema
})

_hal_resource_entity_all_of__links_children_model_schema = json.loads(
    r"""{
  "title" : "HALResourceEntity_allOf__links_children",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to fetch the children of the resource",
    "example" : {
      "href" : "/resources/v1/resources/d3d823f5-f214-4de8-7c0-f2c8c4db5ee1/children"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALResourceEntity_allOf__links_children": _hal_resource_entity_all_of__links_children_model_schema
})

_hal_resource_entity_all_of__links_parent_model_schema = json.loads(
    r"""{
  "title" : "HALResourceEntity_allOf__links_parent",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALIdLink"
  }, {
    "description" : "Link to the parent resource",
    "example" : {
      "href" : "/resources/v1/resources/658c4fb3-d25a-4bfa-aeca-3fb0009e9a8a",
      "id" : "658c4fb3-d25a-4bfa-aeca-3fb0009e9a8a"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALResourceEntity_allOf__links_parent": _hal_resource_entity_all_of__links_parent_model_schema
})

_hal_resource_entity_all_of__links_resource_type_model_schema = json.loads(
    r"""{
  "title" : "HALResourceEntity_allOf__links_resourceType",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALIdLink"
  }, {
    "description" : "Link to the resourceType for the resource",
    "example" : {
      "href" : "/resources/v1/resourcetypes/17b8b6ea-0573-4381-8088-8692f7938165",
      "id" : "17b8b6ea-0573-4381-8088-8692f7938165"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALResourceEntity_allOf__links_resourceType": _hal_resource_entity_all_of__links_resource_type_model_schema
})

_hal_resource_listing_model_schema = json.loads(
    r"""{
  "required" : [ "_embedded", "_links", "count", "limit", "skip", "total" ],
  "type" : "object",
  "description" : "Listing of _Resource_ entities in HAL format",
  "allOf" : [ {
    "$ref" : "#/components/schemas/PagingResult"
  }, {
    "$ref" : "#/components/schemas/PagingCount"
  }, {
    "$ref" : "#/components/schemas/HALPageLinks"
  }, {
    "properties" : {
      "_embedded" : {
        "$ref" : "#/components/schemas/HALResourceListing_allOf__embedded"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALResourceListing": _hal_resource_listing_model_schema})

_hal_resource_listing_all_of__embedded_model_schema = json.loads(
    r"""{
  "title" : "HALResourceListing_allOf__embedded",
  "required" : [ "values" ],
  "type" : "object",
  "properties" : {
    "values" : {
      "title" : "values",
      "type" : "array",
      "description" : "_Resource_ entities in HAL format",
      "items" : {
        "$ref" : "#/components/schemas/HALResourceEntity"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALResourceListing_allOf__embedded": _hal_resource_listing_all_of__embedded_model_schema
})

_hal_resource_type_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALSelfLinks"
  }, {
    "$ref" : "#/components/schemas/ResourceTypeEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALResourceTypeEntity": _hal_resource_type_entity_model_schema
})

_hal_self_links_model_schema = json.loads(
    r"""{
  "required" : [ "_links" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/HALSelfLinks__links"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALSelfLinks": _hal_self_links_model_schema})

_hal_self_links__links_model_schema = json.loads(
    r"""{
  "title" : "HALSelfLinks__links",
  "required" : [ "self" ],
  "type" : "object",
  "properties" : {
    "self" : {
      "$ref" : "#/components/schemas/HALSelfLinks__links_self"
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/HALSelfLinks__links_value"
  },
  "description" : "Links to related objects"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALSelfLinks__links": _hal_self_links__links_model_schema})

_hal_self_links__links_self_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to the resource"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALSelfLinks__links_self": _hal_self_links__links_self_model_schema
})

_hal_self_links__links_value_model_schema = json.loads(
    r"""{
  "title" : "HALSelfLinks__links_value",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALIdLink"
  }, {
    "description" : "Link to a referenced resource"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "HALSelfLinks__links_value": _hal_self_links__links_value_model_schema
})

_list_constraints_200_response_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "properties" : {
      "values" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/ResourceConstraintWithIdEntity"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/PagingResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "listConstraints_200_response": _list_constraints_200_response_model_schema
})

_list_resources_order_parameter_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "ascending",
  "enum" : [ "ascending", "descending" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "list_resources_order_parameter": _list_resources_order_parameter_model_schema
})

_metadata_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "provider" : {
      "$ref" : "#/components/schemas/Provider"
    },
    "providerId" : {
      "type" : "string",
      "example" : "provider_123"
    },
    "customer" : {
      "$ref" : "#/components/schemas/Customer"
    },
    "firmware" : {
      "type" : "string",
      "example" : "1.21234"
    },
    "location" : {
      "$ref" : "#/components/schemas/MetadataEntity_location"
    },
    "metrics" : {
      "type" : "array",
      "description" : "A documentation of possible measurements that are to be expected on\n_Waylay Events_ associated with this _Resource_.",
      "items" : {
        "$ref" : "#/components/schemas/ResourceMetric"
      }
    },
    "sensors" : {
      "type" : "array",
      "description" : "Set of sensors that are applicable for a given _Resource_.\nPlease note that there is no explicit action taken by the Waylay platform on this meta key.\nThe idea behind this abstraction is to assist integrations where an architect of the digital twin\ncan specify which sensors from waylay library are applicable for a given _Resource_ (or _Resource Type_).",
      "items" : {
        "$ref" : "#/components/schemas/ResourceSensor"
      }
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/User_Resource_properties"
  },
  "description" : "Common attributes for _Resource_ or _Resource Type_"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MetadataEntity": _metadata_entity_model_schema})

_metadata_entity_location_model_schema = json.loads(
    r"""{
  "title" : "MetadataEntity_location",
  "required" : [ "lat", "lon" ],
  "type" : "object",
  "properties" : {
    "lat" : {
      "$ref" : "#/components/schemas/Latitude"
    },
    "lon" : {
      "$ref" : "#/components/schemas/Longitude"
    }
  },
  "description" : "A global location, expressed as a longitude-latitude pair."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "MetadataEntity_location": _metadata_entity_location_model_schema
})

_metadata_event_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ResourceMetadataEvent"
  }, {
    "$ref" : "#/components/schemas/ResourcetypeMetadataEvent"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MetadataEvent": _metadata_event_model_schema})

_nd_json_response_stream_model_schema = json.loads(
    r"""{
  "title" : "NdJsonResponseStream",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/MetadataEvent"
  }, {
    "$ref" : "#/components/schemas/CloudMetadataEvent"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NdJsonResponseStream": _nd_json_response_stream_model_schema
})

_numeric_enum_value_constraint_model_schema = json.loads(
    r"""{
  "required" : [ "enumType", "items", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/NumericEnumValueConstraint_type"
    },
    "enumType" : {
      "$ref" : "#/components/schemas/NumericValueConstraint_type"
    },
    "items" : {
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "type" : "number"
      }
    }
  },
  "description" : "Specifies that a value must be one of the given numbers."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NumericEnumValueConstraint": _numeric_enum_value_constraint_model_schema
})

_numeric_enum_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "NumericEnumValueConstraint_type",
  "type" : "string",
  "enum" : [ "enum" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NumericEnumValueConstraint_type": _numeric_enum_value_constraint_type_model_schema
})

_numeric_value_constraint_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/NumericValueConstraint_type"
    },
    "minimum" : {
      "type" : "number",
      "description" : "Specifies the minimum value the attribute can have",
      "example" : -1486.147
    },
    "maximum" : {
      "type" : "number",
      "description" : "Specifies the maximum value the attribute can have",
      "example" : 784596
    }
  },
  "description" : "Specifies that a value must be a number."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NumericValueConstraint": _numeric_value_constraint_model_schema
})

_numeric_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "NumericValueConstraint_type",
  "type" : "string",
  "enum" : [ "numeric" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NumericValueConstraint_type": _numeric_value_constraint_type_model_schema
})

_object_value_constraint_model_schema = json.loads(
    r"""{
  "required" : [ "attributes", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/ObjectValueConstraint_type"
    },
    "attributes" : {
      "type" : "array",
      "description" : "Attributes descriptions",
      "items" : {
        "$ref" : "#/components/schemas/AttributeItem"
      }
    }
  },
  "description" : "Specifies that a value must be an object and which attributes it needs to have"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ObjectValueConstraint": _object_value_constraint_model_schema
})

_object_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "ObjectValueConstraint_type",
  "type" : "string",
  "enum" : [ "object" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ObjectValueConstraint_type": _object_value_constraint_type_model_schema
})

_operation_result_object_model_schema = json.loads(
    r"""{
  "required" : [ "finishedTime", "results" ],
  "type" : "object",
  "properties" : {
    "finishedTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "results" : {
      "$ref" : "#/components/schemas/OperationResultObject_results"
    }
  },
  "description" : "Finished Batch Operation results"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "OperationResultObject": _operation_result_object_model_schema
})

_operation_result_object_results_model_schema = json.loads(
    r"""{
  "title" : "OperationResultObject_results",
  "required" : [ "failure", "success" ],
  "type" : "object",
  "properties" : {
    "success" : {
      "$ref" : "#/components/schemas/SuccessOperationResult"
    },
    "failure" : {
      "$ref" : "#/components/schemas/FailureOperationResult"
    }
  },
  "description" : "Operation results"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "OperationResultObject_results": _operation_result_object_results_model_schema
})

_pagination_links_model_schema = json.loads(
    r"""{
  "title" : "Pagination links",
  "required" : [ "self" ],
  "type" : "object",
  "properties" : {
    "self" : {
      "$ref" : "#/components/schemas/Pagination_links_self"
    },
    "next" : {
      "$ref" : "#/components/schemas/Pagination_links_next"
    },
    "prev" : {
      "$ref" : "#/components/schemas/Pagination_links_prev"
    }
  },
  "description" : "HAL links for pagination"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Pagination_links": _pagination_links_model_schema})

_pagination_links_next_model_schema = json.loads(
    r"""{
  "title" : "Pagination_links_next",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to the next page of the results (if available)",
    "example" : {
      "href" : "/resources/v1/resources?skip=400"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Pagination_links_next": _pagination_links_next_model_schema})

_pagination_links_prev_model_schema = json.loads(
    r"""{
  "title" : "Pagination_links_prev",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to the previous page of the results (if available)",
    "example" : {
      "href" : "/resources/v1/resources?skip=200"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Pagination_links_prev": _pagination_links_prev_model_schema})

_pagination_links_self_model_schema = json.loads(
    r"""{
  "title" : "Pagination_links_self",
  "allOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "description" : "Link to this page of the results",
    "example" : {
      "href" : "/resources/v1/resources?skip=300"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Pagination_links_self": _pagination_links_self_model_schema})

_paging_count_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "count" : {
      "title" : "Page Count",
      "type" : "integer",
      "description" : "The number of items in this result page.",
      "example" : 10
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PagingCount": _paging_count_model_schema})

_paging_result_model_schema = json.loads(
    r"""{
  "required" : [ "limit", "skip", "total" ],
  "type" : "object",
  "properties" : {
    "skip" : {
      "$ref" : "#/components/schemas/PagingSkip"
    },
    "limit" : {
      "$ref" : "#/components/schemas/PagingLimit"
    },
    "total" : {
      "$ref" : "#/components/schemas/PagingTotal"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PagingResult": _paging_result_model_schema})

_patch_resource_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/ResourceEntity"
  }, {
    "type" : "object",
    "properties" : {
      "resourceTypeId" : {
        "nullable" : true
      },
      "parentId" : {
        "nullable" : true
      },
      "name" : {
        "nullable" : true
      },
      "alias" : {
        "nullable" : true
      },
      "lastMessageTimestamp" : {
        "nullable" : true
      },
      "owner" : {
        "nullable" : true
      },
      "tags" : {
        "nullable" : true
      },
      "provider" : {
        "nullable" : true
      },
      "providerId" : {
        "nullable" : true
      },
      "customer" : {
        "nullable" : true
      },
      "firmware" : {
        "nullable" : true
      },
      "location" : {
        "nullable" : true
      },
      "metrics" : {
        "nullable" : true
      },
      "sensors" : {
        "nullable" : true
      }
    },
    "additionalProperties" : {
      "nullable" : true
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PatchResourceEntity": _patch_resource_entity_model_schema})

_patch_resource_type_entity_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/ResourceTypeWithConstraints"
  }, {
    "type" : "object",
    "properties" : {
      "name" : {
        "nullable" : true
      },
      "templates" : {
        "nullable" : true
      },
      "provider" : {
        "nullable" : true
      },
      "providerId" : {
        "nullable" : true
      },
      "customer" : {
        "nullable" : true
      },
      "firmware" : {
        "nullable" : true
      },
      "location" : {
        "nullable" : true
      },
      "metrics" : {
        "nullable" : true
      },
      "sensors" : {
        "nullable" : true
      }
    },
    "additionalProperties" : {
      "nullable" : true
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PatchResourceTypeEntity": _patch_resource_type_entity_model_schema
})

_resource_change_model_schema = json.loads(
    r"""{
  "required" : [ "change", "resourceId", "time", "userId" ],
  "type" : "object",
  "properties" : {
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "resourceId" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "userId" : {
      "$ref" : "#/components/schemas/UserId"
    },
    "change" : {
      "$ref" : "#/components/schemas/ResourceChange_change"
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceChange": _resource_change_model_schema})

_resource_change_change_model_schema = json.loads(
    r"""{
  "title" : "ResourceChange_change",
  "type" : "string",
  "enum" : [ "created", "updated", "deleted" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceChange_change": _resource_change_change_model_schema
})

_resource_changes_paged_response_model_schema = json.loads(
    r"""{
  "title" : "ResourceChangesPagedResponse",
  "type" : "object",
  "allOf" : [ {
    "properties" : {
      "values" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/ResourceChange"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/PagingResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceChangesPagedResponse": _resource_changes_paged_response_model_schema
})

_resource_constraint_creation_response_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 201
    },
    "uri" : {
      "type" : "string",
      "format" : "uri",
      "example" : "/resources/v1/resourceconstraints/cfd2b48e-a141-4d2e-8ec8-f09ce4f65ae3"
    },
    "entity" : {
      "$ref" : "#/components/schemas/ResourceConstraintWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceConstraintCreationResponse": _resource_constraint_creation_response_model_schema
})

_resource_constraint_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "properties" : {
      "id" : {
        "$ref" : "#/components/schemas/ResourceConstraintId"
      }
    }
  }, {
    "$ref" : "#/components/schemas/Constraint"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceConstraintEntity": _resource_constraint_entity_model_schema
})

_resource_constraint_with_id_entity_model_schema = json.loads(
    r"""{
  "title" : "ResourceConstraintWithIdEntity",
  "allOf" : [ {
    "$ref" : "#/components/schemas/WithIdRequired"
  }, {
    "$ref" : "#/components/schemas/ResourceConstraintEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceConstraintWithIdEntity": _resource_constraint_with_id_entity_model_schema
})

_resource_creation_response_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "number",
      "example" : 201
    },
    "uri" : {
      "type" : "string",
      "format" : "uri",
      "example" : "/resources/v1/resources/d3d823f5-f214-4de8-7c0-f2c8c4db5ee1"
    },
    "entity" : {
      "$ref" : "#/components/schemas/ResourceWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceCreationResponse": _resource_creation_response_model_schema
})

_resource_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Representation of a Waylay Resource",
  "allOf" : [ {
    "properties" : {
      "id" : {
        "$ref" : "#/components/schemas/ResourceId"
      },
      "resourceTypeId" : {
        "title" : "Resource Type",
        "description" : "Id of the linked _Resource Type_",
        "allOf" : [ {
          "$ref" : "#/components/schemas/ResourceTypeId"
        } ]
      },
      "parentId" : {
        "title" : "Resource Parent",
        "description" : "Id of the parent _Resource_",
        "example" : "658c4fb3-d25a-4bfa-aeca-3fb0009e9a8a",
        "allOf" : [ {
          "$ref" : "#/components/schemas/ResourceId"
        } ]
      },
      "name" : {
        "title" : "Name",
        "type" : "string",
        "description" : "Name for the _Resource_",
        "example" : "testresource"
      },
      "alias" : {
        "type" : "string",
        "description" : "Alias for the name of the _Resource_",
        "example" : "testresource-alias"
      },
      "lastMessageTimestamp" : {
        "description" : "Epoch time of the last contact",
        "allOf" : [ {
          "$ref" : "#/components/schemas/UnixEpochMillis"
        } ]
      },
      "owner" : {
        "type" : "string",
        "description" : "Owner of the _Resource_"
      },
      "tags" : {
        "$ref" : "#/components/schemas/Tags"
      }
    }
  }, {
    "$ref" : "#/components/schemas/MetadataEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceEntity": _resource_entity_model_schema})

_resource_id_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Primary identifier of a _Resource_",
  "example" : "d3d823f5-f214-4de8-7c0-f2c8c4db5ee1",
  "anyOf" : [ {
    "title" : "System Generated Id",
    "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "type" : "string",
    "description" : "A _Resource_ id generated by the Waylay System"
  }, {
    "title" : "User Provided Id",
    "type" : "string",
    "description" : "A _Resource_ id assigned by the user upon creation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceId": _resource_id_model_schema})

_resource_listing_model_schema = json.loads(
    r"""{
  "required" : [ "limit", "skip", "total", "values" ],
  "type" : "object",
  "description" : "A full listing _Resource_ entities",
  "allOf" : [ {
    "properties" : {
      "values" : {
        "type" : "array",
        "description" : "_Resource_ entities",
        "items" : {
          "$ref" : "#/components/schemas/ResourceWithIdEntity"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/PagingResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceListing": _resource_listing_model_schema})

_resource_metadata_event_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericMetadataEvent"
  }, {
    "required" : [ "resource" ],
    "properties" : {
      "objectType" : {
        "$ref" : "#/components/schemas/ResourceMetadataEvent_allOf_objectType"
      },
      "resource" : {
        "$ref" : "#/components/schemas/ResourceEntity"
      }
    }
  }, {
    "oneOf" : [ {
      "$ref" : "#/components/schemas/CreateEvent"
    }, {
      "$ref" : "#/components/schemas/DeletedResourceEvent"
    }, {
      "$ref" : "#/components/schemas/ChangedEvent"
    }, {
      "$ref" : "#/components/schemas/DiscoveredEvent"
    } ]
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetadataEvent": _resource_metadata_event_model_schema
})

_resource_metadata_event_all_of_object_type_model_schema = json.loads(
    r"""{
  "title" : "ResourceMetadataEvent_allOf_objectType",
  "type" : "string",
  "enum" : [ "resource" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetadataEvent_allOf_objectType": _resource_metadata_event_all_of_object_type_model_schema
})

_resource_metric_model_schema = json.loads(
    r"""{
  "title" : "ResourceMetric",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "Metric name",
      "type" : "string",
      "description" : "The key under which values of this metric are present in the root of a Waylay Event.\nAlso the _metric_ identifier in the timeseries database for these values when stored.",
      "example" : "temperature"
    },
    "valueType" : {
      "title" : "Value type",
      "type" : "string",
      "description" : "Type of the value",
      "example" : "integer"
    },
    "valueChoices" : {
      "title" : "Value Choice",
      "type" : "array",
      "description" : "Enumeration of the possible values for a metric",
      "items" : {
        "type" : "string"
      }
    },
    "metricType" : {
      "$ref" : "#/components/schemas/ResourceMetric_metricType"
    },
    "unit" : {
      "title" : "unit",
      "type" : "string",
      "description" : "Physical measurement unit, preferentially SI unit, for the numerical values of this metric",
      "example" : "m^3/s"
    },
    "maximum" : {
      "title" : "maximum",
      "type" : "number",
      "description" : "Expected maximum value for this metric.",
      "example" : 200.01
    },
    "minimum" : {
      "title" : "minimum",
      "type" : "number",
      "description" : "Expected minimum value for this metric.",
      "example" : -0.0000010
    }
  },
  "description" : "Describes a value that is expected to be present in the events sent to Waylay on behalf of this _Resource (Type)_.\nBy default, such values will end up in the time series database, where each time series is identified by the\n_resource id_ and the _metric name_.\n\n> Note: The Waylay System does not enforce any of the statements made in a _Resource Metric_ when\n> processing or retrieving data. As long as a user does not explicitly use this metadata to configure\n> behaviour, a _Resource Metric_ is purely a documentation entity."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceMetric": _resource_metric_model_schema})

_resource_metric_metric_type_model_schema = json.loads(
    r"""{
  "title" : "ResourceMetric_metricType",
  "type" : "string",
  "description" : "How measurements should be treated as a time series.",
  "example" : "counter",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ResourceMetric_metricType_oneOf"
  }, {
    "$ref" : "#/components/schemas/ResourceMetric_metricType_oneOf_1"
  }, {
    "$ref" : "#/components/schemas/ResourceMetric_metricType_oneOf_2"
  }, {
    "$ref" : "#/components/schemas/ResourceMetric_metricType_oneOf_3"
  }, {
    "$ref" : "#/components/schemas/ResourceMetric_metricType_oneOf_4"
  } ],
  "default" : "gauge"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetric_metricType": _resource_metric_metric_type_model_schema
})

_resource_metric_metric_type_one_of_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "A number per second (implies that unit ends on ‘/s’)",
  "enum" : [ "rate" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetric_metricType_oneOf": _resource_metric_metric_type_one_of_model_schema
})

_resource_metric_metric_type_one_of_1_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "A number per a given interval (such as a statsd flushInterval)",
  "enum" : [ "count" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetric_metricType_oneOf_1": _resource_metric_metric_type_one_of_1_model_schema
})

_resource_metric_metric_type_one_of_2_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Values at each point in time",
  "enum" : [ "gauge" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetric_metricType_oneOf_2": _resource_metric_metric_type_one_of_2_model_schema
})

_resource_metric_metric_type_one_of_3_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Keeps increasing over time (but might wrap/reset at some point) i.e. a gauge with the added notion of “i usually want to derive this to see the rate”",
  "enum" : [ "counter" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetric_metricType_oneOf_3": _resource_metric_metric_type_one_of_3_model_schema
})

_resource_metric_metric_type_one_of_4_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Value represents a unix timestamp. so basically a gauge or counter but we know we can also render the “age” at each point.",
  "enum" : [ "timestamp" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceMetric_metricType_oneOf_4": _resource_metric_metric_type_one_of_4_model_schema
})

_resource_ref_value_constraint_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/ResourceRefValueConstraint_type"
    },
    "attributes" : {
      "type" : "array",
      "description" : "Additional attributes in the reference object, describing the relation.",
      "items" : {
        "$ref" : "#/components/schemas/AttributeItem"
      }
    },
    "resourceTypes" : {
      "type" : "array",
      "description" : "The possible _Resource Types_ for the referenced _Resource_.",
      "items" : {
        "$ref" : "#/components/schemas/ResourceTypeId"
      }
    },
    "exists" : {
      "type" : "boolean",
      "description" : "Flag to indicate if the referenced _Resource_ must exist",
      "default" : false
    }
  },
  "description" : "Specifies that a value is an object having a required '$ref' attribute\nthat references another _Resource_."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceRefValueConstraint": _resource_ref_value_constraint_model_schema
})

_resource_ref_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "ResourceRefValueConstraint_type",
  "type" : "string",
  "enum" : [ "resourceRef" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceRefValueConstraint_type": _resource_ref_value_constraint_type_model_schema
})

_resource_reference_model_schema = json.loads(
    r"""{
  "required" : [ "$ref" ],
  "type" : "object",
  "properties" : {
    "$ref" : {
      "title" : "Resource URI",
      "pattern" : "^/resources/.*",
      "type" : "string",
      "description" : "A URI for the _Resource_, formatted as `/resources/{resourceId}`",
      "format" : "uri-reference",
      "example" : "/resources/04592b9a-e0c2-4e64-8c9a-202e50cd9275"
    }
  },
  "additionalProperties" : {
    "title" : "Relation Attributes",
    "description" : "Additional attributes that describe the relation with the referenced _Resource_."
  },
  "description" : "Represents a reference to a _Resource_"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceReference": _resource_reference_model_schema})

_resource_sensor_model_schema = json.loads(
    r"""{
  "title" : "ResourceSensor",
  "required" : [ "name", "sensor" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "An alias name for the sensor in the context of this _Resource_."
    },
    "sensor" : {
      "$ref" : "#/components/schemas/ResourceSensor_sensor"
    }
  },
  "description" : "Sensor associated with a _Resource_",
  "example" : {
    "name" : "events",
    "sensor" : {
      "name" : "GoogleCalendarStreamSensor",
      "version" : "0.1.5",
      "properties" : {
        "timeout" : 15
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceSensor": _resource_sensor_model_schema})

_resource_sensor_sensor_model_schema = json.loads(
    r"""{
  "title" : "ResourceSensor_sensor",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The identifying name of the _Waylay Sensor_"
    },
    "version" : {
      "title" : "version",
      "pattern" : "\\d+\\.\\d+\\.\\d+",
      "type" : "string",
      "description" : "The sensor version"
    },
    "properties" : {
      "title" : "properties",
      "type" : "object",
      "description" : "Default sensor property configuration."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceSensor_sensor": _resource_sensor_sensor_model_schema
})

_resource_type_change_model_schema = json.loads(
    r"""{
  "required" : [ "change", "resourceTypeId", "time", "userId" ],
  "type" : "object",
  "properties" : {
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "resourceTypeId" : {
      "$ref" : "#/components/schemas/ResourceTypeId"
    },
    "userId" : {
      "$ref" : "#/components/schemas/UserId"
    },
    "change" : {
      "$ref" : "#/components/schemas/ResourceChange_change"
    },
    "resourceType" : {
      "$ref" : "#/components/schemas/ResourceTypeWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceTypeChange": _resource_type_change_model_schema})

_resource_type_creation_response_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "number",
      "example" : 201
    },
    "uri" : {
      "type" : "string",
      "format" : "uri",
      "example" : "/resources/v1/resourcetypes/17b8b6ea-0573-4381-8088-8692f7938165"
    },
    "entity" : {
      "$ref" : "#/components/schemas/ResourceTypeWithIdEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceTypeCreationResponse": _resource_type_creation_response_model_schema
})

_resource_type_entity_model_schema = json.loads(
    r"""{
  "description" : "Representation of a _Resource Type_",
  "allOf" : [ {
    "properties" : {
      "id" : {
        "$ref" : "#/components/schemas/ResourceTypeId"
      },
      "name" : {
        "title" : "Name",
        "type" : "string",
        "description" : "Name for the _Resource Type_",
        "example" : "MyDeviceType"
      },
      "templates" : {
        "title" : "Managed Task Templates",
        "type" : "array",
        "description" : "Templates for task that is automatically created whenever a new \n_Resource_ of this _Resource Type_ is created.",
        "items" : {
          "$ref" : "#/components/schemas/TaskConfiguration"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/MetadataEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceTypeEntity": _resource_type_entity_model_schema})

_resource_type_id_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Primary identifier of a _Resource Type_",
  "example" : "17b8b6ea-0573-4381-8088-8692f7938165",
  "anyOf" : [ {
    "title" : "System Generated Id",
    "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "type" : "string",
    "description" : "A Resource Type id generated by the Waylay System"
  }, {
    "title" : "User Provided Id",
    "type" : "string",
    "description" : "A _Resource Type_ id assigned by the user upon creation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceTypeId": _resource_type_id_model_schema})

_resource_type_listing_model_schema = json.loads(
    r"""{
  "required" : [ "limit", "skip", "total", "values" ],
  "type" : "object",
  "description" : "A listing of _Resource Type_ entities",
  "allOf" : [ {
    "properties" : {
      "values" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/ResourceTypeWithIdEntity"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/PagingResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceTypeListing": _resource_type_listing_model_schema})

_resource_type_with_constraints_model_schema = json.loads(
    r"""{
  "title" : "ResourceTypeWithConstraints",
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/ResourceTypeEntity"
  }, {
    "properties" : {
      "$constraints" : {
        "title" : "Resource Type Constraints",
        "type" : "array",
        "description" : "Validation constraint to be applied to each _Resource_ that has\nits `resourceTypeId` attribute set to the `id` of this _Resource Type_.",
        "items" : {
          "$ref" : "#/components/schemas/ResourceConstraintId"
        }
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceTypeWithConstraints": _resource_type_with_constraints_model_schema
})

_resource_type_with_id_entity_model_schema = json.loads(
    r"""{
  "title" : "ResourceTypeWithIdEntity",
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/WithIdRequired"
  }, {
    "$ref" : "#/components/schemas/ResourceTypeEntity"
  }, {
    "properties" : {
      "$bulkOperation" : {
        "title" : "Running Operation",
        "type" : "string",
        "description" : "Indicates an asynchronous operation is busy for the _Resource Type_.",
        "example" : "d44b2ce9-fb7e-453e-a8bf-b7fefd933313"
      },
      "$constraints" : {
        "title" : "Applied Resource Type Constraints",
        "type" : "array",
        "description" : "Validation constraint as applied to each _Resource_ that has\nits `resourceTypeId` attribute set to the `id` of this _Resource Type_.",
        "items" : {
          "$ref" : "#/components/schemas/ConstraintStatus"
        }
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceTypeWithIdEntity": _resource_type_with_id_entity_model_schema
})

_resource_types_changes_paged_response_model_schema = json.loads(
    r"""{
  "title" : "ResourceTypesChangesPagedResponse",
  "type" : "object",
  "allOf" : [ {
    "properties" : {
      "values" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/ResourceTypeChange"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/PagingResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceTypesChangesPagedResponse": _resource_types_changes_paged_response_model_schema
})

_resource_with_id_entity_model_schema = json.loads(
    r"""{
  "title" : "ResourceWithIdEntity",
  "allOf" : [ {
    "$ref" : "#/components/schemas/WithIdRequired"
  }, {
    "$ref" : "#/components/schemas/ResourceEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceWithIdEntity": _resource_with_id_entity_model_schema
})

_resourcetype_metadata_event_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericMetadataEvent"
  }, {
    "oneOf" : [ {
      "$ref" : "#/components/schemas/CreateEvent"
    }, {
      "$ref" : "#/components/schemas/DeletedEvent"
    }, {
      "$ref" : "#/components/schemas/ChangedEvent"
    } ]
  }, {
    "required" : [ "resourcetype" ],
    "properties" : {
      "objectType" : {
        "$ref" : "#/components/schemas/ResourcetypeMetadataEvent_allOf_objectType"
      },
      "resourcetype" : {
        "$ref" : "#/components/schemas/ResourceTypeEntity"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourcetypeMetadataEvent": _resourcetype_metadata_event_model_schema
})

_resourcetype_metadata_event_all_of_object_type_model_schema = json.loads(
    r"""{
  "title" : "ResourcetypeMetadataEvent_allOf_objectType",
  "type" : "string",
  "enum" : [ "resourcetype" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourcetypeMetadataEvent_allOf_objectType": _resourcetype_metadata_event_all_of_object_type_model_schema
})

_ss_event_stream_model_schema = json.loads(
    r"""{
  "title" : "SSEventStream",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/MetadataEvent"
  }, {
    "$ref" : "#/components/schemas/CloudMetadataEvent"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SSEventStream": _ss_event_stream_model_schema})

_schema_validation_error_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "schemaPath" : {
      "type" : "string",
      "example" : "#"
    },
    "errors" : {
      "type" : "object",
      "example" : { }
    },
    "keyword" : {
      "type" : "string",
      "example" : "required"
    },
    "msgs" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "example" : "Property address missing."
      }
    },
    "value" : {
      "type" : "object",
      "example" : {
        "id" : "714bbf92-5dfc-4c42-9623-1c6e72708126",
        "resourceTypeId" : "bruno",
        "name" : "bruno",
        "customer" : "bruno_customer",
        "array" : [ {
          "coucou" : true,
          "customer" : "bravo"
        }, {
          "coucou" : false
        } ]
      }
    },
    "instancePath" : {
      "type" : "string",
      "example" : "/address"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SchemaValidationError": _schema_validation_error_model_schema
})

_string_enum_value_constraint_model_schema = json.loads(
    r"""{
  "required" : [ "enumType", "items", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/NumericEnumValueConstraint_type"
    },
    "enumType" : {
      "$ref" : "#/components/schemas/StringValueConstraint_type"
    },
    "items" : {
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    }
  },
  "description" : "Specifies that a value must be one of the given strings."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "StringEnumValueConstraint": _string_enum_value_constraint_model_schema
})

_string_value_constraint_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/StringValueConstraint_type"
    },
    "minLength" : {
      "minimum" : 0,
      "type" : "integer",
      "description" : "Minimum length a value must have",
      "example" : 1
    },
    "maxLength" : {
      "minimum" : 0,
      "type" : "integer",
      "description" : "Maximum length a value can have",
      "example" : 255
    }
  },
  "description" : "Specifies that a value must be a string."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "StringValueConstraint": _string_value_constraint_model_schema
})

_string_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "StringValueConstraint_type",
  "type" : "string",
  "enum" : [ "string" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "StringValueConstraint_type": _string_value_constraint_type_model_schema
})

_success_operation_result_value_model_schema = json.loads(
    r"""{
  "title" : "SuccessOperationResult_value",
  "required" : [ "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "statusCode",
      "type" : "integer",
      "description" : "The statusCode of the operation"
    }
  },
  "description" : "The keys will be resource ids or resource type ids."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SuccessOperationResult_value": _success_operation_result_value_model_schema
})

_task_configuration_model_schema = json.loads(
    r"""{
  "title" : "TaskConfiguration",
  "required" : [ "templateName" ],
  "type" : "object",
  "properties" : {
    "templateName" : {
      "title" : "Template Name",
      "type" : "string"
    },
    "type" : {
      "$ref" : "#/components/schemas/TaskConfiguration_type"
    }
  },
  "additionalProperties" : {
    "description" : "Additional task creation attributes"
  },
  "description" : "Specification of a template and task creation attributes\nfor the task that gets instantiate when a _Resource_ created.",
  "example" : {
    "templateName" : "CheckThreshold",
    "type" : "reactive",
    "resetObservations" : false,
    "parallel" : true
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskConfiguration": _task_configuration_model_schema})

_task_configuration_type_model_schema = json.loads(
    r"""{
  "title" : "TaskConfiguration_type",
  "type" : "string",
  "enum" : [ "periodic", "onetime", "scheduled", "reactive" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TaskConfiguration_type": _task_configuration_type_model_schema
})

_user_resource_properties_model_schema = json.loads(
    r"""{
  "title" : "User Resource properties",
  "description" : "Other key-value properties provisioned by the user.",
  "nullable" : true,
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ResourceReference"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "User_Resource_properties": _user_resource_properties_model_schema
})

_validation_failure_model_schema = json.loads(
    r"""{
  "title" : "Validation Failure",
  "allOf" : [ {
    "$ref" : "#/components/schemas/ErrorResponse"
  }, {
    "type" : "object",
    "properties" : {
      "details" : {
        "$ref" : "#/components/schemas/SchemaValidationErrors"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Validation_Failure": _validation_failure_model_schema})

_version_response_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "example" : "resources-service"
    },
    "version" : {
      "type" : "string",
      "example" : "7.3.0"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionResponse": _version_response_model_schema})

_with_id_required_model_schema = json.loads(
    r"""{
  "required" : [ "id" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "type" : "string"
    }
  },
  "example" : {
    "id" : "afcea5a1-81df-44f6-bd34-e0b602a2cf3d"
  },
  "x-comment" : "Entity with a required id"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WithIdRequired": _with_id_required_model_schema})
