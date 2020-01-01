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


#Reading and writing to text files : https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3



'''
import csv
import os


#create list to compile needed data
total_votes = 0
Khan_votes = 0
Correy_votes =0
Li_votes = 0
Otooley_votes = 0


#Open csv reader in read modernize
with open("election_data.csv", "r") as pypoll:
	reader = csv.reader(pypoll)

#Skip the first row to remove headers so that they are not swept within the data	
	next(reader)
	
#Create a loop that compiles list for each data point
	#count voter ID's that are not duplicates in variable
	for row in reader:
		total_votes +=1
	
	#count the amount of times each person appears in the list
		if row[2] == "Khan":
			Khan_votes +=1
		elif row[2] ==  "Correy":
			Correy_votes +=1
		elif row[2] == "Li":
			Li_votes +=1
		else:
			row[2] == "O'Tooley"
			Otooley_votes +=1
		
		

#Determine the overall winner. Create two seperate dictionaries in order to combine them together

candidates = ["Khan","Correy","Li","O'Tooley"]
votes = [Khan_votes,Correy_votes,Li_votes,Otooley_votes]


#zip the two list together to find the max value for the winner
candidates_and_votes = dict(zip(candidates,votes))
winner = max(candidates_and_votes, key = candidates_and_votes.get)


#Create variables to determine the percentage of votes
Khan_percent = (Khan_votes/total_votes) * 100
Correy_percent = (Correy_votes/total_votes) * 100
Li_percent = (Li_votes/total_votes) * 100
Otooley_percent = (Otooley_votes/total_votes) * 100




#Print statements

print(f"Election Results")
print(f"------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------")
print(f"Khan:     {Khan_percent:.3f}% ({Khan_votes})")
print(f"Correy:   {Correy_percent:.3f}% ({Correy_votes})")
print(f"Li:       {Li_percent:.3f}% ({Li_votes})")
print(f"O'Tooley: {Otooley_percent:.3f}%  ({Otooley_votes})")
print(f"------------------------------")
print(f"Winner: {winner}")
print(f"------------------------------")




#generate a text file displaying the analylitical data

with open("pypoll_analysis","w")as file:

#Write analysis data to text file using /n to write info on seperate lines

	file.write(f"Election Results")
	file.write("\n")
	file.write(f"------------------------------")
	file.write("\n")
	file.write(f"Total Votes: {total_votes}")
	file.write("\n")
	file.write(f"------------------------------")
	file.write("\n")
	file.write(f"Khan:     {Khan_percent:.3f}% ({Khan_votes})")
	file.write("\n")
	file.write(f"Correy:   {Correy_percent:.3f}% ({Correy_votes})")
	file.write("\n")
	file.write(f"Li:       {Li_percent:.3f}% ({Li_votes})")
	file.write("\n")
	file.write(f"O'Tooley: {Otooley_percent:.3f}%  ({Otooley_votes})")
	file.write("\n")
	file.write(f"------------------------------")
	file.write("\n")
	file.write(f"Winner: {winner}")
	file.write("\n")
	file.write(f"------------------------------")

	


