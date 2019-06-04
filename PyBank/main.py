import os
import csv

budget_csv = os.path.join("budget_data.csv")

month = []
net = []
maxval = 0
minval = 0

with open(budget_csv,newline="",encoding='utf-8-sig') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    
    headers = next(csvreader)

    for row in csvreader:
            month.append(row[0])
            net.append(int(row[1]))

for index,val in enumerate(net):
    if val>maxval:
        maxval = val
        maxind = index
    elif val<minval:
        minval = val
        minind = index


# :,.2f   :,f try these for formatting
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {len(month)}")
print(f"Total: ${sum(net):,.0f}")
print(f"Average Change: ${sum(net)/len(net):,.2f}")
print(f"Greatest Increase in profits: {month[maxind]} (${maxval:,.0f})")
print(f"Greatest Decrease in profits: {month[minind]} (${minval:,.0f})")


file_out = open("pybank.txt","w") 

file_out.write("Financial Analysis\n")
file_out.write("------------------------------\n")
file_out.write(f"Total Months: {len(month)}\n")
file_out.write(f"Total: ${sum(net):,.0f}\n")
file_out.write(f"Average Change: ${sum(net)/len(net):,.2f}\n")
file_out.write(f"Greatest Increase in profits: {month[maxind]} (${maxval:,.0f})\n")
file_out.write(f"Greatest Decrease in profits: {month[minind]} (${minval:,.0f})\n")

file_out.close()