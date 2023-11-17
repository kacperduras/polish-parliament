from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proceeding import Proceeding
from ...types import Response


def _get_kwargs(
    term: int,
    id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/sejm/term{term}/proceedings/{id}".format(
            term=term,
            id=id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Proceeding]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Proceeding.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Proceeding]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Proceeding]:
    """Returns information about a proceeding

    Args:
        term (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Proceeding]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Proceeding]:
    """Returns information about a proceeding

    Args:
        term (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Proceeding
    """

    return sync_detailed(
        term=term,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Proceeding]:
    """Returns information about a proceeding

    Args:
        term (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Proceeding]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Proceeding]:
    """Returns information about a proceeding

    Args:
        term (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Proceeding
    """

    return (
        await asyncio_detailed(
            term=term,
            id=id,
            client=client,
        )
    ).parsed
