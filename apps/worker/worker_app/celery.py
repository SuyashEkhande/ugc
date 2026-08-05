from celery import Celery  # type: ignore[import-untyped]

celery_app = Celery(
    "ugc_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["worker_app.tasks"],
)
