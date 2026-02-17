"""Model definitions for the Cloudflare Turnstile response."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class MetaData(BaseModel):
    """Represents metadata associated with the Turnstile response.

    :ivar ephemeral_id: An optional identifier for the ephemeral session.
    :vartype ephemeral_id: Optional[str]
    :ivar result_with_testing_key: Whether the result is from a testing key.
    :vartype result_with_testing_key: bool
    """

    ephemeral_id: Optional[str] = None

    result_with_testing_key: bool = False


class Response(BaseModel):
    """Represents the response from the Cloudflare Turnstile verification.

    :ivar success: Indicates whether the verification was successful.
    :vartype success: bool
    :ivar hostname: The hostname of the site where the Turnstile was used.
    :vartype hostname: Optional[str]
    :ivar action: An optional action name associated with the Turnstile request.
    :vartype action: Optional[str]
    :ivar cdata: An optional custom data field.
    :vartype cdata: Optional[str]
    :ivar metadata: Optional metadata related to the Turnstile response.
    :vartype metadata: MetaData
    :ivar timestamp: The time when the challenge was solved.
    :vartype timestamp: Optional[datetime]
    :ivar error_codes: A list of error codes that may be returned in case of failure.
    :vartype error_codes: list[str]
    """

    success: bool
    """Indicates whether the verification was successful."""

    hostname: Optional[str] = None
    """The hostname of the site where the Turnstile was used."""

    action: Optional[str] = None
    """An optional action name associated with the Turnstile request."""

    cdata: Optional[str] = None
    """An optional custom data field."""

    metadata: MetaData = MetaData()
    """Optional metadata related to the Turnstile response."""

    timestamp: Optional[datetime] = Field(alias="challenge_ts", default=None)
    """The time when the challenge was solved."""

    error_codes: list[str] = Field(validation_alias="error-codes", default_factory=list)
    """A list of error codes that may be returned in case of failure."""
