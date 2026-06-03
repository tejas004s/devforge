from typing import TypedDict


class WorkflowState(TypedDict):

    user_request: str

    requirements: str

    architecture: str

    backend_design: str

    frontend_design: str

    qa_review: str

    final_report: str

    execution_log: list

    current_agent: str

    status: str