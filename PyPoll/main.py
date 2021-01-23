#imports operating system module
import os 
#imports module for reading CSV files
import csv

# sets the path for file
csvpath = os.path.join ("Resources", "election_data.csv")

#creates a list to store data
total_votes = []
candidates_list = []
unique_candidate_list = [] 
# votes_for_candidate = []
           
#opens CSV file for reading
with open (csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')
    # skips the header row 
    csv_header = next(csvfile)

    # reads through each row of data
    for row in csvreader:
        #puts in a list total number of votes 
        total_votes.append(row[0])
        #puts in a list votes for each candidate
        candidates_list.append(row[2])
    # finds unique names of candidates from candidate list
    for name in candidates_list: 
        if name not in unique_candidate_list: 
            unique_candidate_list.append(name)   
    # makes a dictionary that counts all the votes each candidate had. Found the hint to the answer in StackOverflow.
    dictionary = {}
    for votes in candidates_list:
        dictionary.setdefault(votes, 0)
        dictionary[votes] += 1
    #calculates the winner 
    max_key =  max (dictionary, key = dictionary.get)  

# sets the variable for output file
output_path = os.path.join ("Analysis", "analysis.txt")

# opens the output file
with open (output_path, 'w', newline='') as textfile:
    # writes the answer to a textflie. Thanks to Stephanie that found this method in StackOverflow
    print ("Election Results", file = textfile)
    print ("-------------------------", file = textfile)
    print (f'Total Votes: {len(total_votes)}', file = textfile)
    print ("-------------------------", file = textfile)  
    # adds a percentage in dictionary and writes to a textfile
    for votes, count in dictionary.items():
        percentage = float(int(count)/len(total_votes))
        percent = "{:.3%}". format(percentage)
        print("{} : {} ({})".format (votes, percent, count), file = textfile) 
    # writes the winner to a textfile
    print ("-------------------------", file = textfile)
    print (f"Winner: {max_key}", file = textfile)
    print ("-------------------------", file = textfile)


