from agents.project_manager import ProjectManagerAgent

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

agent = ProjectManagerAgent()

result = agent.run(state)

print("\n===== REQUIREMENTS DOCUMENT =====\n")

print(result["requirements"])

print("\n===============================\n")

print(result["requirements"])