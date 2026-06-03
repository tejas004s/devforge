from graph.workflow import app


class WorkflowService:

    @staticmethod
    def run(prompt):

        state = {
            "user_request": prompt,
            "requirements": "",
            "architecture": "",
            "backend_design": "",
            "frontend_design": "",
            "qa_review": "",
            "final_report": "",
            "execution_log": [],
            "current_agent": "",
            "status": "running"
        }

        result = app.invoke(state)

        return result