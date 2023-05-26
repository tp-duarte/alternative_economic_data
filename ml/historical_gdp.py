'''
Objective:

This python file gathers data from AWS RDS and turns into a pandas.DataFrame 
that it's exported to a csv file in the ml_data folder.

'''

import pandas as pd
import ml_utils as mu
import psycopg2

try:
    db = psycopg2.connect(
        host="aws-california.caclwjj7hnoo.us-east-2.rds.amazonaws.com",
        database="california",
        user="postgres",
        password="24567811"
    )
    cursor = db.cursor()
    print("Connected to the database!")
    
    # Perform database operations here
    
except psycopg2.Error as e:
    print("Error connecting to the database:", e)


query = "SELECT date, gdp FROM traditional_data"


historical_file = r"..\alternative_economic_data\data\ml_data\historical_gdp.csv"

historical_gdp = mu.query_into_df(query, cursor)
historical_gdp.to_csv(historical_file, index=False)