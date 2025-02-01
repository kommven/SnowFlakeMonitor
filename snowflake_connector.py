import snowflake.connector

class SnowflakeConnector:
    def __init__(self, account, user, private_key, warehouse, database, schema):
        self.account = account
        self.user = user
        self.private_key = private_key
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.connection = None

    def connect(self):
        self.connection = snowflake.connector.connect(
            account=self.account,
            user=self.user,
            private_key=self.private_key,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )

    def execute_query(self, query):
        if self.connection is None:
            raise Exception("Connection not established. Call connect() first.")
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
