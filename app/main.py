from fastapi import FastAPI


app = FastAPI(title="VoIP Python Lab API")


@app.get("/health")
def health_check() -> dict:
    """Simple health check endpoint."""
    return {"status": "ok"}
