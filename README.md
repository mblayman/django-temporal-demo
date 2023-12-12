# Temporal demo

This demo project shows a Temporal workflow in operation.
Because this demo is for a live presentation,
portions of this flow will be synthetic.

* Django site - http://localhost:8000
* Temporal UI - http://localhost:8233

## Big (Dumb) Assumptions

* There is only a single user to support. This avoids auth and work around
  selecting the right user.

## TODO

* [x] Remove sayhello workflow stuff.
* [x] Define workflow and activity.
* [x] Wire up worker process with access to necessary workflows and activities.
* [x] Create unique workflow ID per execution
* [ ] Use http action for ntfy.sh

## Plan

1. Run the trigger view to pretend to be a scheduled workflow.
2. Interact with the happy path so that nothing is added to the escrow.
3. Show the failure path to show that the escrow is incremented.


## The Workflow

1. Send the rich notification.
2. Wait for a signal.
3. Update escrow.
4. On failure, notify escrow amount.
