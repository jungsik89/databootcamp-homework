import os, csv

election_csv = os.path.join('Resources','election_data.csv')

vote_count = 0
candidate_list = []
khanlist = []
correylist = []
lilist = []
otooleylist = []
khanvotetotal = 0

candidateone = 'Khan'
candidatetwo = 'Correy'
candidatethree = 'Li'
candidatefour = "O'Tooley"

# if(name_to_check == row[0]):
#def khanpercentage(election_data):
#spreadsheet = csv.DictReader(election_csv)
with open(election_csv, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')   
    csv_header = next(reader)
    for row in reader:
        vote_count = vote_count + 1
        candidate_list.append(row[2])
        if row[2] == candidateone:
            khanlist.append(candidateone)
        if row[2]==candidatetwo:
            correylist.append(candidatetwo)
        if row[2]==candidatethree:
            lilist.append(candidatethree)
        if row[2]==candidatefour:
            otooleylist.append(candidatefour)
        
    khanvotetotal = khanlist.count('Khan')
    correyvotetotal = correylist.count('Correy')
    livotetotal = lilist.count('Li')
    otooleytotal = otooleylist.count("O'Tooley")

    khanpercentage = ((khanvotetotal/vote_count)*100)
    khanpercentage = round(khanpercentage,5)

    correypercentage = ((correyvotetotal/vote_count)*100)
    correypercentage = round(correypercentage,5)

    lipercentage = ((livotetotal/vote_count)*100)
    lipercentage = round(lipercentage,5)

    otooleypercentage = ((otooleytotal/vote_count)*100)
    otooleypercentage = round(otooleypercentage,5)

    totalcountdict = {}
    totalcountdict.update(Khan = int(khanvotetotal))
    totalcountdict.update(Correy = int(correyvotetotal))
    totalcountdict.update(Li = int(livotetotal))
    totalcountdict.update({"O'Tooley" : int(otooleytotal)})

            
    print(totalcountdict)

    #khanpercentage = (khanvotetotal/vote_count)*100
   

##print(khanvotetotal)
#print(khanpercentage)
#print(khanvotetotal)
#print(vote_count)
        #total_votes = len(column)
        #print(total_votes)
        #total_votes += 1
        #print(total_votes)
       # print(', '.join(row))
print(f"\
    Election Results\n-------------------------\nTotal Votes: {vote_count}\n-------------------------\
    \nKhan: {khanpercentage}% ({khanvotetotal})\nCorrey: {correypercentage}% ({correyvotetotal})\nLi: {lipercentage}% ({livotetotal})\
    \nO'Tooley: {otooleypercentage}% ({otooleytotal})\n-------------------------\
    \nWinner: ")     
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


    
