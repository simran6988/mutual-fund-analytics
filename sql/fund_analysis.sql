-- 1. Top Fund Houses by Total Assets Under Management (AUM)

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum_crore
FROM "03_aum_by_fund_house"
GROUP BY fund_house
ORDER BY total_aum_crore DESC;

-- 2. Number of Mutual Fund Schemes Offered by Each Fund House

SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM "01_fund_master"
GROUP BY fund_house
ORDER BY total_schemes DESC;

/*---------------------------------------------------------
Which fund houses have the highest average expense ratio?
---------------------------------------------------------*/

SELECT
    fund_house,
    ROUND(AVG(expense_ratio_pct), 2) AS average_expense_ratio
FROM "07_scheme_performance"
GROUP BY fund_house
ORDER BY average_expense_ratio DESC;

/*---------------------------------------------------------
Which mutual fund schemes have delivered the highest 5-year returns?
---------------------------------------------------------*/

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 10;

/*---------------------------------------------------------
Which mutual fund schemes have the highest risk-adjusted returns?
---------------------------------------------------------*/

SELECT
    scheme_name,
    fund_house,
    sharpe_ratio
FROM "07_scheme_performance"
ORDER BY sharpe_ratio DESC
LIMIT 10;