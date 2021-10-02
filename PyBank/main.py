
import os
import csv


Total_number_months = 0
Changes_total = 0
Change_count = 0
Profit_Losses_Total = 0
Previous_budget = 0
change = 0

Greatest_decrease = 0
Greatest_decrease_date = ""
Greatest_increase = 0
Greatest_increase_date = ""

csvpath = os.path.join('Resources', 'budget_data.csv')
outputpath = os.path.join('Analysis', 'bank_output.csv')

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        # print(row[1])
        # exit()

        Total_number_months += 1

        Current_budget = int(row[1])

        Profit_Losses_Total += Current_budget

        if Previous_budget != 0:
            change = Current_budget - Previous_budget
            Changes_total += change
            Change_count += 1

        Previous_budget = Current_budget

        if change > Greatest_increase:
            Greatest_increase = change
            Greatest_increase_date = row[0]

        elif change < Greatest_decrease:
            Greatest_decrease = change
            Greatest_decrease_date = row[0]

# print(
#     f'Greatest Increase in Profits: {Greatest_increase_date} (${Greatest_increase})')
# print(
#     f'Greatest Decrease in Profits: {Greatest_decrease_date } (${Greatest_decrease})')

# exit()

output = f"""
  Financial Analysis
  ----------------------------
  Total Months: {Total_number_months}
  Total: ${Profit_Losses_Total}
  Average  Change: ${Changes_total / Change_count:.2f}
  Greatest Increase in Profits: {Greatest_increase_date} (${Greatest_increase})
  Greatest Decrease in Profits: {Greatest_decrease_date } (${Greatest_decrease})
"""

print(output)

with open(outputpath, 'w') as output_file:
    output_file.write(output)
