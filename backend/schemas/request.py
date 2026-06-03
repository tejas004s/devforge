from pydantic import BaseModel


class GeneratePlanRequest(BaseModel):
    prompt: str