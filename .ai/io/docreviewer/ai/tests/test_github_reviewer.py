import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './')))

import pytest
from unittest.mock import patch, MagicMock
from io.docreviewer.github_reviewer import main

@patch("io.docreviewer.github_reviewer.Git")
@patch("io.docreviewer.github_reviewer.GitHub")
@patch("io.docreviewer.github_reviewer.ChatGPT")
def test_main(mock_chat_gpt, mock_github, mock_git):
    # Mock Git methods
    mock_git.get_remote_name.return_value = "origin"
    mock_git.get_diff_files.return_value = ["example.py"]
    mock_git.get_diff_in_file.return_value = "@@ -1 +1 @@\n-print('Hello')\n+print('Hello, world!')"
    mock_git.get_last_commit_sha.return_value = "abc123"

    # Mock GitHub methods
    mock_github_instance = MagicMock()
    mock_github.return_value = mock_github_instance

    # Mock ChatGPT methods
    mock_chat_gpt_instance = MagicMock()
    mock_chat_gpt_instance.ai_request_diffs.return_value = "[{\"position\": 1, \"body\": \"Typo in line\"}]"
    mock_chat_gpt.return_value = mock_chat_gpt_instance

    # Run the main function
    main()

    # Assertions
    mock_git.get_remote_name.assert_called_once()
    mock_git.get_diff_files.assert_called_once()
    mock_git.get_diff_in_file.assert_called_once_with(
        remote_name="origin", head_ref=pytest.ANY, base_ref=pytest.ANY, file_path="example.py"
    )
    mock_chat_gpt_instance.ai_request_diffs.assert_called_once()
    mock_github_instance.post_comment_to_line.assert_called_once_with(
        text="Typo in line",
        commit_id="abc123",
        file_path="example.py",
        position=1
    )