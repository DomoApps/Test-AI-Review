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
      - Spelling errors
      - Grammar issues
      - Style consistency
      - Clarity improvements
      - Formatting issues
      - Racism, sexism, and other forms of discrimination
      - Inappropriate language
      - Inappropriate content

    2. Output Format:
      Provide comments in the following JSON format:
      [
        {{
          "position": <position_in_diff>,
          "body": "<comment_text>"
        }}
      ]
      - The `position` should correspond to the line number in the diff where the issue occurs, as indicated by the `+` lines in the diff.

    3. Guidelines:
      - Only comment on added lines (lines starting with `+` in the diff).
      - Count all lines above in the diff including those beginning with '+' '-' and a blank space to determine the `position`.
      - The first line in the diff is `position` 1, the second line is `position` 2, and so on.
      - Be concise and professional in your comments.
      - Return only valid JSON with no markdown modifiers, wrappers, or additional text.

    4. Example:
      For the following diff:

      @@ -1,3 +1,4 @@
       
      -Old line
       
      +New line with typo
       
      +Another new line

      If you identify a typo in "New line with typo", your output should be:
      [
        {{
          "position": 4,
          "body": "Typo: 'typo' should be corrected."
        }}
      ]

      If you identify an issue in "Another new line", your output should be:
      [
        {{
          "position": 6,
          "body": "Consider rephrasing for clarity."
        }}
      ]

      If no issues are found, respond with and empty array

    DIFFS:

    {diffs}

    Full code from the file:

    {code}

    Notes:
    - The `position` is relative to the added lines in the diff (lines starting with `+`).
    - Removed lines (lines starting with `-`) and context lines should not be included in the `position` calculation.
    - If a hunk contains multiple added lines, count only the `+` lines to determine the `position`.
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
            Log.print_red("Responses where not parsed:", input)
            raise ValueError(f"Failed to parse AI response as JSON: {e}")
        except Exception as e:
            Log.print_red("Responses where not parsed:", input)
            raise ValueError(f"Unexpected error while parsing AI response: {e}")
