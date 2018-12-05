import os
import csv

#Read in Data
#Run function to calulate the information
#Write file and print to terminal

PyBankPath = os.path.join('..', '..', 'Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources'
, 'election_data.csv')

monthlist = []
PLList = []
ChangeList = []
NetPL = 0.0
NetChange = 0.0
index = 0
WorstMonth = ""
BestMonth = ""
Inc = 0.0
Dec = 0.0


with open(PyBankPath, 'r') as budgetfile:

    budget_reader = csv.reader(budgetfile, delimiter=',')
    budget_header = next(budget_reader)

    for row in budget_reader:
        month = row[1]
        monthlist.append(month)
        PL = int(row[0])
        PLList.append(PL)
        NetPL += PL

        if len(monthlist) >= 1:
            index = len(monthlist) - 2
        else:
            index = 0

        Start = PLList[index]
        Change = PL - Start
        ChangeList.append(Change)
        NetChange += Change  

    for r in range(len(ChangeList)):   
        if ChangeList[r] >= Inc:
            Inc = ChangeList[r]
            BestMonth = monthlist[r]
        elif ChangeList[r] <= Dec:
            Dec = ChangeList[r]
            WorstMonth = monthlist[r]

average_change = NetChange/(len(ChangeList)-1)

print(f"Financial Report")
print(f"-----------------------------------------------")
print(f"Total Number of months: {len(monthlist)}")
print(f"Total Profit/Loss: ${NetPL}")
print(f"Average Change: {average_change}")  
print(f"The Best Month was {BestMonth} with a profit of ${Inc}")
print(f"The Worst Month was {WorstMonth} with a loss of ${Dec}")

Budgetoutput = os.path.join("Budget_Output_Election_Data.csv")

with open(Budgetoutput, "w", newline="") as datafile:
    
    Budgetwriter = csv.writer(datafile, delimiter = ',')

    Budgetwriter.writerow(["Total Months", "Total Profit/Loss", "Average Change", "Best Month", "Best Profit", "Worst Month", "Worst Profit"])

    Budgetwriter.writerow([len(monthlist), NetPL, average_change, BestMonth, Inc, WorstMonth, Dec])
