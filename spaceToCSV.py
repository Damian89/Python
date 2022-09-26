import sys

with open('/Users/hdquemada/Desktop/access.txt') as infile:

    # Read space-delimited file and replace all empty spaces by commas
    data = infile.read().replace(' ', ',')

    # Write the CSV data in the output file
    print(data, file=open('/Users/hdquemada/Desktop/access.csv', 'w'))