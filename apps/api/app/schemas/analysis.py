from pydantic import BaseModel, Field


class RepositoryRequest(BaseModel):
    url: str = Field(..., description="GitHub repository URL to analyze")


class RepositoryAnalysis(BaseModel):
    repository: str
    language: str
    framework: str
    files: int
    functions: int
    classes: int
    summary: str
