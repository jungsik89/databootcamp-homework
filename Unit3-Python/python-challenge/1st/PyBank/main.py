import os, sys

print("Financial Analysis")
print("--------------------")

bank_csv = ("budget_data.csv")
month = []

nettotal = []
average = []
gincrease = []
gdecrease = []

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

csv_header = next(csvheader)
    
row_count = sum(1 for row in csv_header)



month.append(row[0])
profloss.append(row[1])
#nettotal = 

print(len(month))
print(len(profloss))





