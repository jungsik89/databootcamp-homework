import os, csv

election_csv = os.path.join('Resources','election_data.csv')
candidateone = 'Khan'
log = []
khanvotecount = {'votecount': 0, 'win percentage': 0.0, 'totalwin': 0}
correyvotecount = {'votecount': 0, 'win percentage': 0.0, 'totalwin': 0} 
livotecount = {'votecount': 0, 'win percentage': 0.0, 'totalwin': 0}
candidates = ['Khan', 'Li', 'Correy']
county = ['']
total_votes = 0
pollresult = []


#def khanpercentage(election_data):
#spreadsheet = csv.DictReader(election_csv)
with open(election_csv, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')   
    for row in reader:
        if row[2] == candidateone:
            log.append(candidateone)
            khanvotecount = candidateone.count('Khan')
            print(khanvotecount)
        #total_votes = len(column)
        #print(total_votes)
        #total_votes += 1
        #print(total_votes)
       # print(', '.join(row))
        
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


    
