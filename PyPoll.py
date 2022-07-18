#Add our dependencies.
import csv 
import os 

#Assign a variable for the file to load a file from the path.
file_to_load = os.path.join("election_results.csv")

#Assign a variable to to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print each header row.
    headers = next(file_reader)
    print(headers)


# Using the with statement open the file as a text file.



# To do: perform analysis
#print (election_data)

# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Close the file.
#election_data.close()
