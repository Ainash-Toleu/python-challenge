#imports operating system module
import os
#imports module for reading csv files
import csv

#sets the path for file
csvpath = os.path.join ("Resources", "budget_data.csv")

#creates a list to store data
months_total = []
monthly_profit_losses = []

#creates a variable with an integer
net_profit_losses = 0

#open the csv file for reading
with open (csvpath) as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =',')
    #skip the header
    next(csvfile)
    #loops through csvreader
    for row in csvreader:
        #The total number of months included in the dataset
        months_total.append(row[0])
        # The net total amount of "Profit/Losses" over the entire period
        net_profit_losses += int(row[1])
        #add all the data in row 2 to a list
        monthly_profit_losses.append(row[1])
        monthly_changes = [int(x) - int(monthly_profit_losses[i - 1]) for i, x in enumerate(monthly_profit_losses) if i > 0]
        sum_changes = sum(monthly_changes)
        
        
 #print out the result
    average_changes = round(sum_changes/len(monthly_changes), 2)
    print (f'Total Months: {len(months_total)}')
    print (f'Total: $ {net_profit_losses}')  
    print (f'Average  Change: $ {average_changes}')
    # print (len(monthly_changes))
    # print (sum_changes)
    

