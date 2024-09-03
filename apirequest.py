import requests

#r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*')

# Access data as JSON string
#print(r.text)

# Access decoded JSON data as Python object
#print(r.json())

"""
1. Make a GET request to the Census API to request county-level data containing

the NAME variable,
the total commuters count, and
the count for commuters who travel 90 or more minutes
for all counties
within the state of New York.

2. Use the .text attribute to access the returned string data and store it in a variable called r_text.

Try printing r_text with the print(___) command.

3. Use the .json() method to access the decoded JSON data and store it in a variable called r_json. Try printing out r_json.
"""

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36') 

r_text = r.text
print(r_text)

r_json = r.json()
print(r_json)