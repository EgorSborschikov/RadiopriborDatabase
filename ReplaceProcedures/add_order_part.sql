CREATE OR REPLACE FUNCTION  add_order_part(
    p_order_id INTEGER,
    p_part_id INTEGER,
    p_quantity INTEGER
) RETURNS VOID AS $$
BEGIN
    INSERT INTO order_parts (order_id, part_id, quantity)
    VALUES (p_order_id, p_part_id, p_quantity);
END;
$$ LANGUAGE plpgsql