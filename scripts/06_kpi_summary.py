import sqlite3
import pandas as pd

print("=" * 60)
print("MUTUAL FUND ANALYTICS")
print("Key Performance Indicators")
print("=" * 60)

connection = sqlite3.connect("database/mutual_fund.db")

# Total Fund Houses
fund_houses = pd.read_sql_query("""
SELECT COUNT(DISTINCT fund_house) AS total
FROM "01_fund_master"
""", connection)

# Total Schemes
schemes = pd.read_sql_query("""
SELECT COUNT(*) AS total
FROM "01_fund_master"
""", connection)

# Total AUM
aum = pd.read_sql_query("""
SELECT MAX(aum_crore) AS total
FROM "03_aum_by_fund_house"
""", connection)

# Total Investors
investors = pd.read_sql_query("""
SELECT COUNT(DISTINCT investor_id) AS total
FROM "08_investor_transactions"
""", connection)

# Total SIP Inflow
sip = pd.read_sql_query("""
SELECT SUM(sip_inflow_crore) AS total
FROM "04_monthly_sip_inflows"
""", connection)

# Best Performing Fund
best_fund = pd.read_sql_query("""
SELECT
    scheme_name,
    return_5yr_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 1
""", connection)

connection.close()

print(f"Total Fund Houses : {fund_houses.iloc[0]['total']}")
print(f"Total Schemes     : {schemes.iloc[0]['total']}")
print(f"Highest AUM       : {aum.iloc[0]['total']:,} Crore")
print(f"Total Investors   : {investors.iloc[0]['total']:,}")
print(f"Total SIP Inflow  : {sip.iloc[0]['total']:,} Crore")

print("\nBest Performing Fund")
print("--------------------")
print(best_fund.to_string(index=False))