-- Calculate the total number of fans for each band origin
-- and order the results by the total number of fans in descending order
SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
