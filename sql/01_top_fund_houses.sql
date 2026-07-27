SELECT
    fund_house,
    SUM(aum_crore) AS total_aum_crore
FROM "03_aum_by_fund_house"
GROUP BY fund_house
ORDER BY total_aum_crore DESC;