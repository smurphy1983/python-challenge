import os
import csv

#Read in Data

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
        #Creates a list of every month that can be used to calculate total number of months
        #appends to the list with every run of the loop
        month = row[1]
        monthlist.append(month)
        #creates a list of the profit and loss amounts that can be used to get a total and help 
        #calulate the averagesPL = int(row[0])
        PL = int(row[0])
        PLList.append(PL)
        NetPL += PL

        #generate a secondary index so that I can call back to calulate the monthly difference
        index = len(monthlist) - 2
        
        #create a variable to hold the inital amount at the start of each month and the use 
        #the newly created index to call back to the previous month
        Start = PLList[index]
        Change = PL - Start
        ChangeList.append(Change)
        NetChange += Change  
        #use a for loop with if statement to calculate the best and worst change month
    for r in range(len(ChangeList)):   
        if ChangeList[r] >= Inc:
            Inc = ChangeList[r]
            BestMonth = monthlist[r]
        elif ChangeList[r] <= Dec:
            Dec = ChangeList[r]
            WorstMonth = monthlist[r]
#calculate average
average_change = NetChange/(len(ChangeList)-1)
#print data to the terminal
print(f"Financial Report")
print(f"-----------------------------------------------")
print(f"Total Number of months: {len(monthlist)}")
print(f"Total Profit/Loss: ${NetPL}")
print(f"Average Change: {average_change}")  
print(f"The Best Month was {BestMonth} with a profit of ${Inc}")
print(f"The Worst Month was {WorstMonth} with a loss of ${Dec}")

Budgetoutput = os.path.join("Budget_Output_Election_Data.csv")
#write file to the directory
with open(Budgetoutput, "w", newline="") as datafile:
    
    Budgetwriter = csv.writer(datafile, delimiter = ',')

    Budgetwriter.writerow(["Total Months", "Total Profit/Loss", "Average Change", "Best Month", "Best Profit", "Worst Month", "Worst Profit"])

    Budgetwriter.writerow([len(monthlist), NetPL, average_change, BestMonth, Inc, WorstMonth, Dec])
