import os
import csv

bank_csv = os.path.join('Resources','budget_data.csv')

profit_list = []
monthly_change_list = []
date_list = []


total_month = 0
total_revenue = 0
total_change = 0
profit = 0


#Open csv
with open(bank_csv, newline="",) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skips the header 
    csv_header = next(csvreader)
    for row in csvreader:
        total_month = total_month + 1
        


print(str(total_month))
        #list(csvreader)
        #print(csvreader)
#month.append(row[0])
#profloss.append(row[1])
#nettotal = 

#print(len(month))
#print(len(profloss))

print("Financial Analysis")
print("--------------------")



