CREATE TABLE tabela0("PuzzleId" text,
"FEN" text,
"Moves" text,
"Rating" numeric,
"RatingDeviation" numeric,
"Popularity" numeric,
"NbPlays" numeric,
"Themes" text,
"GameUrl" text,
"OpeningTags" text);
COPY tabela0 FROM '/docker-entrypoint-initdb.d/lichess_db_puzzle.csv' DELIMITER ',' CSV HEADER;
