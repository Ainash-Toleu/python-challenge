
#imports operating system module
import os 

#imports module for reading CSV files
import csv

total_ProfitLoss = 0  
csvpath = os.path.join ("Resources", "budget_data.csv")
#print (csvpath)

#open CSV file for reading
with open (csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')
    #print (csvreader)

# Read the header row first 
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # for row in csvreader:
    #     print (row)
   
    for row in csvreader:
        #The total number of months included in the dataset
        total = len (list(csvreader))
        print(f"Total Months: {total}")
        #The net total amount of "Profit/Losses" over the entire period
        total_ProfitLoss += int(row[1])
        print (f'Total: $ {total_ProfitLoss}')  
   
   


      










#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period