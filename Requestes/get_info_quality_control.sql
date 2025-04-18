SELECT o.order_id, qc.qc_status, qc.qc_date
FROM quality_control qc
JOIN orders o ON qc.order_id = o.order_id;