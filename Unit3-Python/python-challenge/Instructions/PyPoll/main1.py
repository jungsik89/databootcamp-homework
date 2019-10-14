import os, csv

election_csv = os.path.join('Resources','election_data.csv')

khanvotecount = {'votecount': 0, 'win percentage': 0.0, 'totalwin': 0}
correyvotecount = {'votecount': 0, 'win percentage': 0.0, 'totalwin': 0} 
livotecount = {'votecount': 0, 'win percentage': 0.0, 'totalwin': 0}



#def khanpercentage(election_data):

with open(election_csv, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')   
    for row in reader:
        if row[1] == 'Khan':
            khanvotecount.append[row[1]]
            print('khanvotecount')

        
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


    
