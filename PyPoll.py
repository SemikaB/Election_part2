# The data we need to retrieve
# 1. The total number of vite cast
# 2. A complete list of canidates who received votes 
# 3. The percentage of votes each candidate won
# 5. The winner of the election based on popular votes.
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
print("Hello")
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
  file_reader = csv.reader(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
  txt_file.write("Hello World")
# Write three counties to the filetxt_file.write("Arapahoe")
txt_file.write("Denver")
txt_file.write("Jefferson")
# Write three counties to the file.
txt_file.write("Arapahoe,")
txt_file.write("Denver,")
txt_file.write("Jefferson")
 # Write three counties to the file.
txt_file.write("Arapahoe, Denver, Jefferson")
# Write three counties to the file.
# Write three counties to the file.
txt_file.write("Arapahoe\nDenver\nJefferson")
import csv
# Get the sum of the fares for each city type.
sum_fares_by_type = pyber_data_df.groupby(["type"]).sum()["fare"]
sum_fares_by_type