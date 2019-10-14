import os
import csv



bank_csv = ("budget_data.csv")
month = []

net_total = []
average = []
gincrease = []
gdecrease = []

with open(bank_csv, newline="",) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
#month.append(row[0])
#profloss.append(row[1])
#nettotal = 

#print(len(month))
#print(len(profloss))

print("Financial Analysis")
print("--------------------")



