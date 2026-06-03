from pydantic import BaseModel


class RequirementsOutput(BaseModel):
    requirements: str

class ArchitectureOutput(BaseModel):
    architecture: str

class ArchitectureOutput(BaseModel):
    architecture: str

class FrontendOutput(BaseModel):
    frontend_design: str

class QAOutput(BaseModel):
    qa_review: str