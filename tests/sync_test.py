"""Synchronous tests for the Cloudflare Turnstile API integration."""

from cloudstile import SyncTurnstile, Response

TEST_RESPONSE = "XXXX.DUMMY.TOKEN.XXXX"
ALWAYS_PASS = "1x0000000000000000000000000000000AA"
ALWAYS_FAIL = "2x0000000000000000000000000000000AA"
ALWAYS_SPENT = "3x0000000000000000000000000000000AA"


def test_sync_ip() -> None:

    turnstile = SyncTurnstile(ALWAYS_PASS)

    response = turnstile.validate(TEST_RESPONSE, "192.168.1.1")

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success is True, "Response was not successful"


def test_sync_idempotency() -> None:

    turnstile = SyncTurnstile(ALWAYS_PASS)

    response = turnstile.validate(TEST_RESPONSE, idempotency_key="abc123456789")

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success is True, "Response was not successful"


def test_sync_pass() -> None:

    turnstile = SyncTurnstile(ALWAYS_PASS)

    response = turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success is True, "Response was not successful"


def test_sync_fail() -> None:

    turnstile = SyncTurnstile(ALWAYS_FAIL)

    response = turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success is False, "Response was successful"


def test_sync_spent() -> None:

    turnstile = SyncTurnstile(ALWAYS_SPENT)

    response = turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success is False, "Response was successful"
    assert "timeout-or-duplicate" in response.error_codes
