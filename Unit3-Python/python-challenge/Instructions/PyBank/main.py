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
        date_list.append(row[0])
        profit_list.append(row[1])
        total_revenue = total_revenue + int(row[1])
        final_profit = int(row[1])
        monthly_change = final_profit - initial_profit
        monthly_change_list.append(monthly_change)
        total_change = total_change + monthly_change
        initial_profit = final_profit
        

        
print(int(initial_profit))
print(str(monthly_change))
print(int(final_profit))
print(int(total_revenue))
print(str(total_month))
print(str(profit_list))
#print(str(date_list))
        #list(csvreader)
        #print(csvreader)
#month.append(row[0])
#profloss.append(row[1])
#nettotal = 

#print(len(month))
#print(len(profloss))

print("Financial Analysis")
print("--------------------")



