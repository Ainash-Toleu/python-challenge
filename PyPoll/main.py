#imports operating system module
import os 
#imports module for reading CSV files
import csv

csvpath = os.path.join ("Resources", "election_data.csv")

total_votes = []
candidates_list = []
unique_candidate_list = [] 
votes_for_candidate = []
           
#open CSV file for reading
with open (csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')
    # skip the header row 
    next(csvfile)
    for row in csvreader:
        #The total number of votes cast
        total_votes.append(row[0])
        #A complete list of candidates who received votes
        candidates_list.append(row[2])

    for name in candidates_list: 
        if name not in unique_candidate_list and name != " ": 
            unique_candidate_list.append(name)   

    for x in unique_candidate_list:
        for y in candidates_list:
            if str(x) == str(y):
                votes_for_candidate.append(y)

    dictionary = {}
    for votes in votes_for_candidate:
        
        dictionary.setdefault(votes, 0)
        dictionary[votes] += 1
    max_key =  max (dictionary, key = dictionary.get)  

output_path = os.path.join ("Analysis", "analysis.txt")

with open (output_path, 'w', newline='') as textfile:
    print ("Election Results", file = textfile)
    print ("-------------------------", file = textfile)
    print (f'Total Votes: {len(total_votes)}', file = textfile)
    print ("-------------------------", file = textfile)  

    for votes, count in dictionary.items():
        percentage = float(int(count)/len(total_votes))
        percent = "{:.3%}". format(percentage)
        print("{} : {} ({})".format (votes, percent, count), file = textfile) 

    print ("-------------------------", file = textfile)
    print (f"Winner: {max_key}", file = textfile)
    print ("-------------------------", file = textfile)


