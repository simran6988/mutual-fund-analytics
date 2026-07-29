"""
Project : Mutual Fund Analytics
Purpose : Execute SQL queries from a .sql file
"""

from pathlib import Path
import sqlite3
import pandas as pd


DATABASE_PATH = Path("database") / "mutual_fund.db"
SQL_FILE = Path("sql") / "investor_analysis.sql"


def main():

    connection = sqlite3.connect(DATABASE_PATH)

    with open(SQL_FILE, "r", encoding="utf-8") as file:
        sql_script = file.read()

    queries = [
        query.strip()
        for query in sql_script.split(";")
        if query.strip()
    ]

    for index, query in enumerate(queries, start=1):

        print("\n" + "=" * 70)
        print(f"Query {index}")
        print("=" * 70)

        try:
            result = pd.read_sql_query(query, connection)
            print(result)

            print(f"\nRows Returned : {len(result)}")

        except Exception as error:
            print(f"Error: {error}")

    connection.close()


if __name__ == "__main__":
    main()