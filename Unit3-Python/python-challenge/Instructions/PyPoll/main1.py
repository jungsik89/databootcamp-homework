import os, csv

election_csv = os.path.join('Resources','election_data.csv')

vote_count = 0
candidate_list = []


#def khanpercentage(election_data):
#spreadsheet = csv.DictReader(election_csv)
with open(election_csv, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')   
    csv_header = next(reader)
    for row in reader:
        vote_count = vote_count + 1



print(vote_count)
        #total_votes = len(column)
        #print(total_votes)
        #total_votes += 1
        #print(total_votes)
       # print(', '.join(row))
print(f"Election Results\n-------------------------\nTotal Votes: {vote_count}\n------------------------\nKhan: ")     
    #for candidate in reader:
    
        #count(Khan)

        #if row[1] == 'Khan':
         #   khanvotecount.append[row[1]]
          #  print('khanvotecount')

        
            # print(reader)
        #row_count = len(reader)
        #print(row_count)


        #data = list(reader)
        #row_count = len(data)
        #print(row_count)
  #      candidatename = str(election_data[2])
   #     voterid = str(election_data[0])
    #    county = str(election_data[1])

   # for row in range(row_count):
    #    If 


#print(f"this is {Candidate}")


    
