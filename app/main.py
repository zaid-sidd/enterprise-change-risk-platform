from fastapi import FastAPI

from app.datasets.sample_changes import deployment_changes


app = FastAPI(
    title="Enterprise Change Risk Platform",
    description="""
AI-assisted operational platform for deployment risk analysis and enterprise change intelligence workflows.
""",
    version="1.0.0"
)


@app.get(
    "/",
    tags=["System"]
)
def home():

    return {
        "message": "Enterprise Change Risk Platform is running"
    }


@app.get(
    "/changes",
    tags=["Change Management"],
    summary="Retrieve deployment changes",
    description="Fetches enterprise deployment changes and operational risk metadata."
)
def get_changes():

    return {
        "total_changes": len(deployment_changes),
        "changes": deployment_changes
    }