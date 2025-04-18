SELECT p.part_name, tc.operations
FROM tech_cards tc
JOIN parts p ON tc.part_id = p.part_id;