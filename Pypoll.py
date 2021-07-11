# Import csv and os modules / Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the file using a with statement
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read a print the header row
    headers = next(file_reader)
    print(headers)


# Open the election results and read the file (using 'with statement')
# with open(file_to_load) as election_data:

    # Print the filename object
    # print(election_data)

# Create a filename variable to a direct or indirect path to the file
# file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open() function with the "w" mode to write data to the file
# open(file_to_save, "w")


# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who revieved votes
# 3. The opercentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election nased on popular vote.

# Close the file.
# election_data.close()
