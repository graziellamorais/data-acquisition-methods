import requests
import csv

"""
1. Start by importing the csv module.
2. Use the .json() method to access the decoded JSON data and store it in a variable called r_json.
3. Now write the JSON data into a CSV file called commute_data.csv
After you write the data to the file, click on the file again to see it filled with your data.
"""

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

r_json = r.json()

with open('commute_data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r_json)