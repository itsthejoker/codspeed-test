from dataclasses import dataclass

from snowfake import *

from asbestos import AsbestosCursor, asbestos_cursor


@dataclass
class Settings:
    SNOWFLAKE_USER: str = "my_user"
    SNOWFLAKE_PASSWORD: str = "my_password"
    SNOWFLAKE_ACCOUNT: str = "my_account"
    SNOWFLAKE_WAREHOUSE: str = "my_warehouse"
    SNOWFLAKE_DB: str = "my_database"
    SNOWFLAKE_SCHEMA: str = "my_schema"
    ENABLE_ASBESTOS: bool = False


settings = Settings()
snowflake_connector = SnowfakeConnector()


def snowflake_connection() -> SnowfakeConnection:
    return snowflake_connector.connect(
        user=settings.SNOWFLAKE_USER,
        password=settings.SNOWFLAKE_PASSWORD,
        account=settings.SNOWFLAKE_ACCOUNT,
        warehouse=settings.SNOWFLAKE_WAREHOUSE,
        database=settings.SNOWFLAKE_DB,
        schema=settings.SNOWFLAKE_SCHEMA,
    )


def snowflake_cursor() -> SnowfakeCursor | AsbestosCursor:
    if settings.ENABLE_ASBESTOS:
        return asbestos_cursor()
    return SnowfakeConnection().cursor(DictCursor)


def main(sql_string):
    """This is an example of a lot of our failing tests."""
    with snowflake_cursor() as cursor:
        cursor.execute(sql_string)
        return cursor.fetchall()
