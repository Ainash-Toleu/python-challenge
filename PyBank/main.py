#imports operating system module
import os
#imports module for reading csv files
import csv

#sets the path for file
csvpath = os.path.join ("Resources", "budget_data.csv")

#creates a list to store data
total_month = []
#creates a variable with an integer
total_profit_losses = 0

#open the csv file for reading
with open (csvpath) as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =',')
    #skip the header
    next(csvfile)
    #loops through csvreader
    for row in csvreader:
        #The total number of months included in the dataset
        total_month.append(row[0])
        # The net total amount of "Profit/Losses" over the entire period
        total_profit_losses += int(row[1])
    #print out the result
    print (f'Total Months: {len(total_month)}')
    print (f'Total: $ {total_profit_losses}')   