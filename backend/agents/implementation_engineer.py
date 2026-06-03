from services.gemini_client import GeminiClient


class ImplementationEngineerAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        prompt = f"""
You are a Senior Full Stack Engineer.

Requirements:

{state["requirements"]}

Architecture:

{state["architecture"]}

Generate:

# Backend

1. FastAPI Folder Structure
2. Database Schema
3. API Endpoints
4. Authentication Strategy
5. Deployment Notes

# Frontend

1. React Folder Structure
2. Pages
3. Components
4. State Management
5. User Flows
6. UI Recommendations

Return clean markdown.
"""

        implementation_design = self.llm.generate(
            prompt
        )

        state["backend_design"] = implementation_design

        state["frontend_design"] = implementation_design

        state["current_agent"] = (
            "Implementation Engineer"
        )

        state["execution_log"].append(
            "Implementation Engineer completed"
        )

        return state