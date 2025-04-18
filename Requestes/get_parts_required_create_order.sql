SELECT o.order_id, p.part_name, op.quantity
FROM  order_parts op
JOIN orders o ON op.order_id = o.order_id
JOIN parts p ON op.part_id = p.part_id;