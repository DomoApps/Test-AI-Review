# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

from abc import ABC, abstractmethod
from ai.line_comment import LineComment

class AiBot(ABC):
    
    __no_response = "No critical issues found"
    __problems = """
    Spelling errors (e.g., common typos or incorrect word usage)

    Grammar errors (e.g., subject-verb agreement, incorrect phrasing)

    Punctuation errors (e.g., missing commas, incorrect punctuation usage)

    Style issues (e.g., informal language or non-professional tone)

    Formatting issues (e.g., improper line breaks, inconsistent use of headers or bullet points)

    Content issues (e.g., missing or incorrect information, misleading statements, foul language, racism, sexism, or other forms of discrimination)

    Clarity issues (e.g., confusing wording or ambiguity)

    Redundancy (e.g., repeated phrases or unnecessary wordiness)

    Tone issues (e.g., informal, colloquial, or overly casual language where more formal language is needed)"""
    __chat_gpt_ask_long = """
    You are an expert documentation reviewer.

    Given the git diff output from my company's documetation updates in Markdown, could you describe briefly any {problems}?

    Please focus only on the added lines (indicated by a leading +).

    Do not include any introductions or explanations—just the list of issues, formatted as specified.

    If there are no {problems} just say "{no_response}".

    For each issue, output one line in this format:
    line_number : cause effect.
    No extra spaces in the response.

    For calculating line_number:
    Use the line number from the diff header (e.g., +4 in @@ -4,61 +4,66 @@) to determine the starting line in the modified file.
    For each added line, increment the starting line number based on its order in the diff (e.g., the first added line corresponds to position +4, the second to position +5, and so on).

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
