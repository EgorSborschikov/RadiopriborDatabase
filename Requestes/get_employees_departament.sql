SELECT e.name, d.departament_name
FROM employees e
JOIN departaments d ON e.departament_id = d.departament_id;