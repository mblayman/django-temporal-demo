import asyncio
import uvloop
from django.core.management.base import BaseCommand
from temporalio.client import Client
from temporalio.worker import Worker

from core.activities import send_notification
from core.workflows import HealthCheckin


async def run():
    client = await get_client()
    if client is None:
        print("Failed to connect")
        return

    # Run the worker
    worker = Worker(
        client,
        task_queue="health-checkin-task-queue",
        workflows=[HealthCheckin],
        activities=[send_notification],
    )
    await worker.run()


async def get_client() -> Client | None:
    """Get the Temporal client.

    The demo has a race condition in startup between the Temporal server
    and the worker. We try to get the client in a silly while loop
    so that the demo doesn't crash on startup.
    """
    connecting = True
    client = None
    while connecting:
        try:
            client = await Client.connect("localhost:7233", namespace="default")
            connecting = False
            print("Connected to Temporal")
        except RuntimeError:
            # This code is pretty dumb. In a real context, don't try to connect forever.
            print("Failed to connect to Temporal. Retrying...")
            await asyncio.sleep(1)

    return client


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        uvloop.run(run())
