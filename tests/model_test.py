"""Tests for Response model validation."""

from typing import Any, Dict
from datetime import datetime
from cloudstile.models import Response

ERROR_CODES = [
    "missing-input-response",
    "invalid-input-response",
    "bad-request",
    "timeout-or-duplicate",
    "internal-error",
]

DATA: Dict[str, Any] = {
    "success": False,
    "hostname": "example.com",
    "challenge_ts": datetime.now(),
    "action": "test",
    "error-codes": ERROR_CODES,
    "metadata": {"ephemeral_id": "ephemeral", "result_with_testing_key": True},
}


def test_validation() -> None:

    response = Response.model_validate(DATA)

    assert (
        response.success == DATA["success"]
    ), "Response success should match the input data"
    assert (
        response.hostname == DATA["hostname"]
    ), "Response hostname should match the input data"
    assert (
        response.timestamp == DATA["challenge_ts"]
    ), "Response timestamp should match the input data"
    assert (
        response.action == DATA["action"]
    ), "Response action should match the input data"
    assert (
        response.error_codes == ERROR_CODES
    ), "Response error codes should match the input data"
    assert (
        response.metadata.ephemeral_id == DATA["metadata"]["ephemeral_id"]
    ), "Response metadata ephemeral_id should match the input data"
    assert (
        response.metadata.result_with_testing_key
        == DATA["metadata"]["result_with_testing_key"]
    ), "Response metadata result_with_testing_key should match the input data"
