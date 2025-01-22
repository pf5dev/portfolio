CREATE DATABASE db0;
\c db0
CREATE TABLE tabela0("name" text,
"id" numeric,
"nametype" text,
"recclass" text,
"mass (g)" numeric,
"fall" text,
"year" numeric,
"reclat" numeric,
"reclong" numeric,
"GeoLocation" text);
\d+ tabela0
COPY tabela0 FROM '/docker-entrypoint-initdb.d/Meteorite_Landings.csv' DELIMITER ',' CSV HEADER;
