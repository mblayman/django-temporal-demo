import uvloop
from django.core.management.base import BaseCommand
from temporalio.client import Client
from temporalio.worker import Worker

from core.activities import say_hello
from core.workflows import SayHello


async def run():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client,
        task_queue="hello-task-queue",
        workflows=[SayHello],
        activities=[say_hello],
    )
    await worker.run()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        uvloop.run(run())
