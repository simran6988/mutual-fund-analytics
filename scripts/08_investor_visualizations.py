import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
connection = sqlite3.connect("database/mutual_fund.db")

query = """
SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10
"""

df = pd.read_sql_query(query, connection)

connection.close()

# Create chart
plt.figure(figsize=(10, 6))

plt.barh(df["state"], df["total_investment"])

plt.title("Top 10 States by Investment Amount")
plt.xlabel("Investment Amount (INR)")
plt.ylabel("State")

plt.tight_layout()

# Save chart
plt.savefig(
    "reports/charts/investor/top_states_investment.png",
    dpi=300
)

plt.show()

print("\nChart saved successfully.")
print("reports/charts/investor/top_states_investment.png")