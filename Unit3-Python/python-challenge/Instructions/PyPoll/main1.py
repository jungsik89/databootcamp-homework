import os, csv

election_csv = os.path.join('..','Resources','election_data.csv')

khanvotecount = ['votecount': 0, 'win percentage': 0.0, 'totalwin': 0, )
correyvotecount = ('votecount': 0, 'win percentage': 0.0, 'totalwin': 0, )
livotecount = ('votecount': 0, 'win percentage': 0.0, 'totalwin': 0, )

with open(election_csv, 'w') as csvreader:
    reader = csv.reader(csvreader, delimiter = ",")
    data = list(reader)
    row_count = len(data)

def percentage(election_data):

    candidatename = str(election_data[2])
    voterid = str(election_data[0])
    county = str(election_data[1])

print(f"this is {Candidate}")


    
