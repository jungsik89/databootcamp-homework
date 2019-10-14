import csv

tracker = {'percentage':0, 'k_votes':0, 'c_votes':0, }
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

poll_data = open("election_data_test.csv", "r")
#set variable to object csv
    csvreader = csv.reader(poll_data, delimiter",")

    print(poll_data)
    print(csvreader)


#spreadsheet = csv.DictReader(poll_data)

#for row in spreadsheet:
 #   total_votes = sum(1 for row in poll_data) + 2
    #khan_votes = 
  #  print(total_votes)



    #
    # print(len(int(total_votes)))
