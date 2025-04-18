SELECT o.order_id, e.name, eo.role
FROM employee_orders eo
JOIN orders o ON eo.order_id = o.order_id
JOIN employees e ON eo.employee_id = e.employee_id;