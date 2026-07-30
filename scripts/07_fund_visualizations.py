import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
connection = sqlite3.connect("database/mutual_fund.db")

# Read data
query = """
SELECT
    fund_house,
    MAX(aum_crore) AS latest_aum
FROM "03_aum_by_fund_house"
GROUP BY fund_house
ORDER BY latest_aum DESC
LIMIT 10
"""

df = pd.read_sql_query(query, connection)

connection.close()

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(df["fund_house"], df["latest_aum"])

plt.title("Top 10 Fund Houses by Assets Under Management")
plt.xlabel("Fund House")
plt.ylabel("AUM (Crore)")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save chart
plt.savefig("reports/charts/top_10_fund_houses_aum.png", dpi=300)

plt.show()

print("\nChart saved successfully.")
print("reports/charts/top_10_fund_houses_aum.png")