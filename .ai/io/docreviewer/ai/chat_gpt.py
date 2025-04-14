# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

import os
from openai import OpenAI
from ai.ai_bot import AiBot

class ChatGPT(AiBot):

    def __init__(self, token, model):
        self.__chat_gpt_model = model
        self.__client = OpenAI(api_key = token)

    def ai_request_diffs(self, code, diffs, file_path):
        """
        Requests AI feedback on diffs using the updated prompt.

        Args:
            code (str): The full code of the file.
            diffs (str): The git diffs to review.
            file_path (str): The path of the file being reviewed.

        Returns:
            str: The AI's response.
        """
        return self._chat_gpt_request(
            AiBot.build_ask_text(code=code, diffs=diffs, file_path=file_path)
        )
