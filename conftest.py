import pytest

from asbestos import config


# We're using a variant of this, but it's not necessary for this testing suite.
# I'm including it for completeness.

# def pytest_collection_modifyitems(items):
#     # automatically go through every test and mark it for benchmarking
#     for item in items:
#         item.add_marker("benchmark")


@pytest.fixture(autouse=True)
def run_around_tests():
    """Run the test, then clear any asbestos queries that are lurking."""
    yield
    config.clear_queries()
