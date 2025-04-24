CREATE OR REPLACE FUNCTION update_order_status(
    p_order_id INTEGER,
    p_status_id INTEGER
) RETURNS VOID AS $$
BEGIN 
    UPDATE orders
    SET status_id = p_status_id
    WHERE order_id = p_order_id;
END;
$$ LANGUAGE plpgsql