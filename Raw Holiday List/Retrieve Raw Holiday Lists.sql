SELECT dhu.id, dhu.start_date, dhu.end_date
FROM dim_holidays_uk dhu
WHERE dhu.country = 'Scotland'
GROUP BY dhu.id;

SELECT dhu.id, dhu.start_date, dhu.end_date
FROM dim_holidays_uk dhu
WHERE dhu.country = 'Wales'
GROUP BY dhu.id;

SELECT dhu.id, dhu.start_date, dhu.end_date
FROM dim_holidays_uk dhu
where dhu.country = 'Northern Ireland'
GROUP BY dhu.id;

SELECT dhu.id, dhu.start_date, dhu.end_date
FROM dim_holidays_uk dhu
WHERE dhu.country = 'England'
GROUP BY dhu.id;