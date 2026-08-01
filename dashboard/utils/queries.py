# -----------------------------
# Home Dashboard
# -----------------------------

KPI_QUERY = """
SELECT
(
    SELECT COUNT(DISTINCT fund_house)
    FROM "03_aum_by_fund_house"
) AS fund_houses,

(
    SELECT COUNT(*)
    FROM "07_scheme_performance"
) AS schemes,

(
    SELECT COUNT(DISTINCT investor_id)
    FROM "08_investor_transactions"
) AS investors,

(
    SELECT ROUND(SUM(sip_inflow_crore),0)
    FROM "04_monthly_sip_inflows"
) AS sip_inflow;
"""


HOME_INSIGHT_QUERY = """
SELECT
    scheme_name,
    return_5yr_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 1;
"""


# -----------------------------
# Fund Analysis
# -----------------------------

TOP_FUNDS_QUERY = """
SELECT
    scheme_name,
    fund_house,
    return_5yr_pct,
    expense_ratio_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 10;
"""


# -----------------------------
# Investor Analysis
# -----------------------------

TOP_STATES_QUERY = """
SELECT
    state,
    ROUND(SUM(amount_inr)/10000000,2) AS investment_crore
FROM "08_investor_transactions"
GROUP BY state
ORDER BY investment_crore DESC
LIMIT 10;
"""


PAYMENT_MODE_QUERY = """
SELECT
    payment_mode,
    COUNT(*) AS transactions
FROM "08_investor_transactions"
GROUP BY payment_mode
ORDER BY transactions DESC;
"""


# -----------------------------
# SIP Analysis
# -----------------------------

SIP_TREND_QUERY = """
SELECT
    month,
    sip_inflow_crore
FROM "04_monthly_sip_inflows"
ORDER BY month;
"""


CATEGORY_FLOW_QUERY = """
SELECT
    category,
    ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM "05_category_inflows"
GROUP BY category
ORDER BY total_inflow DESC;
"""


# -----------------------------
# Fund Explorer
# -----------------------------

FUND_LIST_QUERY = """
SELECT DISTINCT
    scheme_name
FROM "07_scheme_performance"
ORDER BY scheme_name;
"""