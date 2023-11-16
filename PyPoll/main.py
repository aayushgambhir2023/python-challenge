import os
import csv

ballot_id = []
county = []
candidate = []
candidatenames = []
input_path = "PyPoll/Resources/election_data.csv"
with open(input_path, 'r') as input_csv:
	reader = csv.reader(input_csv, delimiter=',')
	header=next(reader) #storing the header row
	for row in reader:
		ballot_id.append(row[0])
		county.append(row[1])
		candidate.append(row[2])
total_votes = len(ballot_id)

