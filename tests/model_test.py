import pytest
from datetime import datetime
from cloudstile.models import Response, CloudStileError, HTTPError

ERROR_CODES = [
    "missing-input-response",
    "invalid-input-response",
    "bad-request",
    "timeout-or-duplicate",
    "internal-error",
]
DATA = {
    "success": False,
    "hostname": "example.com",
    "challenge_ts": datetime.now(),
    "action": "test",
    "error-codes": ERROR_CODES,
    "metadata": {"ephemeral_id": "ephemeral", "result_with_testing_key": True},
}


def test_validation():

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


def test_cloud_stile_error():
    message = "Test error message"
    with pytest.raises(CloudStileError, match=message):
        raise CloudStileError(message)


def test_http_error():
    status_code = 404
    message = "Not Found"
    with pytest.raises(HTTPError, match=message):
        raise HTTPError(status_code, message)

    error_instance = HTTPError(status_code, message)
    assert (
        error_instance.status_code == status_code
    ), "HTTPError status_code should match the input"
    assert error_instance.message == message, "HTTPError message should match the input"
