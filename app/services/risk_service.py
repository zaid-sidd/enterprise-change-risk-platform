from app.services.history_service import retrieve_historical_changes
from app.services.advisory_service import generate_operational_advisory


def calculate_change_risk(change):

    risk_score = 0

    historical_matches = retrieve_historical_changes(
        change["service"],
        change["change_type"]
    )

    if change["deployment_window"] == "Peak Hours":
        risk_score += 30

    if change["rollback_available"] is False:
        risk_score += 25

    if change["affected_regions"] >= 3:
        risk_score += 20

    if change["recent_failures"] >= 2:
        risk_score += 25

    if len(historical_matches) >= 1:
        risk_score += 15

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

    return {
        "change_id": change["change_id"],
        "service": change["service"],
        "risk_score": risk_score,
        "calculated_risk": risk_level,
        "historical_matches_found": len(historical_matches),

        "top_historical_match": (
            historical_matches[0]["change"]["failure_pattern"]
            if historical_matches else None
        ),

        "recommended_action": advisory["recommended_action"],

        "monitoring_level": advisory["monitoring_level"],

        "rollback_strategy": advisory["rollback_strategy"]
    }


def analyze_submitted_change(change_data):

    return calculate_change_risk(
        change_data
    )