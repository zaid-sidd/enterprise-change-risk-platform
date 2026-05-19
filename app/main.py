from fastapi import FastAPI

from app.datasets.sample_changes import deployment_changes

from app.services.risk_service import calculate_change_risk


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


@app.get(
    "/changes/risk-analysis",
    tags=["Risk Intelligence"],
    summary="Analyze deployment change risks",
    description="Calculates operational deployment risk scores for enterprise changes."
)
def analyze_change_risks():

    analyzed_changes = []

    for change in deployment_changes:

        analyzed_changes.append(
            calculate_change_risk(change)
        )

    return {
        "total_changes_analyzed": len(analyzed_changes),
        "risk_analysis": analyzed_changes
    }