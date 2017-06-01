# Python 3.4
'''
cd ~/documents/201510-whichdog
python3 url_checker_03.py
http://stackoverflow.com/questions/16778435/python-check-if-website-exists

sudo pip install requests
https://github.com/kennethreitz/requests

urlExists('http://www.yourpurebredpuppy.com/dogbreeds/photos-AB/bedlingtonterriersf3.jpg')

'''

import csv
import requests

def urlExists(path):
   r = requests.head(path)
   return r.status_code == requests.codes.ok

# Input file name
input_file_name = 'output_01_urlin_02.txt'

# Open input file
file_in = open(input_file_name, 'r')

# Output file name
output_file_name = 'output_url_01.txt'

# Open output file
with open(output_file_name,'a') as txtfile_out:

   for row in file_in:

      if(urlExists(row)): 

         txtfile_out.write(row)
         
         print(row)

# Close output file
txtfile_out.close()


