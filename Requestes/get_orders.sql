SELECT o.order_id, o.order_date, s.status_name
FROM orders o
JOIN order_status s ON o.status_id = s.status; -- Выбирается статус с соответствии с id
