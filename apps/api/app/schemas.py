from enum import Enum
from typing import Literal

from pydantic import BaseModel


class ProjectStatus(str, Enum):
    draft = "draft"
    interviewing = "interviewing"
    researching = "researching"
    planning = "planning"
    awaiting_approval = "awaiting_approval"
    generating = "generating"
    ready = "ready"
    publishing = "publishing"
    published = "published"
    failed = "failed"


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"


class ProjectSummary(BaseModel):
    id: int
    title: str
    status: ProjectStatus


class ProjectListResponse(BaseModel):
    items: list[ProjectSummary]
