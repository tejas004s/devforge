from fastapi import APIRouter

from services.workflow_service import (
    WorkflowService
)

from schemas.request import (
    GeneratePlanRequest
)

router = APIRouter()


@router.post("/generate-plan")
def generate_plan(
    request: GeneratePlanRequest
):

    result = WorkflowService.run(
        request.prompt
    )

    return {
        "final_report":
            result["final_report"],

        "execution_log":
            result["execution_log"]
    }w