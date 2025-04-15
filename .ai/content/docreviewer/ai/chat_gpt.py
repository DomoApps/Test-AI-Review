# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

import os
from openai import OpenAI
from ai.ai_bot import AiBot

class ChatGPT(AiBot):
    def __init__(self, client, model):
        """
        Initialize ChatGPT with a client and model.

        Args:
            client: An instance of the OpenAI client or a mock for testing.
            model: The model name to use for the OpenAI API.
        """
        self.__chat_gpt_model = model
        self.__client = client

    def build_request_payload(self, code, diffs):
        """
        Build the request payload for the OpenAI API.

        Args:
            code: The code to analyze.
            diffs: The diffs to include in the request.

        Returns:
            A dictionary representing the request payload.
        """
        return {
            "messages": [
                {
                    "role": "user",
                    "content": AiBot.build_ask_text(code=code, diffs=diffs),
                }
            ],
            "model": self.__chat_gpt_model,
            "stream": True,
        }

    def ai_request_diffs(self, code, diffs):
        payload = self.build_request_payload(code, diffs)
        stream = self.__client.chat.completions.create(payload)
        content = []
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content.append(chunk.choices[0].delta.content)
        return " ".join(content)