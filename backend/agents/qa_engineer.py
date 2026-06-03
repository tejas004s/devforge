from services.gemini_client import GeminiClient


class QAEngineerAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        prompt = f"""
You are a Senior QA Architect.

Requirements:

{state["requirements"]}

Architecture:

{state["architecture"]}

Backend Design:

{state["backend_design"]}

Frontend Design:

{state["frontend_design"]}

Review the project.

Generate:

1. Missing Features
2. Security Risks
3. Scalability Risks
4. Testing Strategy
5. UX Issues
6. Recommendations

Return clean markdown.
"""

        qa_review = self.llm.generate(prompt)

        state["qa_review"] = qa_review

        state["current_agent"] = "QA Engineer"

        state["execution_log"].append(
            "QA Engineer completed"
        )

        return state