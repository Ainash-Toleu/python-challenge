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
monthly_changes = 0
average_changes = 0
greatest_increase = 0
greatest_decrease = 0
right_data = 0
right_data2 = 0

#opens the csv file for reading
with open (csvpath) as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =',')
    #skip the header row
    csv_header = next(csvfile)

    # reads through each row of data
    for row in csvreader:
        #puts in a list all months included in the dataset
        months_total.append(row[0])
        # calculates the net total amount of "Profit/Losses" over the entire period
        net_profit_losses += int(row[1])
        #add all the data in row 2 to a list
        monthly_profit_losses.append(row[1])
        # calculates changes by each month. Found the hit to the answer in StackOverflow
        monthly_changes = [int(x) - int(monthly_profit_losses[i - 1]) for i, x in enumerate(monthly_profit_losses) if i > 0]
        # calculates the sum of changes by each month
        sum_changes = sum(monthly_changes)
        
    

    # calculates average of changes 
    average_changes = round(sum_changes/len(monthly_changes), 2)
    # calculates greatest increase
    greatest_increase = max(monthly_changes)
    # calculates greatest decrease
    greatest_decrease = min(monthly_changes)
    
    right_data = [ x for i, x in enumerate(monthly_profit_losses) if (int(x) - int(monthly_profit_losses[i - 1])) == int(greatest_increase)]
    # print (right_data)
    # print(type(right_data))

    right_data2 = [ x for i, x in enumerate(monthly_profit_losses) if (int(x) - int(monthly_profit_losses[i - 1])) == int(greatest_decrease)]
    # print (right_data2)

    for row in csvreader:
        if row[1] == str(right_data):
            print (row[0])

# sets the variable for output file
output_path = os.path.join ("Analysis", "analysis.txt")

# opens the output file
with open (output_path, 'w', newline='') as textfile:
    # writes the answer to a textflie. Thanks to Stephanie that found this method in StackOverflow
    print ("Financial Analysis", file = textfile)
    print ("----------------------------", file = textfile)
    print (f'Total Months: {len(months_total)}', file = textfile)
    print (f'Total: $ {net_profit_losses}', file = textfile)  
    print (f'Average  Change: $ {average_changes}', file = textfile)
    print (f'Greatest Increase in Profits: ({greatest_increase})', file = textfile)
    print (f'Greatest Decrease in Profits: ({greatest_decrease})', file = textfile)


   
    


