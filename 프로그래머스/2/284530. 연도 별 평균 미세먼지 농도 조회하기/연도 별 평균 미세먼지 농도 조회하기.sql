SELECT year(ym) AS year, 
    round(AVG(pm_val1), 2) AS pm10, round(AVG(pm_val2), 2) AS `pm2.5`
FROM air_pollution
WHERE location2 = '수원'
GROUP BY year
ORDER BY year;