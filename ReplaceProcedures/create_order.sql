CREATE OR REPLACE FUNCTION create_order(
    p_order_date DATE,
    p_customer_id INTEGER,
    p_status_id INTEGER
) RETURNS VOID ASS $$
BEGIN 
    INSERT INTO orders(order_date, customer_id, status_id)
    VALUES (p_order_date, p_customer_id, p_status_id);
END;
$$ LANGUAGE plpgsql