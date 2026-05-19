deployment_changes = [
    {
        "change_id": "CHG-1001",
        "service": "Payment Gateway",
        "change_type": "Infrastructure Update",
        "deployment_window": "Peak Hours",
        "affected_regions": 3,
        "rollback_available": False,
        "recent_failures": 2,
        "risk_level": "High"
    },
    {
        "change_id": "CHG-1002",
        "service": "Authentication Service",
        "change_type": "Configuration Update",
        "deployment_window": "Maintenance Window",
        "affected_regions": 1,
        "rollback_available": True,
        "recent_failures": 0,
        "risk_level": "Low"
    },
    {
        "change_id": "CHG-1003",
        "service": "Monitoring Engine",
        "change_type": "Database Migration",
        "deployment_window": "Business Hours",
        "affected_regions": 2,
        "rollback_available": False,
        "recent_failures": 1,
        "risk_level": "Medium"
    }
]