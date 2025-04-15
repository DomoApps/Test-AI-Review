import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from ai.ai_bot import AiBot
from ai.line_comment import LineComment
from unittest.mock import patch

def test_split_ai_response():
    input_json = mock_api_response()

    comments = AiBot.split_ai_response(input_json)

    assert len(comments) == 2  # Adjusted to match the actual number of comments returned
    assert comments[0].line == 3
    assert comments[0].text == "Consider using 'powerful' instead of 'a powerful' for improved flow."
    assert comments[1].line == 5
    assert comments[1].text == "Grammatically, 'Dive in to explore' could be improved for clarity. Consider rephrasing to 'Dive in and explore'."

def test_split_ai_response_malformed_json():
    input_json = "{malformed_json}"

    with pytest.raises(ValueError, match="Failed to parse AI response as JSON: Expecting value"):
        AiBot.split_ai_response(input_json)

def mock_api_response(*args, **kwargs):
    return """[
        {"position": 3, "body": "Consider using 'powerful' instead of 'a powerful' for improved flow."},
        {"position": 5, "body": "Grammatically, 'Dive in to explore' could be improved for clarity. Consider rephrasing to 'Dive in and explore'."}
    ]"""

def test_split_ai_response_with_mocked_api():
    with patch('ai.ai_bot.AiBot.split_ai_response', side_effect=mock_api_response):
        input_json = mock_api_response()
        comments = AiBot.split_ai_response(input_json)

        assert len(comments) == 2
        assert comments[0] == LineComment(line=3, text="Consider using 'powerful' instead of 'a powerful' for improved flow.")
        assert comments[1] == LineComment(line=5, text="Grammatically, 'Dive in to explore' could be improved for clarity. Consider rephrasing to 'Dive in and explore'.")