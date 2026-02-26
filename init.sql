CREATE TABLE IF NOT EXISTS requests (
    id SERIAL PRIMARY KEY,
    path TEXT,
    host TEXT,
    port INTEGER,
    time TEXT
);
