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