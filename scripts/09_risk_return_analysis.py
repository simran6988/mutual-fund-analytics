import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
connection = sqlite3.connect("database/mutual_fund.db")

query = """
SELECT
    scheme_name,
    return_5yr_pct,
    std_dev_ann_pct
FROM "07_scheme_performance"
WHERE return_5yr_pct IS NOT NULL
AND std_dev_ann_pct IS NOT NULL
"""

df = pd.read_sql_query(query, connection)

connection.close()

# Create scatter plot
plt.figure(figsize=(10, 6))

plt.scatter(
    df["std_dev_ann_pct"],
    df["return_5yr_pct"],
    s=80,
    alpha=0.7
)

plt.title("Risk vs Return of Mutual Fund Schemes")
plt.xlabel("Risk (Standard Deviation %)")
plt.ylabel("5-Year Return (%)")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "reports/charts/fund/risk_vs_return.png",
    dpi=300
)

plt.show()

print("\nChart saved successfully.")
print("reports/charts/fund/risk_vs_return.png")