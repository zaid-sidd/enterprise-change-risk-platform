from fastapi import FastAPI

from app.datasets.sample_changes import deployment_changes

from app.services.risk_service import calculate_change_risk

from app.services.history_service import retrieve_historical_changes

from app.models.change_models import DeploymentChangeRequest

from app.services.risk_service import (
    analyze_submitted_change
)


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

@app.post(
    "/changes/analyze",
    tags=["Risk Intelligence"],
    summary="Analyze submitted deployment change",
    description="Accepts deployment change requests and generates operational risk intelligence."
)
def analyze_change(
    change: DeploymentChangeRequest
):

    result = analyze_submitted_change(
        change.model_dump()
    )

    return {
        "analysis": result
    }

@app.get(
    "/changes/history/{service_name}",
    tags=["Historical Intelligence"],
    summary="Retrieve historical deployment failures",
    description="Fetches historical deployment failures and operational resolutions for enterprise services."
)
def get_historical_changes(service_name: str):

    historical_matches = retrieve_historical_changes(
        service_name
    )

    return {
        "service": service_name,
        "historical_matches_found": len(historical_matches),
        "historical_changes": historical_matches
    }