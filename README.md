# Module 3 Challenge - Election Audit

## Overview of the Election Audit
The purpose of this analysis is to perform an election audit on election data to provide the following information to the Colorado Board of Elections:
 - Total number of votes cast in the election
 - Total number of votes and vote percentage for each county in the election
 - County with the largest number of votes cast
 - Total number of votes and vote percentage for each candidate in the election
 - The winning candidate


## Resources
The following resources were used to perform this analysis
- Data Source: election_results.csv
- Software: Python 3.7.5, Visual Studio Code 1.58.0


## Election Audit Results
The results of the election audit are as follows (see link for results output: https://github.com/pmoores/Election_Analysis/blob/main/analysis/election_analysis.txt): 

 - There were 369,711 votes cast in the election

### County Results
 - Denver received 306,055 votes for 82.8% of the total vote
 - Jefferson received 38,855 votes for 10.5% of the total vote
 - Arapahoe received 24,801 for 6.7% of the total vote.  

 - Denver had the largest number of votes with 306,055 for 82.8% of the total vote

### Candidate Results
 - Diana DeGette received 272,892 votes for 73.8% of the total vote
 - Charles Casper Stockham received 85,213 votes for 23.0% of the total vote
 - Raymon Anthony Doane received 11,606 votes for 3.1% of the total vote.  

 - Diana DeGette won the election with 272,892 votes for 73.8% of the total vote.


## Election Audit Summary: 
The script used for this coding audit successfully retrieved vital information about the proportion of votes received by each candidate and votes cast from each county. This script is also very versatile and can be used to perform other analyses:
 - Example 1: The code can be expanded with very little modification to compare election results between numerous counties and candidates. In fact, this would be as simple as loading a different csv data file.
 - Example 2: A wide variety of statistical analysis methods can be run on this data to create a deeper analysis. For instance, the voting percentages from numerous counties can be compared to determine voter engagement in each county and develop strategies to increase voter engagement where needed.
