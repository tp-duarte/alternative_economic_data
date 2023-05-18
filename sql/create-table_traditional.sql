-- Creates the SQL table that contains traditional data for this project

CREATE TABLE traditional_data (
    date DATE PRIMARY KEY,
	gdp NUMERIC (8, 1), 	
	employment NUMERIC (11, 4),	
	expenditure NUMERIC (10, 3),
	exports NUMERIC (12, 6), 
	imports NUMERIC (12, 6),	
	min_wage NUMERIC (4, 2),
	personal_income NUMERIC (8, 1),
	disposable_income NUMERIC (10, 3)	
);


INSERT INTO traditional_data (date)
SELECT generate_series('2005-01-01'::DATE, '2022-10-01'::DATE, '3 months'::INTERVAL) AS date;
