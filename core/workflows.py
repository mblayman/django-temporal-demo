from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from core.activities import send_notification


@workflow.defn
class HealthCheckin:
    """A workflow to check if the user followed their commitment
    to regular healthy activity
    """

    @workflow.run
    async def run(self) -> None:
        """The workflow definition"""
        return await workflow.execute_activity(
            send_notification,
            start_to_close_timeout=timedelta(seconds=5),
        )
