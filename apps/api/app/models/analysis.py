from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryMetrics:
    repository: str
    language: str
    framework: str
    files: int
    functions: int
    classes: int
    summary: str
