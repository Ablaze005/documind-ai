from documind_doc_generator.generator import generate_documentation


class DocumentationService:
    @staticmethod
    def build_documentation(repository: str, language: str, framework: str) -> dict[str, str]:
        bundle = generate_documentation(repository, language, framework)
        return {
            "readme": bundle.readme,
            "architecture": bundle.architecture,
            "summary": bundle.summary,
        }
