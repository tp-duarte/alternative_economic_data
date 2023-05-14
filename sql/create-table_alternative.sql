CREATE TABLE alternative_data (
    date DATE PRIMARY KEY,
    mob_leisure NUMERIC(2, 6),
    mob_groc_pharm NUMERIC(2, 6),
    mob_parks NUMERIC(2, 6),
    mob_transit NUMERIC(2, 6),
    mob_workplaces NUMERIC(2, 6),
    mob_residential NUMERIC(2, 6),
    search_hous_bubble INTEGER,
    search_pand_assist INTEGER,
    search_pfl INTEGER,
    search_recession INTEGER,
    search_unemp INTEGER,
	us_consumer_sentiment NUMERIC(3, 1)
);


INSERT INTO alternative_data (date)
SELECT generate_series('2005-01-01'::DATE, '2022-10-01'::DATE, '3 months'::INTERVAL) AS date;