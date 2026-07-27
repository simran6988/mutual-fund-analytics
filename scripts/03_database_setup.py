"""
Project : Mutual Fund Analytics
Author  : Simran
Purpose : Create the SQLite database for the project.
"""

from pathlib import Path
import sqlite3

# Project paths
DATABASE_FOLDER = Path("database")
DATABASE_FOLDER.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_FOLDER / "mutual_fund.db"

# Create database
connection = sqlite3.connect(DATABASE_PATH)

print("=" * 60)
print("MUTUAL FUND ANALYTICS")
print("SQLite Database Setup")
print("=" * 60)

print(f"\nDatabase created successfully:")
print(DATABASE_PATH)

connection.close()