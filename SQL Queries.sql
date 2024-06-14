SELECT *
FROM employees
WHERE hire_date >= DATEADD(year, -1, GETDATE());

SELECT d.department_name, SUM(e.salary) AS total_salary_expenditure
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;

SELECT e.employee_name, e.salary, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary DESC
LIMIT 5;