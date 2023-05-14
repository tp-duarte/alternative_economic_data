-- Creates the SQL tables for this project

CREATE TABLE traditional_data (
    date DATE PRIMARY KEY,
	gdp , 	
	employment ,	
	expenditure
	exports , 
	imports ,	
	min_wage ,
	personal_income ,
	disposable_income ,	
);


INSERT INTO traditional_data (date)
SELECT generate_series('2005-01-01'::DATE, '2022-10-01'::DATE, '3 months'::INTERVAL) AS date;
