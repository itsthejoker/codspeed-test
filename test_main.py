from unittest.mock import patch

from main import main, snowflake_cursor, Settings
from snowfake import *

from asbestos import AsbestosCursor, config as asbestos_config
import pytest


test_settings = Settings(
    SNOWFLAKE_USER="test_user",
    SNOWFLAKE_PASSWORD="test_password",
    SNOWFLAKE_ACCOUNT="test_account",
    SNOWFLAKE_WAREHOUSE="test_warehouse",
    SNOWFLAKE_DB="test_database",
    SNOWFLAKE_SCHEMA="test_schema",
    ENABLE_ASBESTOS=True,
)


TEST_QUERY = "SELECT * FROM test_table"
TEST_RESPONSE = [
    {"column1": "value1", "column2": "value2"},
    {"column1": "value3", "column2": "value4"},
]


def test_snowflake_cursor_returned_without_patch():
    """Test that the snowflake_cursor function returns a SnowflakeCursor."""
    with snowflake_cursor() as cursor:
        assert isinstance(cursor, SnowfakeCursor)


def test_asbestos_cursor_returned_with_patch():
    """Test that asbestos_cursor is returned when ENABLE_ASBESTOS is True."""
    with patch("main.settings", test_settings):
        with snowflake_cursor() as cursor:
            assert isinstance(cursor, AsbestosCursor)


@pytest.mark.benchmark
def test_example_sql_query(benchmark):
    """Test that the example SQL query returns a valid result. This test will
    fail with codspeed enabled, because the test query with Asbestos will
    be registered twice. The query will be cleared by an AutoUse fixture
    in conftest.py after the test."""
    with patch("main.settings", test_settings):
        asbestos_config.register(TEST_QUERY, TEST_RESPONSE)
        result = benchmark(main, TEST_QUERY)
        assert result == TEST_RESPONSE


@pytest.mark.benchmark
def test_demonstrate_that_clear_fixture_is_working(benchmark):
    with patch("main.settings", test_settings):
        result = benchmark(main, TEST_QUERY)
        assert result == []
