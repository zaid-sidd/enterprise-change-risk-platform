def generate_approval_decision(risk_level):

    if risk_level == "Critical":

        return {
            "approval_status": "Rejected",
            "approval_reason":
                "Deployment risk exceeds acceptable operational thresholds."
        }

    elif risk_level == "High":

        return {
            "approval_status": "Conditional Approval",
            "approval_reason":
                "Deployment may proceed with enhanced monitoring and rollback readiness."
        }

    elif risk_level == "Medium":

        return {
            "approval_status": "Approved",
            "approval_reason":
                "Deployment risk is manageable with standard operational controls."
        }

    return {
        "approval_status": "Approved",
        "approval_reason":
            "Deployment risk is within acceptable limits."
    }