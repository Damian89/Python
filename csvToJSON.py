import csv
import json


# Function to convert a CSV to JSON
# CSV file has to have the first row with column ID
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):

	# create a dictionary
	data = {}

	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)

		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:

			# Assuming a column named 'Account' to
			# be the primary key
			key = rows['Account']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))

# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'/Users/hdquemada/Desktop/access.csv'
jsonFilePath = r'/Users/hdquemada/Desktop/access.json'

# Call the make_json function
make_json("/Users/hdquemada/Desktop/access.csv", "/Users/hdquemada/Desktop/access.json")
