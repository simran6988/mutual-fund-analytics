import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
connection = sqlite3.connect("database/mutual_fund.db")

query = """
SELECT
    scheme_name,
    expense_ratio_pct,
    return_5yr_pct
FROM "07_scheme_performance"
WHERE expense_ratio_pct IS NOT NULL
AND return_5yr_pct IS NOT NULL
"""

df = pd.read_sql_query(query, connection)

connection.close()

plt.figure(figsize=(10, 6))

plt.scatter(
    df["expense_ratio_pct"],
    df["return_5yr_pct"],
    s=80,
    alpha=0.7
)

plt.title("Expense Ratio vs 5-Year Return")
plt.xlabel("Expense Ratio (%)")
plt.ylabel("5-Year Return (%)")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "reports/charts/fund/expense_vs_return.png",
    dpi=300
)

plt.show()

print("\nChart saved successfully.")
print("reports/charts/fund/expense_vs_return.png")