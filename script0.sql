CREATE DATABASE db0;
\c db0
CREATE TABLE tabela0("name" text,
"id" text,
"nametype" text,
"recclass" text,
"mass (g)" text,
"fall" text,
"year" text,
"reclat" text,
"reclong" text,
"GeoLocation" text);
\d+ tabela0
COPY tabela0 FROM '/docker-entrypoint-initdb.d/Meteorite_Landings.csv' DELIMITER ',' CSV HEADER;
