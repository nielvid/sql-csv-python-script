SELECT table_name as tables
FROM information_schema.tables
WHERE table_schema = 'locations'
AND table_type = 'BASE TABLE';