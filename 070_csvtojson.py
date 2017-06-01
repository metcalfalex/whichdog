# Python 3.4
'''
cd ~/documents/201510-whichdog
python3 csv_to_json_01.py
http://stackoverflow.com/questions/19697846/python-csv-to-json
'''

import json
import csv

# Input file name
input_file_name = 'output_01.csv'

# Output file name
output_file_name = 'output_02.json'

csvfile = open(input_file_name, 'r')
jsonfile = open(output_file_name, 'w')

fieldnames = ("parse_url","parse_width","parse_height","breed","adjective")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write('\n')


# MANUAL: (1) add [] at start and end; (2) replace all '}' with '},' 
