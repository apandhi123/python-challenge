# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

csvpath = os.path.join('budget_data_1.csv')
# csvpath1 = os.path.join('budget_data_2.csv')

with open(csvpath) as csvfile:
  #   open(csvpath1) as csvfile2:   

    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.reader(csvfile)
    # csvreader2 = csv.reader(csvfile2, delimiter=',')
    next(reader,None)

    data = list(reader) 

    # Variables to Track

    Total_months = 0
    Total_Revenue = 0
    Revenue_avg = 0
    revenue_change = 0
    prev_revenue = 0
    greatest_inc = 0
    greatest_dec = 9999999999999999999999
    idate = ""
    ddate = ""

    Total_months = len(data)

    for row in data:
        Current_row = int(row[1])
        Total_Revenue += int(row[1])

       # Set the Revenue average
        Revenue_avg = Total_Revenue/Total_months   
        
        # Keep track of changes
        revenue_change = int(row[1]) - prev_revenue
        
        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row[1])

        # Determine the greatest increase
        if (revenue_change > greatest_inc):
            greatest_inc = revenue_change
            idate = row[0]
            # greatest_inc[0] = row["Date"]

        if (revenue_change < greatest_dec):
            greatest_dec = revenue_change
            ddate = row[0]
            

            # Add to the revenue_changes list
            #  revenue_change.append(int(row[1]))
        
            

 # show output  
print("Financial Analysis")
print("Total Months", Total_months)
print("Total Revenue", "$", Total_Revenue)
print("Revenue_avg", Revenue_avg)
print("revenue_change", revenue_change)
print("Greatest Increase: " + idate + " $"+str(greatest_inc) +"\n")
print("Greatest Decrease: " + ddate + " $"+str(greatest_dec) +"\n")

file_to_output = "PyBankAnswer.txt"
with open(file_to_output, "w") as txt_file:
        txt_file.write("Total Months: ")
        txt_file.write(str(Total_months))
        txt_file.write("\n")
        txt_file.write("Total Revenue: ")
        txt_file.write(str(Total_Revenue))
        txt_file.write("\n")
        txt_file.write("Average Change: ")
        txt_file.write(str(revenue_change))
        txt_file.write("\n")
        txt_file.write("Greatest Increase: ")
        txt_file.write(idate + " $"+str(greatest_inc))
        txt_file.write("\n")
        txt_file.write("Greatest Decrease: ")
        txt_file.write(ddate + " $"+str(greatest_dec))