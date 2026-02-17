Usage
=====

Installation
------------

Install from PyPI:

.. code-block:: shell

   pip install cloudstile

Quickstart
----------

Asynchronous example:

.. code-block:: python

   from cloudstile import AsyncTurnstile

   async_client = AsyncTurnstile(token="your-secret-key")
   response = await async_client.validate("token-from-client")
   print(response.success)

Synchronous example:

.. code-block:: python

   from cloudstile import SyncTurnstile

   sync_client = SyncTurnstile(token="your-secret-key")
   response = sync_client.validate("token-from-client")
   print(response.success)
