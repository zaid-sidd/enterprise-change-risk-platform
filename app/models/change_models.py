from pydantic import BaseModel
from typing import Literal


class DeploymentChangeRequest(BaseModel):

    service: str

    change_type: str

    deployment_window: Literal[
        "Peak Hours",
        "Business Hours",
        "Maintenance Window"
    ]

    affected_regions: int

    rollback_available: bool

    recent_failures: int