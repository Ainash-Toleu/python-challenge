#imports operating system module
import os 

#imports module for reading CSV files
import csv

csvpath = os.path.join ("Resources", "election_data.csv")

total_votes = []

#open CSV file for reading
with open (csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')
    
    # skip the header row 
    next(csvfile)
    for row in csvreader:
        total_votes.append(row[0])

    
print ("Election Results")
print ("-------------------------")
print (f'Total Votes: {len(total_votes)}')
print ("-------------------------")
    

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.