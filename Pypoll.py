# Import csv and os modules / Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# The data we need to retrieve
# 1. Initialize a vote counter to zero
total_votes = 0

# Initialize Candidate Options variable
candidate_options = []

# Declare empty candidate votes dictionary
candidate_votes = {}

# Winning candidate and winning count tracker: empty variable to hold value of winning candidate and two variable set to zero
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results using a with statement
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the csv file
    for row in file_reader:
        # 2. Add to the total votes count
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add it to the list of candidates
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count:
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to a text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    # 1 Iterate though the candidate list
    for candidate_name in candidate_votes:
        #2 Retrieve the vote count and percentage
        votes = candidate_votes[candidate_name]
        #3 Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's vote count percentage to terminal
        print(candidate_results)

        # Save the candidate result to text file
        txt_file.write(candidate_results)


        # 4 Print the candidate name and percentage of votes and format percentage to one decimal place
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # {vote_percentage:.1f}% ({votes:.})\n")

        # To do: print out each candidate's name, vote count, and percentage of number of votes


        # Determine winning vote count and candidate
        # Determine if the number of votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------- \n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
