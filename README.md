# Temporal demo

This demo project shows a Temporal workflow in operation.
Because this demo is for a live presentation,
portions of this flow will be synthetic.

* Django site - http://localhost:8000
* Temporal UI - http://localhost:8233

## Big (Dumb) Assumptions

* There is only a single user to support. This avoids auth and work around
  selecting the right user.
* This code is not going to production. Please, do NOT blindly copy/paste
  without thinking about what your code needs to do.
* Assuming use of NGROK_URL so the demo will not run without setting a value
  in a `.env` file. The value could be anything, but the notifications won't work
  without a publicly resolvable URL.

## Plan

1. Run the trigger view to pretend to be a scheduled workflow.
2. Interact with the happy path so that nothing is added to the escrow.
3. Show the failure path to show that the escrow is incremented.

## The Workflow

1. Send the rich notification.
2. Wait for a signal.
3. Update escrow.
4. On failure, notify escrow amount.
