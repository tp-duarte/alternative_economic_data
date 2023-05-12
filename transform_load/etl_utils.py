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
    
    date_col = data.columns[0]
    data[date_col] = pd.to_datetime(data[date_col]) 

    data.set_index(date_col, inplace=True)
    
    return data


def file_in_list(target_string, string_list):
    """
    Description:
    
    Parameters:
    
    Returns:
    
    """
    
    for string in string_list:
        if target_string == string:
            return True
    return False



def transform_to_quarterly(data, file_name):
    
    exports = "cali-monthly-exports.csv"
    imports = "cali-monthly-imports.csv"
    employment = "cali-monthly-employment.csv"
    minimum_wage = "cali-annual-minimum_wage.csv"
    google_trends = "cali-monthly-google_trends.csv"
    consumer_sentiment = "us-monthly-consumer_sentiment.csv"
    mobility_report = "cali-daily-mobility_report.csv"

    quarterly_agreggates = [exports, imports] 
    quarterly_averages = [employment, google_trends, consumer_sentiment, mobility_report] 
    
    frequency = pd.infer_freq(data.index)
    
    if frequency == "MS" and file_in_list(file_name, quarterly_agreggates) : # 'MS' means Month Start in pandas nomenclature
        quarterly = data.resample("QS").sum()
    
    elif (frequency == "MS" or file_name == mobility_report) and file_in_list(file_name, quarterly_averages):
        quarterly = data.resample("QS").mean()
    
    elif frequency == "AS-JAN" and file_name == minimum_wage: # 'AS' means Annual Start and 'JAN' indicates that it starts in january.
        quarterly = data.resample("QS").ffill()     
    
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
