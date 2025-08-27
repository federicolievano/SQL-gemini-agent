import pymysql
import pandas as pd
from config import DB_CONFIG


def get_connection():
    """Create and return a database connection"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def execute_query(query):
    """Execute a SQL query and return results as DataFrame"""
    connection = get_connection()
    if not connection:
        return None

    try:
        df = pd.read_sql(query, connection)
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        connection.close()


def get_table_schema(table_name):
    """Get schema information for a specific table"""
    query = f"DESCRIBE {table_name}"
    return execute_query(query)


def get_available_tables():
    """Get list of available tables in the database"""
    query = "SHOW TABLES"
    return execute_query(query)
