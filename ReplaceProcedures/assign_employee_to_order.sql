CREATE OR REPLACE FUNCTION assign_employee_to_order(
    p_employee_id INTEGER,
    p_order_id INTEGER,
    p_role VARCHAR
) RETURNS VOID AS $$
BEGIN 
    INSERT INTO employee_orders (employee_id, order_id, role)
    VALUES (p_employee_id, p_order_id, p_role);
END;
$$ LANGUAGE plpgsql