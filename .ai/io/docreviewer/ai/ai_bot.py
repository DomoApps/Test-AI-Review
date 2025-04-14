# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

from abc import ABC, abstractmethod
from ai.line_comment import LineComment

class AiBot(ABC):
    
    __no_response = "No critical issues found"
    __problems = "spelling errors, grammar errors, punctuation errors, style issues, formatting issues, bad language, bad words, content issues, and style consistency with surrounding documentation"
    __chat_gpt_ask_long = """
Given the git diff output could you describe briefly any {problems} only for the added lines?

Start with the line number from the diff header, which specifies where the added lines begin in the original file (e.g., @@ -4,61 +4,66 @@).

For each issue, the correct line number should be calculated by considering the number of lines modified (added or removed).

For each issue, output one line in this format:
line_number : cause effect

Where:

line_number corresponds to the correct line number in the original file (calculated based on the starting line from the diff header).

cause effect describes the problem found in the line, e.g., "grammatical error - 'resource 's' should be 'resources'".

Do not include any introductions or explanations—just the list of issues, formatted as specified.

If there are no {problems} just say "{no_response}".

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
        if input is None or not input:
            return []
        
        lines = input.strip().split("\n")
        models = []

        for full_text in lines:
            number_str = ''
            number = 0
            full_text = full_text.strip()
            if len( full_text ) == 0:
                continue

            reading_number = True
            for char in full_text.strip():
                if reading_number:
                    if char.isdigit():
                        number_str += char
                    else:
                        break

            if number_str:
                number = int(number_str)

            models.append(LineComment(line = number, text = full_text))
        return models
