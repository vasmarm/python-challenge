# python-challenge
PyBank, PyPoll, PyBoss, or PyParagraph.


Option 1: PyBank

task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset
The total amount of revenue gained over the entire period
The average change in revenue between months over the entire period
The greatest increase in revenue (date and amount) over the entire period
The greatest decrease in revenue (date and amount) over the entire period


Eg - 
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)


Option 2: PyPoll

task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.


As an example, your analysis should look similar to the one below:

Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------



Option 3: PyBoss

task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:


Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:


Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

Then convert and export the data to use the following format instead:


Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA


In summary, the required conversions are as follows:


The Name column should be split into separate First Name and Last Name columns.
The DOB data should be re-written into MM/DD/YYYY format.
The SSN data should be re-written such that the first five numbers are hidden from view.
The State data should be re-written as simple two-letter abbreviations.

Option 4: PyParagraph

task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:


Import a text file filled with a paragraph of your choosing.

Assess the passage for each of the following:


Approximate word count
Approximate sentence count
Approximate letter count (per word)
Average sentence length (in words)


As an example, this passage:



“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”


...would yield these results:

Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4
