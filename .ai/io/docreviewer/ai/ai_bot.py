# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

from abc import ABC, abstractmethod
from ai.line_comment import LineComment

class AiBot(ABC):
    
    __no_response = "No critical issues found"
    __problems = "spelling errors, grammar errors, punctuation errors, style issues, formatting issues, bad language, bad words, content issues, and style consistency with surrounding documentation"
    __chat_gpt_ask_long = """
Given the git diff output, which includes lines starting with + (added lines), could you describe briefly any {problems} for the added lines (lines starting with +)??

For line numbers, please treat them as relative to the entire diff output, not starting from 1. This means that line numbers should correspond to their actual position in the full diff output, counting the context lines (those starting with - or ) before reaching the first + line.

For each issue, output one line in this format:
line_number : cause effect

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
