# Import Dependencies
import os

import csv

# Import and export file path
csvpath = os.path.join('Resources', 'election_data.csv')
outputpth = os.path.join('Analysis', 'PyPoll_output.csv')

# Initialize the variables
Elections_list = []
Individual_votes = {}
Winner_votes = 0
Winner = ""
Total_votes = 0

# Read in the file
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)

# start the loop and get the Total vote count
    for row in csv_reader:
        Total_votes += 1
        # print(row[0])
        # exit()

        name = row[2]
# Using the conditional statement to get the votes
        if name not in Elections_list:
            Elections_list.append(name)
            Individual_votes[name] = 1
            # print(name)

        elif name in Elections_list:
            Individual_votes[name] = Individual_votes[name]+1

with open(outputpth, 'w') as output_file:
    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {Total_votes}\n"
        f"-------------------------\n")
# Calculating the percentages of votes

    print(output)
    output_file.write(output)
    for name in Individual_votes:
        count = Individual_votes[name]
        percentage = (count/Total_votes) * 100

        result = f"{name} : {percentage:.3f}% ({count})\n"
        print(result)

        output_file.write(result)

        if count > Winner_votes:
            Winner_votes = count
            Winner = name

    result = (
        f"--------------------------\n"
        f"Winner:  {Winner}\n"
        f"--------------------------\n")

    print(result)

    # output_file.write(result)

with open(outputpth, "w") as txt_file:
    txt_file.write(result)
