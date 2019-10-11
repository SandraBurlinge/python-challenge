import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
file_output = "PyPoll.txt"

# create a list to store the values:
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""

# set file path and open
# # split the data on commas

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    
# The total number of votes cast
# A complete list of candidates who received votes
    for row in csvreader:
    
        total_votes+= 1
       
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

    
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]

print ("Election Results")

print ("-------------------------------------")

print ("Total Votes:" + str(total_votes))

print ("-------------------------------------")

print (key + ":" + str(candidates_percent[key]) + "% (" + str(value) + ")")

print ("-------------------------------------")

print ("Winner: " + winner)

print ("-------------------------------------")


with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")