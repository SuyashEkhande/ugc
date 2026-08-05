from fastapi import FastAPI

from app.schemas import HealthResponse, ProjectListResponse

app = FastAPI(title="AI Creative Studio API", version="0.1.0")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse()


@app.get("/projects", response_model=ProjectListResponse)
def list_projects() -> ProjectListResponse:
    return ProjectListResponse(items=[])
