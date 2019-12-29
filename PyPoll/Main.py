'''
## PyPoll

![Vote-Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

'''
import csv
import os


#create list to compile needed data
total_votes = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []


#Open csv reader in read modernize
with open("election_data.csv", "r") as pypoll:
	reader = csv.reader(pypoll)

#Skip the first row to remove headers so that they are not swept within the data	
	next(reader)
	
#Create a loop that compiles list for each data point
	for row in reader:
		total_votes.append(row[0])
		
		if row[2] = "Khan"
			khan_votes.append
		elif row[2] =  "Correy"
			correy_votes.append
		elif row[2] = "Li"
			li_votes.append
		else:
			row[2] = "O'Tooley"
			otooley.append
		
		




#Print statements

print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(total_votes)}")

	
	


