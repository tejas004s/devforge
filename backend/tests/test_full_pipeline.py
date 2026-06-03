# main_runner.py (or whatever your sequential test script is named)
from agents.project_manager import ProjectManagerAgent
from agents.architect import ArchitectAgent
# FIX: Import the new consolidated ImplementationEngineerAgent
from agents.implementation_engineer import ImplementationEngineerAgent
from agents.qa_engineer import QAEngineerAgent

# Initialize the shared state dictionary
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

# Instantiate the active agents
pm = ProjectManagerAgent()
architect = ArchitectAgent()
# FIX: Instantiate the fullstack engineer
implement = ImplementationEngineerAgent()
qa = QAEngineerAgent()

print("Running Project Manager...")
state = pm.run(state)

print("Running Architect...")
state = architect.run(state)

# FIX: Run the single implementation engine step
print("Running Implementation Engineer (Full Stack)...")
state = implement.run(state)

print("Running QA Engineer...")
state = qa.run(state)

print("\n==========================")
print("EXECUTION LOG")
print("==========================")
for item in state["execution_log"]:
    print(item)

print("\n==========================")
print("QA REVIEW")
print("==========================")
print(state["qa_review"])