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
monthly_changes = []
average_changes = 0
greatest_increase = 0
greatest_decrease = 0
right_data = 0
right_data2 = 0

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
        # if monthly_changes > greatest_increase:
        #     greatest_increase = row[0]
        sum_changes = sum(monthly_changes)
        
    for row in csvreader:
        print(row[0])

    average_changes = round(sum_changes/len(monthly_changes), 2)
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)
    
    right_data = [ x for i, x in enumerate(monthly_profit_losses) if (int(x) - int(monthly_profit_losses[i - 1])) == int(greatest_increase)]
    print (right_data)
    print(type(right_data))

    right_data2 = [ x for i, x in enumerate(monthly_profit_losses) if (int(x) - int(monthly_profit_losses[i - 1])) == int(greatest_decrease)]
    print (right_data2)

    
        # if row[1] == str(right_data):
        #     print (row[0])

    #print out the result
    print ("Financial Analysis")
    print ("----------------------------")
    print (f'Total Months: {len(months_total)}')
    print (f'Total: $ {net_profit_losses}')  
    print (f'Average  Change: $ {average_changes}')
    print (f'Greatest Increase in Profits: ({greatest_increase})')
    print (f'Greatest Decrease in Profits: ({greatest_decrease})')
   
    


