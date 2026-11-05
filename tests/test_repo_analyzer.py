import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for package_dir in [
    ROOT / "packages" / "repo-analyzer" / "src",
    ROOT / "packages" / "ai-engine" / "src",
]:
    if str(package_dir) not in sys.path:
        sys.path.insert(0, str(package_dir))

from documind_ai_engine.providers import ProviderFactory
from documind_repo_analyzer.analyzer import analyze_repository


def test_analyze_repository_metadata() -> None:
    metadata = analyze_repository("https://github.com/example/fastapi-project")
    assert metadata.repository == "fastapi-project"
    assert metadata.language == "Python"
    assert metadata.framework == "FastAPI"
    assert metadata.files > 0


def test_provider_factory() -> None:
    provider = ProviderFactory.create("ollama")
    response = provider.generate("summarize repo")
    assert "Ollama" in response
