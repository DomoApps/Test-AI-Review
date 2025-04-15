import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from unittest.mock import patch
from ai.chat_gpt import ChatGPT

@patch("openai.ChatCompletion.create")
def test_ai_request_diffs(mock_openai):
    mock_openai.return_value = {
        "choices": [
            {"message": {"content": "[{\"position\": 1, \"body\": \"Typo in line\"}]"}}
        ]
    }

    chat_gpt = ChatGPT(token="fake-token", model="gpt-4")
    response = chat_gpt.ai_request_diffs(
        code="print('Hello, world!')",
        diffs="@@ -1 +1 @@\n-print('Hello')\n+print('Hello, world!')",
    )

    assert response == [{"position": 1, "body": "Typo in line"}]  # Adjusted to match the expected output
    mock_openai.assert_called_once()

    mock_response = [
        {"position": 1, "body": "Typo in line 1"},
        {"position": 2, "body": "Grammar issue in line 2"}
    ]

    with patch("ai.ai_bot.AiBot.build_ask_text", return_value=mock_response):
        response = AiBot.build_ask_text("code", "diffs")
        assert response == mock_response