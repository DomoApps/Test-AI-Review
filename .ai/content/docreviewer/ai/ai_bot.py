# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

from abc import ABC, abstractmethod
from ai.line_comment import LineComment
from log import Log


class AiBot(ABC):
    
    __no_response = "No critical issues found"
    __chat_gpt_ask_long = """
    Task:
    Review the following diff for issues and provide comments directly in the format required for posting to the GitHub API.

    Instructions:
    1. Focus Areas:
      Spelling errors
      Grammar issues
      Style consistency
      Clarity improvements
      Formatting issues
      Racism, sexism, and other forms of discrimination
      Inappropriate language or content

    2. Output Format:
      [
        {{
          "position": <position_in_diff>,
          "body": "<comment_text>"
        }}
      ]
      The position corresponds to the line number in the diff where the issue occurs, starting at 1, immediately after the @@ hunk header.

    3. Positioning Rules:
      Start counting positions at 1 for each hunk.

      Count all lines that appear after the @@ hunk header:
        Context lines (start with a space)
        Added lines (start with +)
        Removed lines (start with -)

      Do not count metadata lines:
        diff --git, index, ---, +++, and @@

      Only create comments on added lines (+).

      Reset the position count for each new hunk.

      Ensure that the position corresponds to the exact line in the diff where the issue occurs. Double-check the line content to avoid misalignment.

    4. Output Rules:
      Do not comment on removed (-) or context ( ) lines.
      Be concise and professional in your comments.
      Return a JSON array of comments.
      If no issues are found, return an empty array [].
      Do not include any markdown, explanations, or additional text.

    5. Example: Given this diff:

      @@ -1,3 +1,4 @@
      -Old line
      
      +New line with typo
      
      +Another new line

      A comment on "New line with typo" should be:
      [
        {{
          "position": 3,
          "body": "Typo: 'typo' should be corrected."
        }}
      ]

      A comment on "Another new line" should be:
      [
        {{
          "position": 5,
          "body": "Consider rephrasing for clarity."
        }}
      ]

      Here is the diff to review:
        {diffs}
    """

    @abstractmethod
    def ai_request_diffs(self, code, diffs) -> str:
        """
        Abstract method to request AI feedback on diffs.

        Args:
            code (str): The full code of the file.
            diffs (str): The git diffs to review.

        Returns:
            str: The AI's response.
        """
        pass

    @staticmethod
    def build_ask_text(code, diffs) -> str:
        return AiBot.__chat_gpt_ask_long.format(
            no_response=AiBot.__no_response,
            diffs=diffs,
            code=code
        )

    @staticmethod
    def is_no_issues_text(source: str) -> bool:
        target = AiBot.__no_response.replace(" ", "")
        source_no_spaces = source.replace(" ", "")
        return source_no_spaces.startswith(target)
    
    @staticmethod
    def split_ai_response(input) -> list[LineComment]:
        """
        Parses the AI response in JSON format and converts it into a list of LineComment objects.

        Args:
            input (str): The AI response in JSON format.

        Returns:
            list[LineComment]: A list of LineComment objects.
        """
        if input is None or not input.strip():
            return []

        if not isinstance(input, str):
            raise ValueError("Input must be a string.")

        import json
        import re

        try:
            comments = json.loads(input)
            return [
                LineComment(line=comment["position"], text=comment["body"])
                for comment in comments
                if "position" in comment and "body" in comment
            ]
        except json.JSONDecodeError as e:
            Log.print_red("JSON Decode error:", input)
            raise ValueError(f"Failed to parse AI response as JSON: {e}")
        except Exception as e:
            Log.print_red("AI bot exception:", input)
            raise ValueError(f"Unexpected error while parsing AI response: {e}")
