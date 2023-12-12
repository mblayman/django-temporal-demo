import asyncio
from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from core.activities import notify_status, send_notification, update_escrow


ANSWER_TIMEOUT = 60 * 60 * 4  # Wait 4 hours for a response from the user.


@workflow.defn
class HealthCheckin:
    """A workflow to check if the user followed their commitment
    to regular healthy activity
    """

    def __init__(self):
        self._answer_queue = asyncio.Queue()

    @workflow.run
    async def run(self) -> None:
        """The workflow definition"""
        await workflow.execute_activity(
            send_notification,
            start_to_close_timeout=timedelta(seconds=5),
        )

        await workflow.wait_condition(
            lambda: not self._answer_queue.empty(),
            timeout=ANSWER_TIMEOUT,
        )

        reply = await self._answer_queue.get()

        await workflow.execute_activity(
            update_escrow,
            reply,
            start_to_close_timeout=timedelta(seconds=5),
        )

        await workflow.execute_activity(
            notify_status,
            reply,
            start_to_close_timeout=timedelta(seconds=5),
        )

        self._answer_queue.task_done()
        return None

    @workflow.signal
    async def send_answer(self, reply):
        await self._answer_queue.put(reply)
