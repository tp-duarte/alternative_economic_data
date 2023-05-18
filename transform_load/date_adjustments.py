import etl_utils as eu
import os
import pandas as pd

STAGING_2_1 = r"..\alternative_economic_data\data\traditional_data\staging_2"
STAGING_2_2 = r"..\alternative_economic_data\data\alternative_data\staging_2"
PROCESSED_1 = r"..\alternative_economic_data\data\traditional_data\processed"
PROCESSED_2 = r"..\alternative_economic_data\data\alternative_data\processed"

trad_files = eu.get_csv_files(STAGING_2_1)
alt_files = eu.get_csv_files(STAGING_2_2)

for file in trad_files:

    # file specifications
    
    file_name = os.path.basename(file)
    encoding = eu.encoding_detect(file)
    delimeter = eu.detect_delimiter(file)

    # reading and transforming data

    data = pd.read_csv(file, encoding=encoding, delimiter=delimeter)
    data = eu.transform_to_date(data)
    
    quarter = eu.transform_to_quarterly(data, file_name)
    quarter = quarter.query("index >= '2005-01-01' and index <= '2022-10-01'")
    
    # exporting data
    
    quarterly_data = eu.rename_file(file, "quarterly")
    quarterly_data_processed = eu.change_directory(quarterly_data, PROCESSED_1)
    quarter.to_csv(quarterly_data_processed)


for file in alt_files:
    
    # file specifications
    
    file_name = os.path.basename(file)
    encoding = eu.encoding_detect(file)
    delimeter = eu.detect_delimiter(file)
    
    # reading and transforming data

    data = pd.read_csv(file, encoding=encoding, delimiter=delimeter)
    data = eu.transform_to_date(data)
    
    quarter = eu.transform_to_quarterly(data, file_name)
    quarter = quarter.query("index >= '2005-01-01' and index <= '2022-10-01'")
    
    # exporting data
    
    quarterly_data = eu.rename_file(file, "quarterly")
    quarterly_data_processed = eu.change_directory(quarterly_data, PROCESSED_2)
    quarter.to_csv(quarterly_data_processed)