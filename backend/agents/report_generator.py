from services.gemini_client import GeminiClient


class ReportGeneratorAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        prompt = f"""
You are a Senior Technical Program Manager.

Create a final consolidated project plan.

Requirements:
{state["requirements"]}

Architecture:
{state["architecture"]}

Backend Design:
{state["backend_design"]}

Frontend Design:
{state["frontend_design"]}

QA Review:
{state["qa_review"]}

Generate:

1. Executive Summary
2. Final Architecture
3. Backend Plan
4. Frontend Plan
5. Risks
6. Development Roadmap
7. Deployment Strategy

Return clean markdown.
"""

        report = self.llm.generate(prompt)

        state["final_report"] = report

        state["current_agent"] = "Report Generator"

        state["execution_log"].append(
            "Report Generator completed"
        )

        return state