# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

import os
from openai import OpenAI
from ai.ai_bot import AiBot

class ChatGPT(AiBot):
    def __init__(self, token, model):
        """
        Initializes the ChatGPT class with the OpenAI API token and model.

        Args:
            token (str): The OpenAI API token.
            model (str): The OpenAI model to use (e.g., 'gpt-4').
        """
        import openai
        self.__chat_gpt_model = model
        self.__client = OpenAI(api_key = token)
        self.__client.ChatCompletion = openai.ChatCompletion

    def ai_request_diffs(self, code, diffs):
        """
        Sends a request to the OpenAI API to analyze diffs and return comments.

        Args:
            code (str): The full code of the file.
            diffs (str): The git diffs to review.
            file_path (str): The path of the file being reviewed.

        Returns:
            str: The AI's response.
        """
        prompt = AiBot.build_ask_text(code=code, diffs=diffs)
        return self._send_request(prompt)

    def _send_request(self, prompt):
        response = self.__client.ChatCompletion.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.__chat_gpt_model
        )
        return response["choices"][0]["message"]["content"]