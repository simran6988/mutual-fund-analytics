/*---------------------------------------------------------
Which states contribute the highest investment amount?
---------------------------------------------------------*/

SELECT
    state,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;

/*---------------------------------------------------------
Which age groups contribute the highest investment amount?
---------------------------------------------------------*/

SELECT
    age_group,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM "08_investor_transactions"
GROUP BY age_group
ORDER BY total_investment DESC;

/*---------------------------------------------------------
Which income groups contribute the highest investment amount?
---------------------------------------------------------*/

SELECT
    CASE
        WHEN annual_income_lakh < 10 THEN 'Below 10 Lakh'
        WHEN annual_income_lakh BETWEEN 10 AND 25 THEN '10 - 25 Lakh'
        WHEN annual_income_lakh BETWEEN 25 AND 50 THEN '25 - 50 Lakh'
        WHEN annual_income_lakh BETWEEN 50 AND 75 THEN '50 - 75 Lakh'
        ELSE 'Above 75 Lakh'
    END AS income_group,

    ROUND(SUM(amount_inr), 2) AS total_investment

FROM "08_investor_transactions"

GROUP BY income_group

ORDER BY total_investment DESC;

/*---------------------------------------------------------
Which payment methods are used most frequently?
---------------------------------------------------------*/

SELECT
    payment_mode,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM "08_investor_transactions"
GROUP BY payment_mode
ORDER BY transaction_count DESC;

/*---------------------------------------------------------
What is the KYC completion status of investors?
---------------------------------------------------------*/

SELECT
    kyc_status,
    COUNT(*) AS investor_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM "08_investor_transactions"),
        2
    ) AS percentage
FROM "08_investor_transactions"
GROUP BY kyc_status
ORDER BY investor_count DESC;