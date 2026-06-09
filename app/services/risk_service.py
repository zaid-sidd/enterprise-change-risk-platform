import uuid

from app.services.history_service import retrieve_historical_changes
from app.services.advisory_service import generate_operational_advisory
from app.services.approval_service import generate_approval_decision


def calculate_change_risk(change):

    risk_score = 0

    risk_factors = []

    historical_matches = retrieve_historical_changes(
        change["service"],
        change["change_type"]
    )

    if change["deployment_window"] == "Peak Hours":
        risk_score += 30

        risk_factors.append(
            "Deployment scheduled during peak business hours"
        )

    if change["rollback_available"] is False:
        risk_score += 25

        risk_factors.append(
            "Rollback plan unavailable"
        )

    if change["affected_regions"] >= 3:
        risk_score += 20

        risk_factors.append(
            "Deployment affects multiple regions"
        )

    if change["recent_failures"] >= 2:
        risk_score += 25

        risk_factors.append(
            "Recent deployment failures detected"
        )

    if len(historical_matches) >= 1:
        risk_score += 15

        risk_factors.append(
            "Historical failure patterns found"
        )

    if risk_score >= 70:
        risk_level = "Critical"

    elif risk_score >= 40:
        risk_level = "High"

    elif risk_score >= 20:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    advisory = generate_operational_advisory(
        risk_level
    )

    approval = generate_approval_decision(
        risk_level
    )

    generated_change_id = change.get(
        "change_id",
        f"REQ-{str(uuid.uuid4())[:8]}"
    )

    return {
        "change_id": generated_change_id,

        "service": change["service"],

        "risk_score": risk_score,

        "calculated_risk": risk_level,

        "historical_matches_found": len(
            historical_matches
        ),

        "top_historical_match": (
            historical_matches[0]["change"][
                "failure_pattern"
            ]
            if historical_matches
            else None
        ),

        "risk_factors": risk_factors,

        "recommended_action":
            advisory["recommended_action"],

        "monitoring_level":
            advisory["monitoring_level"],

        "rollback_strategy":
            advisory["rollback_strategy"],

        "approval_status":
            approval["approval_status"],

        "approval_reason":
            approval["approval_reason"]
    }


def analyze_submitted_change(change_data):

    return calculate_change_risk(
        change_data
    )