# graph/nodes.py
from agents.project_manager import ProjectManagerAgent
from agents.architect import ArchitectAgent
from agents.implementation_engineer import ImplementationEngineerAgent
from agents.qa_engineer import QAEngineerAgent
from agents.report_generator import ReportGeneratorAgent

# Initialize agents
pm = ProjectManagerAgent()
architect = ArchitectAgent()
implement = ImplementationEngineerAgent()
qa = QAEngineerAgent()
report = ReportGeneratorAgent()


def project_manager_node(state):
    return pm.run(state)


def architect_node(state):
    return architect.run(state)


def implement_node(state):
    # This single node runs the consolidated implementation engineer
    return implement.run(state)


def qa_node(state):
    return qa.run(state)


def report_node(state):
    return report.run(state)