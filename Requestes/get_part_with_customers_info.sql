SELECT o.order_id, o.order_date, c.customer_name, s.status_name
FROM order order
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_status s ON o.status_id = s.status_id;