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