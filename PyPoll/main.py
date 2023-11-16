import os
import csv

ballot_id = []
county = []
candidates = []
votes_count = {}  #empty dictionary to store the names of the candidates
input_path = "PyPoll/Resources/election_data.csv"
percentage = 0
with open(input_path, 'r') as input_csv:
	csvreader = csv.reader(input_csv, delimiter=',')
	header=next(csvreader) #storing the header row
	for row in csvreader: 
		ballot_id.append(row[0])
		county.append(row[1])
		candidate= row[2] 
		if candidate not in candidates: #if the candidate name is not in the candidates list 
			candidates.append(candidate) #add it to the empty list 
		if candidate in votes_count:  #if the candidate name is in the dictionary then 
			votes_count[candidate] += 1 #add the vote
		else:
			votes_count[candidate]=1
	total_votes = len(ballot_id) #total votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
		percentage = (votes_count[candidate]/total_votes)*100 #calculating percentage
		print(f"{candidate}: {round(percentage,2)}% ({votes_count[candidate]})")

output_file = 'PyPoll/Analysis/election_data.txt' #writing to an empty txt file
with open(output_file,"w",newline= '') as datafile:
    datafile.write('Election Results\n')
    datafile.write('----------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('----------------------------\n')
    for c in candidates:
        percentage = (votes_count[c]/total_votes)*100
        datafile.write(f"{c}: {round(percentage,3)}% ({votes_count[c]})\n")
            
