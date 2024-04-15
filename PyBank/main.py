"""
Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
"""
#import modules
import os
import csv

#load the resource file
budgetPath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#tracking variables
totMonths = 0
totNetProfit_Loss = 0
netChanges = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999999]

#read the csv file and convert
with open(budgetPath) as csvFile:
    
    #use csv.reader() function to break everything up based on the ',' delimiter
    budgetReader = csv.reader(csvFile, delimiter=",")

    #skip the headers in the first row: index 0 = date/month, index 1 = profit/loss
    budgetHeader = next(csvFile)

    totMonths += 1 #add one to months

    firstRow = next(budgetReader) #pull first row data
    totNetProfit_Loss += float(firstRow[1]) #add first row index 1 data to total net profit/loss
    previousProfit_Loss = float(firstRow[1]) #initializing previous variable to calculate netChanges

    #loop through rest of the data by row
    for row in budgetReader:

        totMonths += 1 #add to total months
        totNetProfit_Loss += float(row[1]) #running total of net profits/losses
        netChangeCalc = float(row[1]) - previousProfit_Loss #net changes calculation
        netChanges.append(netChangeCalc) #append net changes calculation to netChanges list
        previousProfit_Loss = float(row[1]) #reset previous profit/loss to use for next calculation
        
        if netChangeCalc > greatestIncrease[1]: #check for greatest net change increase and populate list if true
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = netChangeCalc
        
        if netChangeCalc < greatestDecrease[1]:#check for greatest net change decrease and populate list if true
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = netChangeCalc

netMonthlyAvg = sum(netChanges) / len(netChanges) #calculate net changes monthly average 

#display results:
print("Financial Analysis \n--------------------------------")
print(f"Total Months: {totMonths}")
print(f"Total: ${totNetProfit_Loss:,.2f}")
print(f"Average Change: ${netMonthlyAvg:,.2f}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:,.2f})")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:,.2f})")

#write to a text file 'analysis.txt'
analysisOutputPath = os.path.join("..", "PyBank", "analysis", "analysis.txt")

with open(analysisOutputPath, "w") as text:
    
    text.write("Financial Analysis \n--------------------------------\n")
    text.write(f"Total Months: {totMonths}\n")
    text.write(f"Total: ${totNetProfit_Loss:,.2f}\n")
    text.write(f"Average Change: ${netMonthlyAvg:,.2f}\n")
    text.write(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:,.2f})\n")
    text.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:,.2f})")