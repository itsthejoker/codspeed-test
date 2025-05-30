# Minimum code to mock a Snowflake connection and cursor for testing purposes


class DictCursor:
    ...


class SnowfakeCursor:
    def __init__(self, cursor_type=None):
        self.cursor_type = cursor_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class SnowfakeConnection:
    def cursor(self, *args, **kwargs):
        return SnowfakeCursor()


class SnowfakeConnector:
    def connect(self, user, password, account, warehouse, database, schema):
        return SnowfakeConnection()
