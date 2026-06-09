def generate_operational_advisory(risk_level):

    if risk_level == "Critical":

        return {
            "recommended_action": "Delay deployment and perform change review.",
            "monitoring_level": "Enhanced",
            "rollback_strategy": "Mandatory"
        }

    elif risk_level == "High":

        return {
            "recommended_action": "Proceed with deployment under active monitoring.",
            "monitoring_level": "Elevated",
            "rollback_strategy": "Recommended"
        }

    elif risk_level == "Medium":

        return {
            "recommended_action": "Proceed during approved deployment window.",
            "monitoring_level": "Standard",
            "rollback_strategy": "Available"
        }

    return {
        "recommended_action": "Proceed normally.",
        "monitoring_level": "Standard",
        "rollback_strategy": "Optional"
    }