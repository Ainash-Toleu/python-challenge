#imports operating system module
import os 

#imports module for reading CSV files
import csv

csvpath = os.path.join ("Resources", "election_data.csv")
print (csvpath)

#open CSV file for reading
with open (csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')
    print (csvreader)

# Read the header row first 
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")    

    # for row in csvreader:
    #     print (row)

    

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.