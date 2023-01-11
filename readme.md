# Ben's OpenAI API Wrapper for Python

Fully asynchronous Python client for the [OpenAI API], using [aiohttp].

[OpenAI API]: https://beta.openai.com/docs/api-reference
[aiohttp]: https://docs.aiohttp.org

## Quick Start

```python
import asyncio
from openai import OpenAI

openai = OpenAI(
    api_key="your openai api key",
    organization="optionally, your openai organization id",
    user="optionally, a user id for tracking purposes",
)
```

## License

[MIT](license.txt)
