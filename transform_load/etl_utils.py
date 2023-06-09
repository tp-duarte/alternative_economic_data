'''
Objective:

This python module contains functions that are used in the ETL steps of the project.
It enables the ETL in the following files:

- general_treatments.py
- date_adjustments.py
- inserting_data.py

The module contains functions for:

- Folder and operational system procedures;
- File's encoding and delimiters detection;
- Date aggregations and transformations. 

'''

import chardet as ct
import glob
import os
import pandas as pd


def detect_delimiter(file_path):
	"""
	Description: Detects the delimiter of a csv file after reading lines.

	Parameters:

        file_path (str): A string containing the file path. Preferrably the path is specified with two backslashs.

	Returns:

        best_delimiter (str): A string containing the best delimiter.
        
	"""

    # Open the file and read the first few lines
	with open(file_path, 'r') as f:
		lines = [next(f) for x in range(10)]

	# Try each possible delimiter and count the number of fields
	delimiters = [',', ';', '\t', '|']  # Possible delimiters
	max_fields = 0
	best_delimiter = None

	for delimiter in delimiters:
		field_counts = [len(line.split(delimiter)) for line in lines]
		total_fields = sum(field_counts)

		if total_fields > max_fields:
			max_fields = total_fields
			best_delimiter = delimiter

	return best_delimiter


def encoding_detect(data_path):
	"""
	Description: encoding detection for files

	Parameters:

        data_path (str): A string containing the path of the data, preferrably with two backslashs for each folder.

    Returns:
    
        encoding (str): A string containing the encoding of the file
    
	"""
	with open(data_path, 'rb') as f:
		lines = []
		for i in range(5):
			line = f.readline()
			if not line:
				break
			lines.append(line)
		result = ct.detect(b''.join(lines))

	encoding = result['encoding']

	return encoding

def get_csv_files(path):
    """
    Description: Gets the csv files that are inside a folder.
    
    Parameters:
    
        path (str): A string containing the path of the data.
    
    Returns:
    
        csv_files (list): A list containing the path of each csv file.
    """
    csv_files = []
    
    if os.path.exists(path):
        
        if os.path.isdir(path):
            csv_files = glob.glob(os.path.join(path, "*.csv"))
            
            return csv_files
            
        else:
            print("The specified path is not a directory.")
    else:
        print("The specified path does not exist.")


def transform_to_date(data):
    """
    Description: Transforms the date column of a pandas DataFrame into a datetime format.
    It also sets the date as index.
    
    Parameters:
    
        data (pd.DataFrame): A pandas DataFrame to be transformed.
    
    Returns:
    
        data (pd.DataFrame): A pandas DataFrame with date values transformed.  
        
    """
    
    date_col = data.columns[0]
    data[date_col] = data[date_col].astype(str)
    data[date_col] = pd.to_datetime(data[date_col]) 

    data.set_index(date_col, inplace=True)
    
    return data


def file_in_list(string_eval, string_list):
    """
    Description: Checks if a string is contained is a list of strings.
    
    Parameters:
    
        string_eval (str): A string to be evaluated;
        string_list (list): A list containing strings.
    
    Returns:
    
        True or False (boolean): Returns if the string is contained or not in the strings list.
        
    """
    
    for string in string_list:
        if string_eval == string:
            return True
    return False


