
import os
import csv

from csv import reader
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader, None)

#create a Python script that analyzes the records to calculate each of the following:

    #The total number of months included in the dataset
     month = 0
     total_count  = 0
     months = []
     revenue = []
     net_change = []

for row in csvreader:
        month = month + 1
        months.append(row[0])
  
    # The net total amount of "Profit/Losses" over the entire period
        
        total_count = total_count + float(row[1])
        revenue.append(float(row[1]))


    #The average of the changes in "Profit/Losses" over the entire period
   
for i in range(1,len(revenue)):
        net_change.append(revenue[i] - revenue[i-1])   
        average = round(sum(net_change)/len(net_change), 2)
        max_net_change_date = str(months[net_change.index(max(net_change))])
        min_net_change_date = str(months[net_change.index(min(net_change))])
        

    # Save in text file
with open("PyBank.txt", "w") as txtfile:
        txtfile.write(f"Financial Analysis \n")
        txtfile.write(f"Total P&L: ${total_count} \n")
        txtfile.write(f"Average Change: ${average} \n")
        txtfile.write(f"Greatest Increase in Profits: {max(net_change)} \n")
        txtfile.write(f"Greatest Decrease in Profits: {min(net_change)} \n")
        txtfile.close()

# Print
print("Financial Analaysis")
print("------------------------------")
print(f"Total Months: {month}") 
print(f"Total P & L: ${total_count}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {max_net_change_date} ({max(net_change)})")
print(f"Greatest Decrease in Profits: {min_net_change_date} ({min(net_change)})")