# SnowFlakeMonitor
This is a web-based Application to provide user various reports for Organization Health

## SnowflakeConnector Class

The `SnowflakeConnector` class is a Python class designed to connect to Snowflake using an API Key. It provides methods to initialize the connection, execute queries, and close the connection.

### Usage Instructions

1. Install the `snowflake-connector-python` package if you haven't already:
   ```bash
   pip install snowflake-connector-python
   ```

2. Create an instance of the `SnowflakeConnector` class:
   ```python
   from snowflake_connector import SnowflakeConnector

   connector = SnowflakeConnector(
       account='your_account',
       user='your_user',
       private_key='your_private_key',
       warehouse='your_warehouse',
       database='your_database',
       schema='your_schema'
   )
   ```

3. Establish the connection to Snowflake:
   ```python
   connector.connect()
   ```

4. Execute a query:
   ```python
   result = connector.execute_query('SELECT * FROM your_table')
   print(result)
   ```

5. Close the connection:
   ```python
   connector.close_connection()
   ```
