"""OpenAI API client"""

from typing import Optional

import aiohttp


class OpenAI:
    """OpenAI API client"""

    api_key: str
    """OpenAI API key"""

    organization_id: Optional[str]
    """OpenAI organization ID"""

    user: Optional[str]
    """End-user ID"""

    def __init__(
        self,
        api_key: str,
        organization_id: Optional[str] = None,
        user: Optional[str] = None,
    ):
        """Initialize the OpenAI API wrapper class.

        :param api_key: OpenAI API key
        :param organization_id: Optional OpenAI organization ID
        :param user: Optional End-user ID

        Documentation:
        https://beta.openai.com/docs/api-reference/authentication
        https://beta.openai.com/docs/guides/safety-best-practices/end-user-ids
        """

        self.api_key = api_key
        self.organization_id = organization_id
        self.user = user

    async def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        async with aiohttp.ClientSession() as session:
            url = f"https://api.openai.com/v1/{endpoint}"

            # Set headers
            headers = kwargs.get("headers", {})
            headers["Authorization"] = f"Bearer {self.api_key}"
            if self.organization_id:
                headers["OpenAI-Organization"] = self.organization_id
            kwargs["headers"] = headers

            # Set json data
            if "json" in kwargs and "user" not in kwargs["json"] and self.user:
                kwargs["json"]["user"] = self.user

            async with session.request(method, url, **kwargs) as response:
                return await response.json()
