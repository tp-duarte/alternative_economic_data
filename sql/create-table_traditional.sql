-- Creates the SQL table that contains traditional data for this project

CREATE TABLE traditional_data (
    date DATE PRIMARY KEY,
	gdp NUMERIC (7, 1), 	
	employment NUMERIC (6, 1),	
	expenditure NUMERIC (7, 3),
	exports NUMERIC (5, 6), 
	imports NUMERIC (5, 6),	
	min_wage NUMERIC (2, 2),
	personal_income NUMERIC (7, 1),
	disposable_income NUMERIC (7, 3)	
);


INSERT INTO traditional_data (date)
SELECT generate_series('2005-01-01'::DATE, '2022-10-01'::DATE, '3 months'::INTERVAL) AS date;
