import json
import uuid

from django.http import HttpResponse
from django.shortcuts import render
from temporalio.client import Client

from core.workflows import HealthCheckin


def index(request):
    return render(request, "index.html", {})


async def trigger(request):
    """Trigger the workflow.

    In a real system, a workflow would be started by a schedule.
    A workflow would trigger child workflows for each user OR
    the system could be designed so that each user got its own unique schedule.
    """
    client = await Client.connect("localhost:7233")

    workflow_id = f"health-checkin-{uuid.uuid4()}"
    await client.start_workflow(
        HealthCheckin.run,
        id=workflow_id,
        task_queue="health-checkin-task-queue",
    )

    return HttpResponse(workflow_id.encode())


async def answer(request):
    data = json.loads(request.body.decode())
    workflow_id = data["workflow_id"]
    client = await Client.connect("localhost:7233")
    handle = client.get_workflow_handle(workflow_id)
    await handle.signal(HealthCheckin.send_answer, data["reply"])
    return HttpResponse(b"{}")
