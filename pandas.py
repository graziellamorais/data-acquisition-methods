"""
1. Start by importing the pandas library.
2. Create a variable called commute_df. Set your variable to be a pandas DataFrame from the commute_data.csv file you created in the last exercise.
3. Preview the first few rows of commute_df using the .head() method and print out the output.
4. Rename the headings to more descriptive names, then print the first few rows of the DataFrame again to see the changes.
"""

import pandas

commute_df = pandas.read_csv("commute_data.csv")

print(commute_df.head())

commute_df.columns = ['name', 'total_commuters', '90_or_more', 'state', 'county']

print(commute_df.head())