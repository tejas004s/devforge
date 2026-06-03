from pydantic import BaseModel


class GeneratePlanResponse(BaseModel):
    final_report: str
    execution_log: list[str]