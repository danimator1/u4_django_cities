-- settings.sql
CREATE DATABASE djourneys;
CREATE USER djourneysuser WITH PASSWORD 'djourneys';
GRANT ALL PRIVILEGES ON DATABASE djourneys TO djourneysuser;
ALTER DATABASE djourneys OWNER TO djourneysuser;