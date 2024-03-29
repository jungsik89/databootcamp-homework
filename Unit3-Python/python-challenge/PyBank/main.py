import os
import csv

bank_csv = os.path.join('Resources','budget_data.csv')

profit_list = []
monthly_change_list = []
date_list = []

total_month = 0
total_revenue = 0
total_change = 0
initial_profit = 0


#Open csv
with open(bank_csv, newline="",) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skips the header 
    csv_header = next(csvreader)
    for row in csvreader:
        total_month = total_month + 1 
        #counts the amount of month and row
        date_list.append(row[0]) 
        #date list contains the exact amount of rows in column Date
        profit_list.append(row[1])
        #profit list contains the exact amount of rows in column Profit/Losses
        total_revenue = total_revenue + int(row[1])
        #total revenue is calcualted by adding up each amt in each row in Profit/Losses column (it prints 38382578)
        last_profit = int(row[1])
        #last profit equal to the last row. 
        monthly_change = last_profit - initial_profit
        #calculate change amount
        monthly_change_list.append(monthly_change)
        #append these to a list 
        initial_profit = last_profit
        #initial profit is assigned the last value, loop restarts 

monthly_change_list.pop(0)
total_change = total_change + (sum([int(i) for i in monthly_change_list]))
average_change = total_change/(total_month-1)
greatest_increase_p = max(monthly_change_list)
greatest_decrease_p = min(monthly_change_list)
increase_date = date_list[monthly_change_list.index(greatest_increase_p)]
decrease_date = date_list[monthly_change_list.index(greatest_decrease_p)]
     
print(f"Financial Analysis\n--------------------\nTotal Months: {total_month}\nTotal: ${total_revenue}\nAverage Change: ${average_change}\n\
Greatest Increase in Profits: Year-> {increase_date} Amount-> ${greatest_increase_p}\nGreatest Decrease in Profits: Year-> {decrease_date} Amount-> ${greatest_decrease_p}")

with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("---------------------------------------\n")
    text.write("Total Months: " + str(total_month))
    text.write("\nTotal: $" + str(total_revenue))
    text.write("\nAverage Change: $" + str(average_change))
    text.write("\nGreatest Increase in Profits: Year->: " + str(increase_date) + " Amount->: $" + str(greatest_increase_p))
    text.write("\nGreatest Decrease in Profits: Year->: " + str(decrease_date) + " Amount->: $" + str(greatest_decrease_p))



#print(sum(monthly_change_list))
#print(int(monthly_change))
#print(int(total_change))      
#print(str(monthly_change_list))
#print(int(average_change))
#print(str(profit_list))
#print(int(greatest_increase_p))
#print(str(increase_date))
#print(int(final_profit))
#print(str(date_list))
#print(int(total_change))
##print(int(initial_profit))
#print(str(monthly_change_list))
#print(str(profit_list))
#print(str(date_list))
#list(csvreader)
#print(csvreader)
#month.append(row[0])
#profloss.append(row[1])
#nettotal = ?
#print(len(month))
#print(len(profloss))
