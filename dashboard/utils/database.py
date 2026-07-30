import sqlite3
import pandas as pd


DATABASE_PATH = "database/mutual_fund.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def run_query(query):
    connection = get_connection()

    try:
        dataframe = pd.read_sql_query(query, connection)
        return dataframe
    finally:
        connection.close()