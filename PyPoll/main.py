import os
import csv



# define path for data file
PyPollPath = os.path.join('..', '..', 'Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

Voter_Id_List = []
Candidate_List = []
Candidate = ""


#define variables and lists to hold votecount and percent vote count data
PerVote1 = 0
PerVote2 = 0
PerVote3 = 0
PerVote4 = 0
PerVote_List = []
Vote_Count_List = []
Vote_Count1 = 0
Vote_Count2 = 0
Vote_Count3 = 0
Vote_Count4 = 0


#use a function that can be called to populate the list of candidates
def Make_List():
    if Candidate not in Candidate_List:
        Candidate_List.append(Candidate)
    return Candidate_List
    
# read through imported data
with open (PyPollPath, 'r') as electionfile:

    election_reader = csv.reader(electionfile, delimiter = ",")
    election_header = next(election_reader)

    for row in election_reader:
        #generate voter Id list
        Voter_Id = row[0] 
        Voter_Id_List.append(Voter_Id)
        Candidate = row[2]
        #call function to make candidate list
        Make_List()
        #if statement to update vote count for each candidate
        if Candidate == Candidate_List[0]:
            Vote_Count1+=1                      
        elif Candidate == Candidate_List[1]: 
            Vote_Count2+=1     
        elif Candidate == Candidate_List[2]: 
            Vote_Count3+=1
        elif Candidate == Candidate_List[3]: 
            Vote_Count4+=1
        
#add vote counts to vote count list
Vote_Count_List.append(Vote_Count1)
Vote_Count_List.append(Vote_Count2)
Vote_Count_List.append(Vote_Count3)
Vote_Count_List.append(Vote_Count4)
#calculate percentages of votes
PerVote1 = round(Vote_Count1/len(Voter_Id_List)*100, 2)
PerVote2 = round(Vote_Count2/len(Voter_Id_List)*100, 2)
PerVote3 = round(Vote_Count3/len(Voter_Id_List)*100, 2)
PerVote4 = round(Vote_Count4/len(Voter_Id_List)*100, 2)
#append percentages to list
PerVote_List.append(PerVote1)
PerVote_List.append(PerVote2)
PerVote_List.append(PerVote3)
PerVote_List.append(PerVote4)

Win = 0.0
#for loop to calculate who won
for r in range(len(PerVote_List)):   
        if PerVote_List[r] >= Win:
            Win = PerVote_List[r]
            Winner = Candidate_List[r]


# print to screen
print("Election Results")
print("---------------------------------")
for x in range (4):
    print(f"{Candidate_List[x]}: {PerVote_List[x]}% ({Vote_Count_List[x]} total votes)")
print("---------------------------------")
print(f"Winner: {Winner}")

Election_zip = zip(Candidate_List, PerVote_List, Vote_Count_List)

Electionoutput = os.path.join("Election_Output.csv")

with open(Electionoutput, "w", newline="") as datafile:
    
    Electionwriter = csv.writer(datafile, delimiter = ',')

    Electionwriter.writerow(["Candidates", "Percentage Votes", "Total Votes"])

    for x in range (4):
        Electionwriter.writerow([Candidate_List[x], PerVote_List[x], Vote_Count_List[x]])

    Electionwriter.writerow(["Winner:", Winner])    