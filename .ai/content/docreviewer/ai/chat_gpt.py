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

    def ai_request_diffs(self, code, diffs, file_path):
        """
        Sends a request to the OpenAI API to analyze diffs and return comments.

        Args:
            code (str): The full code of the file.
            diffs (str): The git diffs to review.
            file_path (str): The path of the file being reviewed.

        Returns:
            str: The AI's response.
        """
        prompt = AiBot.build_ask_text(code=code, diffs=diffs, file_path=file_path)
        return self._send_request(prompt)

    def _send_request(self, prompt):
        stream = self.__client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model = self.__chat_gpt_model,
            stream = True,
        )
        content = []
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content.append(chunk.choices[0].delta.content)
        return " ".join(content)