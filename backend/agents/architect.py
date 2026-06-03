from services.gemini_client import GeminiClient


class ArchitectAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        prompt = f"""
You are a Principal Software Architect.

Requirements Document:

{state["requirements"]}

Generate:

1. High Level Architecture
2. System Components
3. Database Design
4. API Design Strategy
5. Deployment Architecture
6. Security Considerations

Return clean markdown.
"""

        architecture = self.llm.generate(prompt)

        state["architecture"] = architecture

        state["current_agent"] = "Architect"

        state["execution_log"].append(
            "Architect completed"
        )

        return state