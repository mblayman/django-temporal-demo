import json

import httpx
from django.conf import settings
from temporalio import activity

from .models import Escrow


@activity.defn
async def send_notification() -> None:
    """Send notification to user.

    In a real app, this would send a notification to a specific user.
    """
    workflow_id = activity.info().workflow_id

    async with httpx.AsyncClient() as client:
        await client.post(
            "https://ntfy.sh/",
            json={
                "topic": "mblayman-temporal",
                "title": "Did you get moving?",
                "message": "In the last 24 hours, did you exercise like you promised yourself?",
                "actions": [
                    {
                        "action": "http",
                        "label": "Yep",
                        # In a real app, this would be the actual response URL.
                        "url": settings.NGROK_URL + "answer/",
                        "method": "POST",
                        "body": json.dumps(
                            {"reply": "yes", "workflow_id": workflow_id}
                        ),
                    },
                    {
                        "action": "http",
                        "label": "Nah",
                        # In a real app, this would be the actual response URL.
                        "url": settings.NGROK_URL + "answer/",
                        "method": "POST",
                        "body": json.dumps({"reply": "no", "workflow_id": workflow_id}),
                    },
                ],
            },
        )
    return None


@activity.defn
async def update_escrow(reply) -> None:
    """Update the escrow account if the user did not exercise."""
    if reply == "yes":
        return None

    # In a real app, we would have to find the escrow account related to the user.
    # Here we will assume that there is only one account for demo purposes.
    escrow = await Escrow.objects.afirst()
    escrow.amount += 10 * 100  # Amount is in cents.
    await escrow.asave()
    return None


@activity.defn
async def notify_status(reply) -> None:
    """Notify a user that they failed."""
    if reply == "yes":
        return None

    # In a real app, this would send a notification to a specific user.
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://ntfy.sh/",
            json={
                "topic": "mblayman-temporal",
                "title": "Say goodbye to your money!",
                "message": (
                    "We'll send $10 to your least favorite political party. "
                    " You had better get moving tomorrow!"
                ),
            },
        )
    return None
