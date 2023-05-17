import etl_utils as eu
import pandas as pd 
import os

STAGING_1_1 = r"..\data\traditional_data\staging_1"
STAGING_1_2 = r"..\data\alternative_data\staging_1"

STAGING_2_1 = r"..\data\traditional_data\staging_2"
STAGING_2_2 = r"..\data\alternative_data\staging_2"

trad_files = eu.get_csv_files(STAGING_1_1)
alt_files = eu.get_csv_files(STAGING_1_2)

personal_income = "cali-quarterly-personal_income.csv"
expenditure = "cali-annual-expenditure.csv"
google_trends = "cali-monthly-google_trends.csv"
mobility_report = "us-daily-mobility_report.csv"
consumer_sentiment = "us-monthly-consumer_sentiment.csv"


for file in trad_files: 
    file_name = os.path.basename(file)
    
    # reading file
    
    encoding = eu.encoding_detect(file)
    delimeter = eu.detect_delimiter(file)           
    
    data = pd.read_csv(file, encoding=encoding, delimiter=delimeter)

    # doing general data transformations

    if file_name == personal_income:

        replacements = {
            ":Q1" : "-01-01",
            ":Q2" : "-04-01",
            ":Q3" : "-07-01",
            ":Q4" : "-10-01",            
                        } 
                
        data["date"] = data["date"].replace(replacements, regex=True)


for file in alt_files:
    
    # reading files 
    
    file_name = os.path.basename(file)
    encoding = eu.encoding_detect(file)
    delimeter = eu.detect_delimiter(file)   
    
    data = pd.read_csv(file)
    
    # doing general data transformations
    
    if file_name == google_trends:
        
        data = data.replace("<1", "0")  # replacing unformatted numbers
        
    elif file_name == mobility_report:
        
        date_col = data.pop('date')  
        data.insert(0, 'date', date_col)   # querying file for california data 
        data = data.query("state == 'California'")
        
        file = eu.get_modified_file_path(file_name, "cali-daily-mobility_report.csv")
    
    elif file_name == consumer_sentiment:
        
        data[["Month", "Year"]] = data[["Month", "Year"]].astype(str) # adjusting date string 
        date_series = data['Year'] + "-" + data['Month']
        data.insert(0, "date", date_series)

    # exporting data to second staging area
    
    file = eu.change_directory(file, STAGING_2_2)
    data.to_csv(file, index=False)   


