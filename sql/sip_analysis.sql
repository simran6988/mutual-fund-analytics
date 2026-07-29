/*---------------------------------------------------------
How have monthly SIP inflows changed over time?
---------------------------------------------------------*/

SELECT
    month,
    sip_inflow_crore,
    active_sip_accounts_crore
FROM "04_monthly_sip_inflows"
ORDER BY month;

/*---------------------------------------------------------
Which categories received the highest net inflows?
---------------------------------------------------------*/

SELECT
    category,
    ROUND(SUM(net_inflow_crore), 2) AS total_net_inflow
FROM "05_category_inflows"
GROUP BY category
ORDER BY total_net_inflow DESC;

/*---------------------------------------------------------
How has the mutual fund industry's total folio count changed?
---------------------------------------------------------*/

SELECT
    month,
    total_folios_crore,
    equity_folios_crore,
    debt_folios_crore,
    hybrid_folios_crore
FROM "06_industry_folio_count"
ORDER BY month;

/*---------------------------------------------------------
Which fund houses manage the highest Assets Under Management (AUM)?
---------------------------------------------------------*/

SELECT
    fund_house,
    MAX(aum_crore) AS latest_aum_crore,
    MAX(num_schemes) AS total_schemes
FROM "03_aum_by_fund_house"
GROUP BY fund_house
ORDER BY latest_aum_crore DESC
LIMIT 10;