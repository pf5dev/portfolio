CREATE TABLE tabela1("name" text,
"id" numeric,
"nametype" text,
"recclass" text,
"mass (g)" numeric,
"fall" text,
"year" numeric,
"reclat" numeric,
"reclong" numeric,
"GeoLocation" text);
COPY tabela1 FROM '/docker-entrypoint-initdb.d/Meteorite_Landings.csv' DELIMITER ',' CSV HEADER;
