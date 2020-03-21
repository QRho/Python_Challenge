import csv

f= open ('election_data.csv') 

csv_f =csv.reader(f, delimiter=',')

#open the csv and read it 
#Take header off data

header = next(csv_f )

#Create and Label the txt file
fo= open ('election.txt','w') 

fo.write('Election Results \n')
fo.write('----------------\n')

#Set variables and lists for script
votes=[]
candidates=[]
percent=float


#Begin a for loop to cycle through all the rows in the dataset
for row in csv_f:

#append the rows that I am pulling data from

  candidates.append(row[2])
  votes.append((row[0]))

#Calculate the total votes using len & write into txt file

  Total= (len(votes))
fo.write('Total Votes:\n')
fo.write(f'{Total}\n')
fo.write('----------------\n')

#Import counter and make a dictionary of data
from collections import Counter
candidate_counter = Counter(candidates)

for key,val in candidate_counter.items():
#write the key, percent and actual ammount of votes on same line
    fo.write(f'{key}:  {"{:.0%}".format(candidate_counter[key]/Total)}  ({val}) \n')

#write to the txt file formatting to show winner
fo.write('----------------\n')
fo.write ('Winner:') 
fo.write('\n----------------\n') 
#Winner =(candidate_counter '({val})max()')


winner=max(candidate_counter.values())
#print(winner)
 
# Write to txt file the key candidate with most votes as winner
for key,val in candidate_counter.items():
 
  if val == winner: 
   fo.write(key)

#close out txt file and then csv

fo.close()

f.close()



