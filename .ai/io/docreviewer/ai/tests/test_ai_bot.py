import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from ai.ai_bot import AiBot
from ai.line_comment import LineComment

def test_split_ai_response():
    input_json = """[
        {"position": 1, "body": "Typo in line 1"},
        {"position": 2, "body": "Grammar issue in line 2"}
    ]"""

    comments = AiBot.split_ai_response(input_json)

    assert len(comments) == 2
    assert comments[0] == LineComment(line=1, text="Typo in line 1")
    assert comments[1] == LineComment(line=2, text="Grammar issue in line 2")

def test_split_ai_response_malformed_json():
    input_json = "{malformed_json}"

    with pytest.raises(ValueError, match="Failed to parse AI response as JSON"):
        AiBot.split_ai_response(input_json)