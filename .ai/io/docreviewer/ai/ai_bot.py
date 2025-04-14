# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

from abc import ABC, abstractmethod
from ai.line_comment import LineComment

class AiBot(ABC):
    
    __no_response = "No critical issues found"
    __problems = "spelling errors, grammar errors, punctuation errors, style issues, formatting issues, bad language, bad words, content issues, and style consistency with surrounding documentation"
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

2. Output Format:
   Provide comments in the following JSON format:
   {{
     "path": "{file_path}",
     "position": <position_in_diff>,
     "body": "<comment_text>"
   }}
   - The `position` should correspond to the line number in the diff where the issue occurs, as indicated by the `+` lines in the diff.

3. Guidelines:
   - Only comment on added lines (lines starting with `+` in the diff).
   - Ensure the `position` matches the line's position in the diff, not the original file.
   - Be concise and professional in your comments.

4. Example:
   For the following diff:
   ```
   @@ -1,3 +1,4 @@
   -Old line
   +New line with typo
   +Another new line
   ```
   If you identify a typo in "New line with typo", your output should be:
   ```json
   {{
     "path": "example/file.txt",
     "position": 1,
     "body": "Typo: 'typo' should be corrected."
   }}
   ```

DIFFS:

{diffs}

Full code from the file:

{code}
"""

    @abstractmethod
    def ai_request_diffs(self, code, diffs) -> str:
        pass

    @staticmethod
    def build_ask_text(code, diffs) -> str:
        return AiBot.__chat_gpt_ask_long.format(
            problems = AiBot.__problems,
            no_response = AiBot.__no_response,
            diffs = diffs,
            code = code,
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

        import json

        try:
            comments = json.loads(input)
            models = []

            for comment in comments:
                line = comment.get("position", 0)
                text = comment.get("body", "")
                if line > 0 and text:
                    models.append(LineComment(line=line, text=text))

            return models
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse AI response as JSON: {e}")
