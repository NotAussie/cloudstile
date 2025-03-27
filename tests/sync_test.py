import pytest
from cloudstile import SyncTurnstile, Response

TEST_RESPONSE = "XXXX.DUMMY.TOKEN.XXXX"
ALWAYS_PASS = "1x0000000000000000000000000000000AA"
ALWAYS_FAIL = "2x0000000000000000000000000000000AA"
ALWAYS_SPENT = "3x0000000000000000000000000000000AA"


def test_async_ip():

    turnstile = SyncTurnstile(ALWAYS_PASS)

    response = turnstile.validate(TEST_RESPONSE, "192.168.1.1")

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == True, "Response was not successful"


def test_async_idempotency():

    turnstile = SyncTurnstile(ALWAYS_PASS)

    response = turnstile.validate(TEST_RESPONSE, idempotency_key="abc123456789")

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == True, "Response was not successful"


def test_sync_pass():

    turnstile = SyncTurnstile(ALWAYS_PASS)

    response = turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == True, "Response was not successful"


def test_sync_fail():

    turnstile = SyncTurnstile(ALWAYS_FAIL)

    response = turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == False, "Response was successful"


def test_sync_spent():

    turnstile = SyncTurnstile(ALWAYS_SPENT)

    response = turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == False, "Response was successful"
    assert "timeout-or-duplicate" in response.error_codes
