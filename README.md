# codspeed-test

This is an example of a set of tests that runs normally using `pytest`, but fails when using `codspeed`. This repo is "as close to production" as I can get, and demonstrates an example where we use the `asbestos` library (https://pypi.org/project/asbestos/) to intercept and mock a Snowflake cursor so that we can dynamically inject SQL and expected responses for testing. 

There is an issue with codspeed that causes test teardown to not run properly, which causes the test to fail on the second run.


## Repo Setup

You will need `uv` installed to set up the repo. Clone it first, then run:

```sh
uv sync
```

Run the tests with:

```sh
uv run pytest && uv run pytest --codspeed
```
