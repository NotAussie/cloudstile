"""Asynchronous implementation of the Cloudflare Turnstile API."""

from typing import Optional
from .base import BaseTurnstile
from .models import Response
import httpx


class AsyncTurnstile(BaseTurnstile):
    """
    Asynchronous implementation of the Cloudflare Turnstile API.

    This class extends the :class:`BaseTurnstile` class to provide an asynchronous
    method for validating Turnstile tokens using the Cloudflare Turnstile
    service.

    Inherits from:
        :class:`BaseTurnstile`: The abstract base class for Turnstile validation.
    """

    async def validate(  # pylint: disable=invalid-overridden-method
        self,
        token: str,
        ip: Optional[str] = None,
        idempotency_key: Optional[str] = None,
    ) -> Response:
        """
        Asynchronously validate a Turnstile token against the Cloudflare service.

        Sends a POST request to the Turnstile validation endpoint with the
        necessary parameters and returns the validation response.

        :param token: The Turnstile token to validate.
        :type token: str
        :param ip: The IP address of the user submitting the token.
        :type ip: Optional[str]
        :param idempotency_key: A unique key to ensure idempotent validation requests.
        :type idempotency_key: Optional[str]
        :return: The response from the Turnstile validation service.
        :rtype: :class:`Response`
        :raises httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        :raises httpx.RequestError: If there is an error making the request.
        """
        async with httpx.AsyncClient() as client:

            data = {
                "secret": self._secret,
                "response": token,
            }

            if ip:
                data["remoteip"] = ip

            if idempotency_key:
                data["idempotency_key"] = idempotency_key

            resp = await client.post(self._validate_route, json=data)
            resp.raise_for_status()

            response = Response.model_validate(resp.json())

            return response
