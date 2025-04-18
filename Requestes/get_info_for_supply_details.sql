SELECT s.supplier_name, p.part_name, su.supply_date, su.quantity
FROM supplies su
JOIN suppliers s ON su.supplier_id = s.supplier_id
JOIN parts p ON su.part_id = p.part_id;