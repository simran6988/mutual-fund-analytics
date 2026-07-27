"""
Project : Mutual Fund Analytics
Author  : Simran
Purpose : Load all cleaned datasets into SQLite.
"""

from pathlib import Path
import sqlite3
import pandas as pd


def main():
    # Project paths
    database_path = Path("database") / "mutual_fund.db"
    processed_path = Path("data") / "processed"

    # Connect to SQLite
    connection = sqlite3.connect(database_path)

    print("=" * 60)
    print("MUTUAL FUND ANALYTICS")
    print("Load Cleaned Data into SQLite")
    print("=" * 60)

    csv_files = sorted(processed_path.glob("*_clean.csv"))

    if not csv_files:
        print("No cleaned datasets found.")
        connection.close()
        return

    for file in csv_files:
        table_name = file.stem.replace("_clean", "")

        df = pd.read_csv(file)

        df.to_sql(
            table_name,
            connection,
            if_exists="replace",
            index=False
        )

        print(f"Loaded: {table_name} ({len(df)} rows)")

    connection.close()

    print("\nAll datasets loaded successfully.")
    print(f"Database saved at: {database_path}")


if __name__ == "__main__":
    main()