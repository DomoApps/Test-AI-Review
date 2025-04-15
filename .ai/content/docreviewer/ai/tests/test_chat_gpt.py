import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from unittest.mock import patch, ANY
from ai.chat_gpt import ChatGPT
from ai.ai_bot import AiBot

@patch("openai.ChatCompletion.create")
def test_ai_request_diffs(mock_chat_completion_create):
    # Mock the OpenAI API response
    mock_chat_completion_create.return_value = {
        "choices": [
            {
                "message": {
                    "content": "Mocked AI response"
                }
            }
        ]
    }

    ai = ChatGPT(client=mock_chat_completion_create, model="gpt-4")
    code = "def example_function():\n    pass"
    diffs = "- def example_function():\n+ def example_function(param):\n    pass"

    # Simulate the response from the create method
    mock_chat_completion_create.create.return_value = {
        "choices": [
            {
                "message": {
                    "content": "Mocked AI response"
                }
            }
        ]
    }

    response = ai.ai_request_diffs(code=code, diffs=diffs)

    # Assert the mocked response is returned
    assert response == "Mocked AI response"

    # Ensure the OpenAI API was called with the correct parameters
    mock_chat_completion_create.create.assert_called_once_with(
        messages=ANY,
        model="gpt-4",
        stream=True
    )

    mock_response = [
        {"position": 1, "body": "Typo in line 1"},
        {"position": 2, "body": "Grammar issue in line 2"}
    ]

    with patch("ai.ai_bot.AiBot.build_ask_text", return_value=mock_response):
        response = AiBot.build_ask_text("code", "diffs")
        assert response == mock_response

@patch("openai.ChatCompletion.create")
def test_build_request_payload(mock_chat_completion_create):
    ai = ChatGPT(client=mock_chat_completion_create, model="gpt-4")
    code = "def example_function():\n    pass"
    diffs = "- def example_function():\n+ def example_function(param):\n    pass"

    payload = ai.build_request_payload(code, diffs)

    # Assert the payload structure
    assert payload["model"] == "gpt-4"
    assert payload["stream"] is True
    assert "messages" in payload
    assert payload["messages"][0]["role"] == "user"
    assert "content" in payload["messages"][0]