\c postgres;

DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'sprint_final') THEN
        CREATE DATABASE sprint_final;
    END IF;
END $$;

\c sprint_final;

CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);