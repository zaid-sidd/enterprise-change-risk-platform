historical_changes = [
    {
        "change_id": "HIST-2001",
        "service": "Payment Gateway",
        "failure_pattern": "Checkout failures after infrastructure update",
        "root_cause": "Load balancer timeout misconfiguration",
        "resolution": "Rollback load balancer changes and restart gateway services.",
        "rollback_required": True
    },
    {
        "change_id": "HIST-2002",
        "service": "Authentication Service",
        "failure_pattern": "User login failures after config deployment",
        "root_cause": "Expired authentication certificates",
        "resolution": "Renew certificates and redeploy authentication service.",
        "rollback_required": False
    },
    {
        "change_id": "HIST-2003",
        "service": "Monitoring Engine",
        "failure_pattern": "Alert processing delays after database migration",
        "root_cause": "Database indexing mismatch",
        "resolution": "Rebuild indexes and restart monitoring workers.",
        "rollback_required": False
    }
]