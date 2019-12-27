
'''
## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * THE TOTAL NUMBER OF MONTHS INCLUDED IN THE DATASET

  * THE NET TOTAL AMOUNT OF "PROFIT/LOSSES" OVER THE ENTIRE PERIOD

  * THE AVERAGE OF THE CHANGES IN "PROFIT/LOSSES" OVER THE ENTIRE PERIOD

  * THE GREATEST INCREASE IN PROFITS (DATE AND AMOUNT) OVER THE ENTIRE PERIOD

  * THE GREATEST DECREASE IN LOSSES (DATE AND AMOUNT) OVER THE ENTIRE PERIOD

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# sorting data in a csv file https://www.youtube.com/watch?v=VvKn3Y7qAKs

# Use this command later on to create a new csv file to post Homework results. https://www.youtube.com/watch?v=q5uM4VKywbA&t=630s
with open('new_pybank.csv', 'w') as new_file
	csv_writer = csv.writer(new_file)
	
#https://www.youtube.com/watch?v=W7QByFjVom8

#  Video talking about spliting the data  https://www.youtube.com/watch?v=W7QByFjVom8

# Stack overflow example of finding the difference within a list of numbers https://stackoverflow.com/questions/47040728/get-average-difference-between-all-numbers-in-a-list-python

'''

import csv
import os
import statistics


#Create list to iterate through specific rows for the following 
Month_Count = []
Profit_amount = []
Monthly_change = []

#Open CSV file in read mode
with open("budget_data.csv", "r") as pybank:
	reader = csv.reader(pybank)
	
#skip the first row to remove the headers from your set of information	
	next(reader)

#create a loop that creates two list as it passes through the information. This will allow you to manipulate the data 	
	for row in reader:
		Month_Count.append(row[0])
		Profit_amount.append(int(row[1]))
		
#Loop through profit list to get difference in each month		
for i in range(len(Profit_amount)-1):
	
	#Take the difference between two months and append it to monthly change
		Monthly_change.append(Profit_amount[i+1]-Profit_amount[i])
		
#establish the minimum and maximum values from the profit list

best_increase = max(Monthly_change)
best_decrease = min(Monthly_change)

#Connect max and min using month list and index / use +1 to associate the change to the next coming month
best_increase_month = Monthly_change.index(max(Monthly_change)) + 1
best_decrease_month = Monthly_change.index(min(Monthly_change)) + 1



#Print Statements


print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {len(Month_Count)}")
print(f"Total: ${sum(Profit_amount)}")
print(f"Average Change: {round(sum(Monthly_change)/len(Monthly_change),2)}")
print(f"Greatest Increase in Profits: {Month_Count[best_increase_month]} (${(str(best_increase))})")
print(f"Greatest Decrease in Profits: {Month_Count[best_decrease_month]} (${(str(best_decrease))})")