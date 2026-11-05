from collections.abc import Callable

from app.services.repo_service import RepoAnalysisService


def get_repo_service() -> RepoAnalysisService:
    return RepoAnalysisService()


def get_service_provider() -> Callable[[], RepoAnalysisService]:
    return get_repo_service
