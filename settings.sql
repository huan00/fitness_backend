-- settings.sql
CREATE DATABASE fitness;
CREATE USER fituser WITH PASSWORD 'fit';
GRANT ALL PRIVILEGES ON DATABASE fitness TO fituser;