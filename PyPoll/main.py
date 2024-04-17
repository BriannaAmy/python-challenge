"""
The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote
"""
#import modules
import os
import csv

#load resource file
electionDataPath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#intialize tracking variables
totVotes = 0 #running total of all votes
candidateNames = [] #list to store candidate names
candidateVotes = [] #list to store num of candidate votes

#read and convert the csv file
with open(electionDataPath) as csvFile:
    electionDataReader = csv.reader(csvFile,delimiter=",")

    #skip the first row with the headers Ballot ID/County/Candidate
    electionHeaders = next(electionDataReader)

    #loop rest of data
    for row in electionDataReader:

        totVotes += 1 #running total of all votes

        #check for cadidate change
        if row[2] not in candidateNames:
            candidateNames.append(row[2]) #add candidate name to list
            candidateVotes.append(1) #initialize index to 1
        else:
            #increment candidate votes based on name
            candidateVotes[candidateNames.index(row[2])] += 1

#display results
print("\nElection Results\n---------------------------------------")
print(f"Total Votes: {totVotes}\n---------------------------------------")

#candidate vote percentages
for name in candidateNames:
    votePercent = round((candidateVotes[candidateNames.index(name)] / totVotes)*100,3)
    print(f"{name}: {votePercent}% ({candidateVotes[candidateNames.index(name)]})")

print("---------------------------------------")

#get highest number of votes to find winner
winner = candidateNames[candidateVotes.index(max(candidateVotes))]

print(f"Winner: {winner}\n---------------------------------------")

#write results in text file under analysis folder
analysisOutputPath = os.path.join("..", "PyPoll", "analysis", "analysis.txt")

with open(analysisOutputPath, "w") as text:

    text.write("\nElection Results\n---------------------------------------\n")
    text.write(f"Total Votes: {totVotes}\n---------------------------------------\n")

    for name in candidateNames:
        votePercent = round((candidateVotes[candidateNames.index(name)] / totVotes)*100,3)
        text.write(f"{name}: {votePercent}% ({candidateVotes[candidateNames.index(name)]})\n")
    
    text.write("---------------------------------------\n")
    text.write(f"Winner: {winner}\n---------------------------------------")