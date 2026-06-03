from agents.base_agent import BaseAgent


class ProjectManagerAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "Project Manager"
        )

    def run(self, state):

        prompt = f"""
You are a Senior Product Manager.

Analyze:

{state["user_request"]}

Generate:
1. Requirements
2. User Stories
3. Risks
4. Success Criteria
"""

        requirements, duration = (
            self.generate(prompt)
        )

        state["requirements"] = requirements

        state["current_agent"] = (
            self.agent_name
        )

        state["execution_log"].append(
            {
                "agent": self.agent_name,
                "duration": duration
            }
        )

        return state