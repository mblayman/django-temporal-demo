import json

import httpx
from temporalio import activity


@activity.defn
async def send_notification() -> None:
    return None
    # TODO: Call ntfy.sh and send along the workflow execution ID.
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://ntfy.sh/",
            json={
                "topic": "mblayman-test123",
                "title": "Did you get moving?",
                "message": "In the last 24 hours, did you exercise like you promised yourself?",
                "actions": [
                    {
                        "action": "http",
                        "label": "Yep",
                        "url": "https://www.mattlayman.com/",
                        "method": "POST",
                        "body": json.dumps({"execution-id": "123"}),
                    }
                ],
            },
        )
    return None
