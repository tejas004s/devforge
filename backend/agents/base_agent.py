from services.gemini_client import GeminiClient
import time


class BaseAgent:

    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.llm = GeminiClient()

    def generate(self, prompt):

        start_time = time.time()

        response = self.llm.generate(prompt)

        duration = round(
            time.time() - start_time,
            2
        )

        return response, duration