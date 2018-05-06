# Modules
import os
import csv

# Set path for files
csvpath_budget_data_1 = os.path.join("Resources", "budget_data_1.csv")
csvpath_budget_data_2 = os.path.join("Resources", "budget_data_2.csv")

# Creating variables 
count = 0
totalRevenue = 0.00
revenue_data = []
date = []
rev_change = []
maxRevenue = 0.00
minRevenue = 0.00
maxRevIndexDate = 0
minRevIndexDate = 0
totalMonths = 0
averageRevenueChange = 0

# Checking if the File is Present or not
if(os.path.isfile(csvpath_budget_data_1)):
    print("File budget_data_1.csv Found! Let's Proceed")

    # Open the CSV budget_data_1
    with open(csvpath_budget_data_1, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skipping the headers
        next(csvreader)

        # Loop through looking for the video
        for row in csvreader:
            revenue_data.append(float(row[1]))
            date.append(row[0])

        # Creating a loop for calculating the revenue change
        for i in range(1,len(revenue_data)):
            rev_change.append(revenue_data[i]-revenue_data[i-1])
        
        # Calculating the max and min of Revenue Change and Dates
        maxRevenueChange = max(rev_change)
        minRevenueChange = min(rev_change)
        maxRevIndexDate = str(date[rev_change.index(maxRevenueChange)])
        minRevIndexDate = str(date[rev_change.index(minRevenueChange)])

        # Calculating other variable
        totalMonths = str(len(revenue_data))
        totalRevenue = str(sum(revenue_data))
        averageRevenueChange = str(sum(revenue_data)/len(revenue_data))

        # Printing everything
        print("-" * 72)
        print("FILE NAME - budget_data_2.csv")
        print("-" * 72)
        print("Total Months: " + totalMonths) 
        print("Total Revenue: " + totalRevenue)  
        print("Average Revenue Change: " + averageRevenueChange)
        print("Greatest Increase in Revenue: " +  "$" + str(maxRevenueChange) + " (" + maxRevIndexDate + ")")
        print("Greatest Decrease in Revenue: " + "$"+ str(minRevenueChange) + " (" + minRevIndexDate+ ")")
        print("-" * 72) 
        print("*" * 72) 
    
   # Exporting results to a text file
    file = open('Results.txt','a')
    file.write("-----------------------------------\n")
    file.write('Financial Analysis for ' + csvpath_budget_data_1 + '\n')
    file.write("-----------------------------------\n")
    file.write("Total Months:"+ str(totalMonths)+'\n')
    file.write('Total Revenue: $'+ str(totalRevenue)+'\n')
    file.write('Average Revenue Change: $'+ str(averageRevenueChange)+'\n')
    file.write("Greatest Increase in Revenue:"+ str(maxRevenueChange)+"($"+str(maxRevIndexDate)+")"+'\n')
    file.write("Greatest Decrease in Revenue:"+str(minRevenueChange)+"($"+ str(minRevIndexDate)+")"+"\n")
    file.close()
else:
    print("File Not Found! Please check")

##########################################################################

# Reseting all the variables
count = 0
totalRevenue = 0.00
revenue_data = []
date = []
rev_change = []
maxRevenue = 0.00
minRevenue = 0.00
maxRevIndexDate = 0
minRevIndexDate = 0
totalMonths = 0
averageRevenueChange = 0

# Checking if the File is Present or not
if(os.path.isfile(csvpath_budget_data_2)):
    print("File budget_data_2.csv Found! Let's Proceed")

    # Open the CSV budget_data_2
    with open(csvpath_budget_data_2, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skipping the headers
        next(csvreader)

        # Loop through looking for the video
        for row in csvreader:
            revenue_data.append(float(row[1]))
            date.append(row[0])

        # Creating a loop for calculating the revenue change
        for i in range(1,len(revenue_data)):
            rev_change.append(revenue_data[i]-revenue_data[i-1])
        
        # Calculating the max and min of Revenue Change and Dates
        maxRevenueChange = max(rev_change)
        minRevenueChange = min(rev_change)
        maxRevIndexDate = str(date[rev_change.index(maxRevenueChange)])
        minRevIndexDate = str(date[rev_change.index(minRevenueChange)])

        # Calculating other variable
        totalMonths = str(len(revenue_data))
        totalRevenue = str(sum(revenue_data))
        averageRevenueChange = str(sum(revenue_data)/len(revenue_data))

        # Printing everything
        print("-" * 72)
        print("FILE NAME - budget_data_2.csv")
        print("-" * 72)
        print("Total Months: " + totalMonths) 
        print("Total Revenue: " + totalRevenue)  
        print("Average Revenue Change: " + averageRevenueChange)
        print("Greatest Increase in Revenue: " +  "$" + str(maxRevenueChange) + " (" + maxRevIndexDate + ")")
        print("Greatest Decrease in Revenue: " + "$"+ str(minRevenueChange) + " (" + minRevIndexDate+ ")")
        print("-" * 72) 
        print("*" * 72) 

    # Exporting results to a text file
    file = open('Results.txt','a')
    file.write("-----------------------------------\n")
    file.write('Financial Analysis for ' + csvpath_budget_data_2 + '\n')
    file.write("-----------------------------------\n")
    file.write("Total Months:"+ str(totalMonths)+'\n')
    file.write('Total Revenue: $'+ str(totalRevenue)+'\n')
    file.write('Average Revenue Change: $'+ str(averageRevenueChange)+'\n')
    file.write("Greatest Increase in Revenue:"+ str(maxRevenueChange)+"($"+str(maxRevIndexDate)+")"+'\n')
    file.write("Greatest Decrease in Revenue:"+str(minRevenueChange)+"($"+ str(minRevIndexDate)+")"+"\n")
    file.close()   
    
else:
    print("File Not Found! Please check")

