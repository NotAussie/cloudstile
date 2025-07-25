import pytest
from cloudstile import AsyncTurnstile, Response

TEST_RESPONSE = "XXXX.DUMMY.TOKEN.XXXX"
ALWAYS_PASS = "1x0000000000000000000000000000000AA"
ALWAYS_FAIL = "2x0000000000000000000000000000000AA"
ALWAYS_SPENT = "3x0000000000000000000000000000000AA"


@pytest.mark.asyncio
async def test_async_pass() -> None:

    turnstile = AsyncTurnstile(ALWAYS_PASS)

    response = await turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == True, "Response was not successful"


@pytest.mark.asyncio
async def test_async_ip() -> None:

    turnstile = AsyncTurnstile(ALWAYS_PASS)

    response = await turnstile.validate(TEST_RESPONSE, "192.168.1.1")

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == True, "Response was not successful"


@pytest.mark.asyncio
async def test_async_idempotency() -> None:

    turnstile = AsyncTurnstile(ALWAYS_PASS)

    response = await turnstile.validate(TEST_RESPONSE, idempotency_key="abc123456789")

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == True, "Response was not successful"


@pytest.mark.asyncio
async def test_async_fail() -> None:

    turnstile = AsyncTurnstile(ALWAYS_FAIL)

    response = await turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == False, "Response was successful"


@pytest.mark.asyncio
async def test_async_spent() -> None:

    turnstile = AsyncTurnstile(ALWAYS_SPENT)

    response = await turnstile.validate(TEST_RESPONSE)

    assert isinstance(response, Response), "Response was not a Response object"
    assert response.success == False, "Response was successful"
    assert "timeout-or-duplicate" in response.error_codes
