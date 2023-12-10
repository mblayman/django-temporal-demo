from django.http import HttpResponse
from temporalio.client import Client

from core.workflows import HealthCheckin


async def trigger(request):
    """Trigger the workflow.

    In a real system, a workflow would be started by a schedule.
    A workflow would trigger child workflows for each user OR
    the system could be designed so that each user got its own unique schedule.
    """
    client = await Client.connect("localhost:7233")

    await client.start_workflow(
        HealthCheckin.run,
        id="health-checkin-workflow",
        task_queue="health-checkin-task-queue",
    )

    return HttpResponse(b"ok")
