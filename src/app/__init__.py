def main() -> None:
    from app.tracing import setup_tracing

    setup_tracing()
    print("Hello from agent-template!")
