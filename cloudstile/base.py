"""Abstract base class for implementing Cloudflare Turnstile interactions."""

from abc import ABC, abstractmethod
import logging
from .models import Response
from typing import Optional, Union, Coroutine


class BaseTurnstile(ABC):
    """
    Abstract base class for implementing Cloudflare Turnstile validation.

    This class provides the foundational structure for creating a Turnstile
    validator, including the necessary configuration for secret management
    and idempotency.

    Attributes
    ----------
    _secret : str
        The Cloudflare Turnstile secret used for validation.
    _validate_route : str
        The URL endpoint for Turnstile validation.
    """

    def __init__(self, secret: str):
        """
        Initialize the Turnstile client instance.

        Parameters
        ----------
        secret : str
            Cloudflare Turnstile secret.
        """
        self._secret = secret

        self._validate_route = (
            "https://challenges.cloudflare.com/turnstile/v0/siteverify"
        )

        self.logger = logging.getLogger("cloudstile")

    @abstractmethod
    def validate(
        self,
        token: str,
        ip: Optional[str] = None,
        idempotency_key: Optional[str] = None,
    ) -> Union[Response, Coroutine[None, None, Response]]:
        """
        Validate a Turnstile token against the Cloudflare service.

        Parameters
        ----------
        token : str
            Turnstile token to validate.
        ip : str, optional
            IP address of the submitting user.
        idempotency_key : str, optional
            Unique key to ensure the request is idempotent.

        Returns
        -------
        Response
            Response from the Turnstile validation service.
        Coroutine[None, None, Response]
            Asynchronous response if implemented asynchronously.
        """
