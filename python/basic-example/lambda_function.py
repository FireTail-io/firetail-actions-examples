from dataclasses import dataclass, field
from typing import Literal

import requests
from dataclasses_json import DataClassJsonMixin

SUPPORTED_EVENT_CODES = Literal[
    "firetail:data-exposure-detected",
    "firetail:default-login-endpoint-detected",
    "firetail:cve-detected",
    "firetail:vulnerability-detected",
    "firetail:fuzzing-successful",
    "firetail:ssl-vulnerabilities-detected",
]

SUPPORTED_SEVERITY_LEVELS = Literal[
    "critical",
    "high",
    "medium",
    "low",
    "info",
]


@dataclass
class ActionCallbackObservationsContext:
    route: str | None = None
    method: str | None = None
    details: str | None = None
    url: str | None = None


@dataclass
class ActionCallBackObservation:
    code: SUPPORTED_EVENT_CODES
    severity: SUPPORTED_SEVERITY_LEVELS
    tags: list[str]
    context: ActionCallbackObservationsContext | dict = field(
        default_factory=lambda: {}
    )
    debounceKey: str | None = None


@dataclass
class ActionCallback(DataClassJsonMixin):
    observations: list[ActionCallBackObservation]


def callback_handler(event: dict, observations: ActionCallback):
    callback = event["callback_url"]
    response = requests.post(
        callback,
        json=observations.to_json(),
        headers={"Authorization": "Bearer " + event["jwt_token"]},
    )
    return response


def lambda_handler(event: dict, context: object):
    observations = ActionCallback(
        observations=[
            ActionCallBackObservation(
                code="firetail:data-exposure-detected",
                severity="high",
                tags=["data-exposure"],
                context=ActionCallbackObservationsContext(
                    route="/api/v1/users",
                    method="POST",
                    details="User data exposed in response",
                    url="https://api.example.com/api/v1/users",
                ),
                debounceKey="https://api.example.com/api/v1/users:POST",
            )
        ]
    )
    ft_response = callback_handler(event, observations=observations)
    if ft_response.status_code > 299:
        raise Exception(f"Failed to send observations to Firetail: {ft_response.text}")
