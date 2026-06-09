def generate_executive_report(
    analysis_result
):

    return {
        "executive_summary":
            f"{analysis_result['service']} deployment classified as {analysis_result['calculated_risk']} risk.",

        "deployment_risk":
            analysis_result["calculated_risk"],

        "approval_status":
            analysis_result["approval_status"],

        "recommended_action":
            analysis_result["recommended_action"],

        "business_impact":
            "Potential customer-facing service disruption if deployment issues occur."
            if analysis_result["calculated_risk"] in ["Critical", "High"]
            else
            "Limited operational impact expected."
    }