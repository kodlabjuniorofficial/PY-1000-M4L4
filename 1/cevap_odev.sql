-- ÇÖZÜM-1:
SELECT name, year 
FROM top250 
ORDER BY year ASC 
LIMIT 5;

-- ÇÖZÜM-2:
SELECT name, rating 
FROM top250 
WHERE rating >= 9.0;

-- ÇÖZÜM-3:
SELECT genre, COUNT(*) 
FROM top250 
GROUP BY genre 
ORDER BY COUNT(*) DESC;

-- ÇÖZÜM-4:
SELECT AVG(budget), SUM(box_office) 
FROM top250;

-- ÇÖZÜM-5:
SELECT name, run_time 
FROM top250 
WHERE run_time > 180;
