"""
Project : Mutual Fund Analytics
Author  : Simran
Purpose : Execute SQL queries stored in the sql folder.
"""

from pathlib import Path
import sqlite3
import pandas as pd


DATABASE_PATH = Path("database") / "mutual_fund.db"
SQL_PATH = Path("sql") / "01_top_fund_houses.sql"


def main():

    connection = sqlite3.connect(DATABASE_PATH)

    with open(SQL_PATH, "r", encoding="utf-8") as file:
        query = file.read()

    result = pd.read_sql_query(query, connection)

    connection.close()

    print("=" * 60)
    print("MUTUAL FUND ANALYTICS")
    print("SQL Query Result")
    print("=" * 60)

    print(result)

    print(f"\nTotal Rows : {len(result)}")


if __name__ == "__main__":
    main()