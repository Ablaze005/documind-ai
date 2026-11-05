from fastapi import APIRouter, Depends, status

from app.core.dependencies import get_repo_service
from app.schemas.analysis import RepositoryAnalysis, RepositoryRequest
from app.services.repo_service import RepoAnalysisService

router = APIRouter(prefix="/api/v1", tags=["repositories"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "documind-ai"}


@router.post("/repositories/analyze", response_model=RepositoryAnalysis, status_code=status.HTTP_200_OK)
def analyze_repository(
    payload: RepositoryRequest,
    service: RepoAnalysisService = Depends(get_repo_service),
) -> RepositoryAnalysis:
    return service.analyze_repository(payload.url)
