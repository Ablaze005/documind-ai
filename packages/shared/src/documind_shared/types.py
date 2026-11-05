from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryFacts:
    repository: str
    language: str
    framework: str
    files: int
    functions: int
    classes: int


SupportedProvider = str
