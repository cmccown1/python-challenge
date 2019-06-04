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



print("Financial Analysis")
print("------------------------------")
print (f"Total Months: {len(month)}")
print (f"Total: {sum(net)}")
print (f"Average Change: {sum(net)/len(net)}")
print(f"Greatest Increase in profits: {month[maxind]} ({maxval})")
print(f"Greatest Decrease in profits: {month[minind]} ({minval})")