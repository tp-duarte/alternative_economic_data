-- Alternative data with gdp 


COPY (
	SELECT alt.*, trad.gdp
	FROM traditional_data AS trad
	JOIN alternative_data AS alt ON trad.date = alt.date
)

TO 'D:\articles\alternative_economic_data\data\ml_data\alt_gdp.csv' 
WITH (FORMAT CSV, HEADER);

-- Traditional data 

COPY (
	SELECT trad.*
	FROM traditional_data AS trad
)

TO 'D:\articles\alternative_economic_data\data\ml_data\trad_gdp.csv' 
WITH (FORMAT CSV, HEADER);


-- All data 

COPY (
	SELECT trad.*, alt.*
	FROM traditional_data AS trad
	FULL OUTER JOIN alternative_data AS alt 
	ON trad.date = alt.date
)


TO 'D:\articles\alternative_economic_data\data\ml_data\all_gdp.csv' 
WITH (FORMAT CSV, HEADER);

