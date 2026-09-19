CREATE OR REPLACE FUNCTION NthHighestSalary(N INT)
RETURNS TABLE (Salary INT) AS $$
BEGIN
    RETURN QUERY
    SELECT (
        SELECT DISTINCT E.salary
        FROM Employee E
        ORDER BY E.salary DESC
        LIMIT 1 OFFSET GREATEST(N - 1, 0)
    )::INT
    WHERE N >= 1;
END;
$$ LANGUAGE plpgsql;