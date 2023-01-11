import pytest
from pytest_mock import MockFixture


class MockRequest:
    status = 200
    data = {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def json(self):
        return self.data


@pytest.fixture
def mock_request(mocker):
    return mocker.patch("aiohttp.ClientSession.request", return_value=MockRequest())
