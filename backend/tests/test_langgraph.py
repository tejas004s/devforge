from graph.workflow import app

state = {
    "user_request":
    "Build a hospital management system using React and FastAPI",

    "requirements": "",
    "architecture": "",
    "backend_design": "",
    "frontend_design": "",
    "qa_review": "",
    "final_report": "",

    "execution_log": [],
    "current_agent": ""
}

result = app.invoke(state)

print("\n========================")
print("EXECUTION LOG")
print("========================")

for item in result["execution_log"]:
    print(item)

print("\n========================")
print("FINAL REPORT")
print("========================")

print(result["final_report"])