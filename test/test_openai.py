from unittest.mock import MagicMock

import pytest

from openai import OpenAI


@pytest.mark.asyncio
async def test_basic_request(mock_request: MagicMock):
    openai = OpenAI("sk-TEST")
    response = await openai._request("GET", "test")
    assert response == {}
    mock_request.assert_called_once_with(
        "GET",
        "https://api.openai.com/v1/test",
        headers={
            "Authorization": "Bearer sk-TEST",
        },
    )


@pytest.mark.asyncio
async def test_request_with_headers(mock_request: MagicMock):
    openai = OpenAI("sk-TEST")
    response = await openai._request("PUT", "test", headers={"Test": "test"})
    assert response == {}
    mock_request.assert_called_once_with(
        "PUT",
        "https://api.openai.com/v1/test",
        headers={
            "Authorization": "Bearer sk-TEST",
            "Test": "test",
        },
    )


@pytest.mark.asyncio
async def test_request_with_org(mock_request: MagicMock):
    openai = OpenAI("sk-TEST", "org-TEST")
    response = await openai._request("DELETE", "test")
    assert response == {}
    mock_request.assert_called_once_with(
        "DELETE",
        "https://api.openai.com/v1/test",
        headers={
            "Authorization": "Bearer sk-TEST",
            "OpenAI-Organization": "org-TEST",
        },
    )


@pytest.mark.asyncio
async def test_request_with_user(mock_request: MagicMock):
    openai = OpenAI("sk-TEST", "org-TEST", "myuser")
    response = await openai._request("POST", "test", json={"test": "test"})
    assert response == {}
    mock_request.assert_called_once_with(
        "POST",
        "https://api.openai.com/v1/test",
        headers={
            "Authorization": "Bearer sk-TEST",
            "OpenAI-Organization": "org-TEST",
        },
        json={"test": "test", "user": "myuser"},
    )


@pytest.mark.asyncio
async def test_request_with_user_override(mock_request: MagicMock):
    openai = OpenAI("sk-TEST", "org-TEST", "myuser")
    response = await openai._request(
        "POST", "test", json={"test": "test", "user": "myoverrideuser"}
    )
    assert response == {}
    mock_request.assert_called_once_with(
        "POST",
        "https://api.openai.com/v1/test",
        headers={
            "Authorization": "Bearer sk-TEST",
            "OpenAI-Organization": "org-TEST",
        },
        json={"test": "test", "user": "myoverrideuser"},
    )
