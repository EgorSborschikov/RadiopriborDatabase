SELECT tc.tech_card_id, mp.program_code
FROM machine_programs mp
JOIN tech_card tc ON mp.tech_card_id = tc.tech_card_id;