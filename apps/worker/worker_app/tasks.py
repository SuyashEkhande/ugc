from worker_app.celery import celery_app


@celery_app.task(name="worker.echo")  # type: ignore[untyped-decorator]
def echo(message: str) -> str:
    """Placeholder task proving the worker can route and execute work."""
    return message
