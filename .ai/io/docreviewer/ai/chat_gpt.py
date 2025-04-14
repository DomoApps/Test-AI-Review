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
        openai.api_key = token

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
        """
        Sends a prompt to the OpenAI API and returns the response.

        Args:
            prompt (str): The prompt to send to the OpenAI API.

        Returns:
            str: The response from the OpenAI API.
        """
        import openai

        try:
            response = openai.ChatCompletion.create(
                model=self.__chat_gpt_model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response['choices'][0]['message']['content']
        except openai.error.OpenAIError as e:
            raise RuntimeError(f"Failed to communicate with ChatGPT API: {e}")