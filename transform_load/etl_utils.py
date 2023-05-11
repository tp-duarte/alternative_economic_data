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


def transform_to_quarterly(data):

    date_col = data.columns[0]
    frequency = pd.infer_freq(data.index)
    
    if frequency == "MS": # MS means Month Start in pandas nomenclature
        
        quarterly = data.resample("QS").sum()
        
    return quarterly

    
def check_frequency(data):
    """
    Description: checks the frequency of which a time series occurs.
    
    Parameters:
    
    data (pd.DataFrame): A pandas DataFrame object. 
    
    Returns:
    
    frequency (str): A string containing the frequency type
    """
    
    ###
    
