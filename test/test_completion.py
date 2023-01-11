# from datetime import datetime
# import pytest


# def current_milli_time():
#     return int(datetime.now().timestamp() * 1000)


# def mock_completion():
#     return {
#         "id": "cmpl-TEST",
#         "object": "text_completion",
#         "created": current_milli_time(),
#         "model": "text-davinci-003",
#         "choices": [
#             {
#                 "text": "test",
#                 "index": 0,
#                 "logprobs": None,
#                 "finish_reason": "length",
#             }
#         ],
#         "usage": {
#             "text_characters": 0,
#             "tokens": 0,
#             "model": "text-davinci-003",
#         },
#     }


# @pytest.mark.asyncio
# async def test_completion(mocker: MockFixture):
#     mock_request = mocker.patch(
#         "aiohttp.ClientSession.request",
#         return_value=MockRequest(data=mock_completion()),
#     )
#     openai = OpenAI("sk-TEST")
#     response = await openai.create_completion(
#         "text-davinci-003",
#         prompt="test",
#     )
