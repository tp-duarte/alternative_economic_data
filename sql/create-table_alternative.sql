-- Creates the SQL table for alternative data

CREATE TABLE alternative_data (
    date DATE PRIMARY KEY,
    search_hous_bubble NUMERIC (6, 4),
    search_pand_assist NUMERIC (6, 4),
    search_pfl NUMERIC (6, 4),
    search_recession NUMERIC (6, 4),
    search_unemp NUMERIC (6, 4),
	us_consumer_sentiment NUMERIC(4, 2),
    mob_leisure NUMERIC(8, 6),
    mob_groc_pharm NUMERIC(8, 6),
    mob_parks NUMERIC(8, 6),
    mob_transit NUMERIC(8, 6),
    mob_workplaces NUMERIC(8, 6),
    mob_residential NUMERIC(8, 6)
);


INSERT INTO alternative_data (date)
SELECT generate_series('2005-01-01'::DATE, '2022-10-01'::DATE, '3 months'::INTERVAL) AS date;