def transform_to_quarterly(data, file_name):
    """
    Description: Resampling of the data files of the project. This function aggregates the file
    to a quarterly frequency, using methods that matches the necessities of the files.
    
    Parameters:
    
        data (pd.DataFrame): A pandas DataFrame to be resampled;
        file_name (str): A string of the file being processed at the time.
    
    Returns:
    
        quarterly (pd.DataFrame): A DataFrame containing the resampled quarterly data.
        
    """
    
    gdp = "cali-quarterly-gdp.csv"
    expenditure = "cali-annual-expenditure.csv" 
    disposable_income = "cali-annual-disposable_income.csv"    
    exports = "cali-monthly-exports.csv"
    imports = "cali-monthly-imports.csv"
    employment = "cali-monthly-employment.csv"
    minimum_wage = "cali-annual-minimum_wage.csv"
    personal_income = "cali-quarterly-personal_income.csv"
    google_trends = "cali-monthly-google_trends.csv"
    consumer_sentiment = "us-monthly-consumer_sentiment.csv"
    mobility_report = "cali-daily-mobility_report.csv"

    quarterly_agreggates = [exports, imports] 
    quarterly_averages = [employment, google_trends, consumer_sentiment, mobility_report]
    quarterly_disaggregates = [disposable_income, expenditure] 
    
    frequency = pd.infer_freq(data.index)
    
    if frequency == "MS" and file_in_list(file_name, quarterly_agreggates): # 'MS' means Month Start in pandas nomenclature
        quarterly = data.resample("QS").sum()
    
    elif (frequency == "MS" or file_name == mobility_report) and file_in_list(file_name, quarterly_averages):
        quarterly = data.resample("QS").mean()
        
    elif frequency == "AS-JAN" and file_in_list(file_name, quarterly_disaggregates): # 'AS' means Annual Start and 'JAN' indicates that it starts in january.
        quarterly = data.asfreq("QS").ffill()
        quarterly = quarterly / 4
        
    elif frequency == "AS-JAN" and file_name == minimum_wage: 
        quarterly = data.resample("QS").ffill()
    
    else:
        return data
    
    return quarterly

    
def get_modified_file_path(file_path, new_file_name):
    """
    Get the modified file path given the file path and the desired new file name.

    Parameters:
        file_path (str): The path of the file.
        new_file_name (str): The new name to be assigned to the file.

    Returns:
        str: The modified file path with the new file name.
    """
    
    directory, current_file_name = os.path.split(file_path)
    new_file_path = os.path.join(directory, new_file_name)
    
    return new_file_path


def change_directory(file_path, new_directory):
    """
    Change the directory of a file while preserving the file name and extension.

    Parameters:
        file_path (str): The original file path.
        new_directory (str): The new directory path.

    Returns:
        str: The modified file path with the same file name and extension in the new directory.
    """
    directory, file_name = os.path.split(file_path)
    new_file_path = os.path.join(new_directory, file_name)
    
    return new_file_path


def rename_file(file_path, new_name):
    """
    Renames the second part of a file path while preserving the file name and extension.

    Parameters:
        file_path (str): The original file path.
        new_name (str): The new name to replace the second part of the file path.

    Returns:
        str: The modified file path with the same file name and extension.
    """

    directory, filename = os.path.split(file_path)
    base_name, extension = os.path.splitext(filename)
    name_parts = base_name.split('-')

    name_parts[1] = new_name
    new_base_name = '-'.join(name_parts)
    new_file_name = new_base_name + extension
    new_file_path = os.path.join(directory, new_file_name)

    return new_file_path


def get_numeric_scale(cursor, table_name):
    """
    Description: This function produces a dictionary mapping of SQL NUMERIC column names and their decimal scale.
    
    Parameters:
    
        cursor (psycopg2.cursor): A Postgres cursor to execute the statement;
        table_name (str): A string containing the name of the table to make the mapping.
    
    Returns:
    
        mapping (dict): A dictionary containing sql columns as keys and their numeric scale as values. 
        
    """
    
    sql_query = "SELECT column_name, numeric_scale FROM information_schema.columns " \
                f"WHERE table_name = '{table_name}'"
    
    cursor.execute(sql_query)
    result = cursor.fetchall()
    
    mapping = {}
    
    for var in result:
        var_name = var[0]
        var_scale = var[1]
        mapping[var_name] = var_scale
    
    return mapping


def apply_rounding(mapping_dict, data, cursor, table_name):
    """
    Description: Applies a rounding in float columns of a dataframe accordingly to the format of the SQL table
    provided.
    
    Parameters:
    
        mapping_dict (dict): A mapping dictionary with datframe to sql columns; 
        data (pd.DataFrame): A pandas dataframe to apply the function;
        cursor (psycopg2.cursor): A Postgres cursor for the operation;
        table_name (str): A string containing the name of the table of the desired numeric scale.
    
    Returns:
    
        data (pd.DataFrame): A pandas dataframe with the rounded data.

    """
    
    inverted_dict = {value: key for key, value in mapping_dict.items()}    
    cols_to_round = get_numeric_scale(cursor, table_name)

    for col, decimal_place in cols_to_round:
        
        df_col = inverted_dict[col]
        data[df_col] = data[df_col].round(decimal_place)
    
    return data