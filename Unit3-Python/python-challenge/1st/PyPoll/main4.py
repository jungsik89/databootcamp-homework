import csv

tracker = {'percentage':0, 'totalvotes':0, 'voterid':0, 'county':"", 'candidate':""}
candidates = ('Khan', 'Correy', 'Li', "O'tooley")
l = [x for x in candidates]
print(candidates[0])
print(candidates[1])
print(candidates[2])
print(candidates[3])



#total_votes = 0
#khan_votes = 0
##correy_votes = 0
#li_votes = 0
##otooley_votes = 0
#winner = ""



list = []

filename = 'election_data_test.csv'

with open(filename, newline='') as poll_data:
#set variable to object csv
  csvreader = csv.reader(poll_data)
 # try:
  for row in csvreader:
        #county = (row['Country'])
        #candidate = int(row['Candidate'])
        #voterid = int(row['Voter ID'])
        #print(county)
        #print(candidate)
        #print(voterid)
        #print(row)
        #print(csvreader)

        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

       # for row in csvreader:
        #  print(row)

#spreadsheet = csv.DictReader(poll_data)

#for row in spreadsheet:
 #   total_votes = sum(1 for row in poll_data) + 2
    #khan_votes = 
  #  print(total_votes)



    #
    # print(len(int(total_votes)))
