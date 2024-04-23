# coding: utf-8
"""Waylay Resources api.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Literal,
    TypeVar,
    overload,
)

from pydantic import (
    Field,
    StrictBool,
    TypeAdapter,
)
from typing_extensions import (
    Annotated,  # >=3.9,
)
from waylay.sdk.api import (
    HeaderTypes,
    QueryParamTypes,
    Response,
)
from waylay.sdk.api._models import Model
from waylay.sdk.plugin import WithApiClient

if TYPE_CHECKING:
    from waylay.services.resources.models import (
        Constraint,
        ErrorResponse,
        ResourceConstraintCreationResponse,
        ResourceConstraintWithIdEntity,
    )
    from waylay.services.resources.queries.resource_constraint_api import (
        CreateQuery,
        DeleteQuery,
        GetQuery,
        ListQuery,
        ReplaceQuery,
    )


try:
    from waylay.services.resources.models import (
        Constraint,
        ErrorResponse,
        ResourceConstraintCreationResponse,
        ResourceConstraintWithIdEntity,
    )
    from waylay.services.resources.queries.resource_constraint_api import (
        CreateQuery,
        DeleteQuery,
        GetQuery,
        ListQuery,
        ReplaceQuery,
    )

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        Constraint = Model

        CreateQuery = dict
        ResourceConstraintCreationResponse = Model

        ErrorResponse = Model

        DeleteQuery = dict

        ErrorResponse = Model

        ErrorResponse = Model

        GetQuery = dict
        ResourceConstraintWithIdEntity = Model

        ErrorResponse = Model

        ListQuery = dict
        ResourceConstraintWithIdEntity = Model

        Constraint = Model

        ReplaceQuery = dict
        ResourceConstraintWithIdEntity = Model

        ErrorResponse = Model

        ErrorResponse = Model


T = TypeVar("T")


class ResourceConstraintApi(WithApiClient):
    """ResourceConstraintApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def create(
        self,
        *,
        json: Constraint,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResourceConstraintCreationResponse: ...

    @overload
    async def create(
        self,
        *,
        json: Constraint,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def create(
        self,
        *,
        json: Constraint,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def create(
        self,
        *,
        json: Constraint,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def create(
        self,
        *,
        json: Constraint,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def create(
        self,
        *,
        json: Constraint,
        query: CreateQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResourceConstraintCreationResponse | T | Response | Model:
        """Create Resource Constraint.

        Creates a new _Resource Constraint_ from the given representation.
        :param json: The json request body.
        :type json: Constraint, optional
        :param query: URL Query parameters.
        :type query: CreateQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}
        if json is not None and validate_request:
            body_adapter = TypeAdapter(Constraint)
            json = body_adapter.validate_python(json)  # type: ignore # https://github.com/pydantic/pydantic/discussions/7094
        body_args["json"] = json

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(CreateQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "201": ResourceConstraintCreationResponse if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/resources/v1/resourceconstraints",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def delete(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> None: ...

    @overload
    async def delete(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def delete(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def delete(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> None: ...

    @overload
    async def delete(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def delete(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: DeleteQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> None | T | Response:
        """Remove Resource Constraint.

        Removes a _Resource Constraint_. Fails if the _Resource Constraint_ is already applied to a _Resource Type_.
        :param resource_constraint_id: _Resource_ Constraint id (required)
        :type resource_constraint_id: str
        :param query: URL Query parameters.
        :type query: DeleteQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "resourceConstraintId": str(resource_constraint_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(DeleteQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "204": None,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponse,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="DELETE",
            resource_path="/resources/v1/resourceconstraints/{resourceConstraintId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def get(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResourceConstraintWithIdEntity: ...

    @overload
    async def get(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def get(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def get(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def get(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def get(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResourceConstraintWithIdEntity | T | Response | Model:
        """Get Resource Constraint.

        Gets the definition or _JSON Schema_ representation of a _Resource Constraint_.
        :param resource_constraint_id: _Resource_ Constraint id (required)
        :type resource_constraint_id: str
        :param query: URL Query parameters.
        :type query: GetQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "resourceConstraintId": str(resource_constraint_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(GetQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": ResourceConstraintWithIdEntity if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/resources/v1/resourceconstraints/{resourceConstraintId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> List[ResourceConstraintWithIdEntity]: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> List[ResourceConstraintWithIdEntity] | T | Response | Model:
        """List Resource Constraints.

        Lists _Resource Constraints_ that fulfill the given criteria.
        :param query: URL Query parameters.
        :type query: ListQuery | QueryParamTypes, optional
        :param query['skip'] (dict) <br> query.skip (Query) : (Paging) items to skip in the listing
        :type query['skip']: int
        :param query['limit'] (dict) <br> query.limit (Query) : (Paging) maximal number of items returned
        :type query['limit']: int
        :param query['filter'] (dict) <br> query.filter (Query) : (Filter) fuzzy search on multiple fields.
        :type query['filter']: str
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(ListQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": List[ResourceConstraintWithIdEntity]
                if not select_path
                else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/resources/v1/resourceconstraints",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def replace(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        json: Constraint,
        query: ReplaceQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResourceConstraintWithIdEntity: ...

    @overload
    async def replace(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        json: Constraint,
        query: ReplaceQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def replace(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        json: Constraint,
        query: ReplaceQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def replace(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        json: Constraint,
        query: ReplaceQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def replace(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        json: Constraint,
        query: ReplaceQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def replace(
        self,
        resource_constraint_id: Annotated[
            str, Field(strict=True, description="_Resource_ Constraint id")
        ],
        *,
        json: Constraint,
        query: ReplaceQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResourceConstraintWithIdEntity | T | Response | Model:
        """Update Resource Constraint.

        Replaces the full definition of a _Resource Constraint_. Fails if the _Resource Constraint_ is already applied to a _Resource Type_ that has _Resources_ assigned to it.
        :param resource_constraint_id: _Resource_ Constraint id (required)
        :type resource_constraint_id: str
        :param json: The json request body.
        :type json: Constraint, optional
        :param query: URL Query parameters.
        :type query: ReplaceQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "resourceConstraintId": str(resource_constraint_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}
        if json is not None and validate_request:
            body_adapter = TypeAdapter(Constraint)
            json = body_adapter.validate_python(json)  # type: ignore # https://github.com/pydantic/pydantic/discussions/7094
        body_args["json"] = json

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(ReplaceQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": ResourceConstraintWithIdEntity if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponse,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="PUT",
            resource_path="/resources/v1/resourceconstraints/{resourceConstraintId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )
