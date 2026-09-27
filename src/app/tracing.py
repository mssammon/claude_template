"""OpenTelemetry tracing to Phoenix. Call setup_tracing() once, before building any graph."""

from phoenix.otel import register

from app.config import settings

_configured = False


def setup_tracing() -> None:
    global _configured
    if _configured:
        return
    register(
        project_name=settings.phoenix_project_name or None,  # None -> Phoenix "default" project
        endpoint=settings.phoenix_collector_endpoint or None,  # None -> http://localhost:6006
        auto_instrument=True,  # turns on every installed OpenInference instrumentor
    )
    _configured = True
