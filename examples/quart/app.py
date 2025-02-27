from quart import Quart, request, jsonify
from cloudstile import AsyncTurnstile

app = Quart(__name__)
turnstile = AsyncTurnstile(secret="...")


@app.route("/submit", methods=["POST"])
async def submit():

    body = await request.form

    response = await turnstile.validate(
        body.get("cf-turnstile-response", "..."),
        request.remote_addr,
    )

    return jsonify(response.model_dump())  # <- Response is a pydantic object


app.run()
