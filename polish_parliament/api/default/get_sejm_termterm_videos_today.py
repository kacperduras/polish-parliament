from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.video import Video
from ...types import Response


def _get_kwargs(
    term: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/sejm/term{term}/videos/today".format(
            term=term,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[List["Video"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Video.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[List["Video"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["Video"]]:
    """Returns a list of video transmissions for today

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Video']]
    """

    kwargs = _get_kwargs(
        term=term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["Video"]]:
    """Returns a list of video transmissions for today

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Video']
    """

    return sync_detailed(
        term=term,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["Video"]]:
    """Returns a list of video transmissions for today

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Video']]
    """

    kwargs = _get_kwargs(
        term=term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["Video"]]:
    """Returns a list of video transmissions for today

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Video']
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
        )
    ).parsed
