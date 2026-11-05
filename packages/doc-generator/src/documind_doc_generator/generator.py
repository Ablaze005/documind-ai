from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DocumentationBundle:
    readme: str
    architecture: str
    summary: str


def generate_documentation(repository: str, language: str, framework: str) -> DocumentationBundle:
    readme = (
        f"# {repository}\n\n"
        "## Overview\n"
        f"This project is built with {language} and uses {framework}.\n\n"
        "## Getting started\n"
        "1. Install dependencies\n"
        "2. Configure environment variables\n"
        "3. Run the app locally\n"
    )
    architecture = (
        "## Architecture\n"
        "- API layer exposes core functionality\n"
        "- Repository analyzer inspects structure and metadata\n"
        "- AI engine generates human-friendly summaries\n"
        "- Documentation layer packages outputs for delivery\n"
    )
    summary = (
        f"{repository} is a {language}-based project using {framework}. "
        "The system combines static repository analysis with AI-assisted synthesis to generate useful docs."
    )
    return DocumentationBundle(readme=readme, architecture=architecture, summary=summary)
