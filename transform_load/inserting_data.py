import etl_utils as eu
import pandas as pd 
import psycopg2

PROCESSED_1 =  r"..\alternative_economic_data\data\traditional_data\processed"
PROCESSED_2 =  r"..\alternative_economic_data\data\alternative_data\processed"
TRAD_TABLE_NAME = "traditional_data"
ALT_TABLE_NAME = "alternative_data"

trad_files = eu.get_csv_files(PROCESSED_1)
alt_files = eu.get_csv_files(PROCESSED_2)
all_files = trad_files + alt_files

df_sql = {
    "disposable_income": "disposable_income",
    "expenditure": "expenditure",
    "STTMINWGCA": "min_wage",
    "CANA": "employment",
    "EXPTOTCA": "exports",
    "IMPTOTCA": "imports",
    "CANQGSP": "gdp",
    "personal_income": "personal_income", 
    "retail and recreation": "mob_leisure",
    "parks": "mob_parks",    
    "grocery and pharmacy": "mob_groc_pharm",
    "transit stations": "mob_transit",
    "workplaces": "mob_workplaces",
    "residential": "mob_residential",
    "Housing bubble: (Califórnia)" : "search_hous_bubble",
    "pandemic unemployment assistance california: (Califórnia)": "search_pand_assist",
    "California Paid Family Leave  PFL: (Califórnia)": "search_pfl",
    "Recession: (Califórnia)": "search_recession",
    "Unemployment benefits: (Califórnia)": "search_unemp",
    "Index": "us_consumer_sentiment"   
    }

key_value_list = list(df_sql.items())

trad_list = key_value_list[0:8]
alt_list = key_value_list[8:]

trad_dict = dict(trad_list)
alt_dict = dict(alt_list)


connection = psycopg2.connect(
    database="california",
    user="postgres",
    password="0000",
    host="localhost",
    port="5433"
)

cursor = connection.cursor()

cursor.execute("SELECT date FROM traditional_data")
date_values = cursor.fetchall()

for file in all_files:
    
    encoding = eu.encoding_detect(file)
    delimiter = eu.detect_delimiter(file)
    df = pd.read_csv(file, encoding=encoding, delimiter=delimiter)

    df_vars = [column for column in df.columns if column in df_sql.keys()]
    sql_vars = [df_sql[column] for column in df.columns if column in df_sql]
    
    condition_1 = all(var in trad_dict for var in df_vars)
    condition_2 = all(var in alt_dict for var in df_vars)
    
    if condition_1 or condition_2:
        table_name = TRAD_TABLE_NAME if condition_1 else ALT_TABLE_NAME
        
        df = eu.apply_rounding(df_sql, df, cursor, table_name)

        for date_value in date_values:
            
            date_value = date_value[0]
            date_col = df.columns[0]
            df[date_col] = pd.to_datetime(df[date_col], format='%Y-%m-%d')
            filtered_df = df.query(f"{date_col} == '{date_value}'")
            
            if filtered_df.empty:
                continue
            
            try:
                values = [filtered_df[column].to_list()[0] for column in df_vars]
                values = tuple(values)
                
                set_clause = ', '.join([f"{column} = %s" for column in sql_vars]) # output example : column_1 = %s, column_2 = %s, ....  
                
                query = f"UPDATE {table_name} " \
                        f"SET {set_clause} " \
                        f"WHERE date = '{date_value}'; " 
                
                cursor.execute(query, values)
                connection.commit()

            except (Exception, psycopg2.Error) as error:
                connection.rollback()  # Roll back the transaction
                print("Error while inserting", error, values, file)
