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

* [ ] Remove sayhello workflow stuff.
* [ ] Define workflow and activity.
* [ ] Wire up worker process with access to necessary workflows and activities.
