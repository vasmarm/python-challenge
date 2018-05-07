# Modules
import os
import csv

# Set path for files
csvpath_election_data_1 = os.path.join("Resources", "election_data_1.csv")
csvpath_election_data_2 = os.path.join("Resources", "election_data_2.csv")

# Declaring variables
totalVotes = 0
candidateList = []
voterId = []
votes = [0,0,0,0,0]
votesPercentage = [0.00,0.00,0.00,0.00,0.00]

# Checking if the File is Present or not
if(os.path.isfile(csvpath_election_data_1)):
    print("File election_data_1.csv Found! Let's Proceed")
    
    # Open the CSV budget_data_1
    with open(csvpath_election_data_1, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skipping the headers
        next(csvreader)

        # Loop through looking for the video
        for row in csvreader:
            totalVotes = totalVotes + 1
            voterId.append(row[0])
            if row[2] not in candidateList:
                candidateList.append(row[2])

            # Checking for Vote Counts for each candidate
            if row[2] == 'Vestal':
                votes[0] = votes[0] + 1
            elif row[2] == 'Torres':
                votes[1] = votes[1] + 1
            elif row[2] == 'Seth':
                votes[2] = votes[2] + 1
            elif row[2] == 'Cordin':
                votes[3] = votes[3] + 1

        # Calculating Percentages of votes for each candidate
        for i in range(0,len(candidateList)):
            votesPercentage[i] = round((votes[i]/totalVotes)*100,2)    

        # Printing the results
        print("Election Results -->")
        print("-" *72)
        print("Total Number of Votes Casted: " + str(totalVotes))
        print("-" *72)
        print("Vestal: " + str(votesPercentage[0]) + "% " + " (" + str(votes[0]) + ")")
        print("Torres: " + str(votesPercentage[1]) + "% " + " (" + str(votes[1]) + ")")
        print("Seth: " + str(votesPercentage[2]) + "% " + " (" + str(votes[2]) + ")")
        print("Cordin: " + str(votesPercentage[3]) + "% " + " (" + str(votes[3]) + ")")
        print("-" *72)
        print("Winner: " + candidateList[votes.index(max(votes))])
        print("*" *72)

    # Exporting results to a text file
    file = open('Poll_Results.txt','a')
    file.write("-" *72 + "\n")
    file.write('Polls Analysis for ' + csvpath_election_data_1 + '\n')
    file.write("-" *72 + "\n")
    file.write("Total Number of Votes Casted:"+ str(totalVotes)+'\n')
    file.write("-" *72 + "\n")
    file.write("Vestal: " + str(votesPercentage[0]) + "% " + " (" + str(votes[0]) + ")" + "\n")
    file.write("Torres: " + str(votesPercentage[1]) + "% " + " (" + str(votes[1]) + ")" + "\n")
    file.write("Seth: " + str(votesPercentage[2]) + "% " + " (" + str(votes[2]) + ")" + "\n")
    file.write("Cordin: " + str(votesPercentage[3]) + "% " + " (" + str(votes[3]) + ")" + "\n")
    file.write("-" *72 + "\n")
    file.write("Winner: " + candidateList[votes.index(max(votes))] + "\n")
    file.write("*" *72 + "\n")
    file.close()
else:
    print("Error! File Not Found!")


##########################################################################

# Reseting all the variables
totalVotes = 0
candidateList = []
voterId = []
votes = [0,0,0,0,0]
votesPercentage = [0.00,0.00,0.00,0.00,0.00]

# Checking if the File is Present or not
if(os.path.isfile(csvpath_election_data_2)):
    print("File election_data_2.csv Found! Let's Proceed")
    
    # Open the CSV budget_data_1
    with open(csvpath_election_data_2, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skipping the headers
        next(csvreader)

        # Loop through looking for the video
        for row in csvreader:
            totalVotes = totalVotes + 1
            voterId.append(row[0])
            if row[2] not in candidateList:
                candidateList.append(row[2])

            # Checking for Vote Counts for each candidate
            if row[2] == "Khan":
                votes[0] = votes[0] + 1
            elif row[2] == "Correy":
                votes[1] = votes[1] + 1
            elif row[2] == "Li":
                votes[2] = votes[2] + 1
            elif row[2] == "O'Tooley":
                votes[3] = votes[3] + 1

        # Calculating Percentages of votes for each candidate
        for i in range(0,len(candidateList)):
            votesPercentage[i] = round((votes[i]/totalVotes)*100,2)    

        # Printing the results
        print("Election Results -->")
        print("-" *72)
        print("Total Number of Votes Casted: " + str(totalVotes))
        print("-" *72)
        print("Khan: " + str(votesPercentage[0]) + "% " + " (" + str(votes[0]) + ")")
        print("Correy: " + str(votesPercentage[1]) + "% " + " (" + str(votes[1]) + ")")
        print("Li: " + str(votesPercentage[2]) + "% " + " (" + str(votes[2]) + ")")
        print("O'Tooley: " + str(votesPercentage[3]) + "% " + " (" + str(votes[3]) + ")")
        print("-" *72)
        print("Winner: " + candidateList[votes.index(max(votes))])
        print("*" *72)
        

    # Exporting results to a text file
    file = open('Poll_Results.txt','a')
    file.write("-" *72 + "\n")
    file.write('Polls Analysis for ' + csvpath_election_data_1 + '\n')
    file.write("-" *72 + "\n")
    file.write("Total Number of Votes Casted:"+ str(totalVotes)+'\n')
    file.write("-" *72 + "\n")
    file.write("Khan: " + str(votesPercentage[0]) + "% " + " (" + str(votes[0]) + ")" + "\n")
    file.write("Correy: " + str(votesPercentage[1]) + "% " + " (" + str(votes[1]) + ")" + "\n")
    file.write("Li: " + str(votesPercentage[2]) + "% " + " (" + str(votes[2]) + ")" + "\n")
    file.write("O'Tooley: " + str(votesPercentage[3]) + "% " + " (" + str(votes[3]) + ")" + "\n")
    file.write("-" *72 + "\n")
    file.write("Winner: " + candidateList[votes.index(max(votes))] + "\n")
    file.write("*" *72 + "\n")
    file.close()
else:
    print("Error! File Not Found!")