import chardet as ct

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

	print("Encoding detected.")

	return encoding

