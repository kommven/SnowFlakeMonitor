import streamlit as st
from snowflake_connector import SnowflakeConnector

st.title("Snowflake Connection App")

account = st.text_input("Snowflake Account")
user = st.text_input("Username")
private_key = st.text_input("API Key", type="password")
warehouse = st.text_input("Warehouse")
database = st.text_input("Database")
schema = st.text_input("Schema")

if st.button("Connect"):
    try:
        connector = SnowflakeConnector(
            account=account,
            user=user,
            private_key=private_key,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        connector.connect()
        st.success("Connection established successfully!")
    except Exception as e:
        st.error(f"Connection failed: {e}")
