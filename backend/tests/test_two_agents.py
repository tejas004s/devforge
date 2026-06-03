from agents.project_manager import ProjectManagerAgent
from agents.architect import ArchitectAgent

state = {
    "user_request": "Build a hospital management system using React and FastAPI",
    "requirements": "",
    "architecture": "",
    "backend_design": "",
    "frontend_design": "",
    "qa_review": "",
    "final_report": "",
    "execution_log": [],
    "current_agent": ""
}

pm = ProjectManagerAgent()
architect = ArchitectAgent()

state = pm.run(state)

print("\nGenerating Architecture...\n")

state = architect.run(state)

print(state["architecture"])