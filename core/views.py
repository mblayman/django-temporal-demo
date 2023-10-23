from django.http import HttpResponse
from temporalio.client import Client

from core.workflows import SayHello


async def hello(request, name):
    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        SayHello.run, name, id="hello-workflow", task_queue="hello-task-queue"
    )

    return HttpResponse(result.encode())
