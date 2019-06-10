
# import dependencies
import os
import csv

#initialize variables
month = []      # list to store month values in input file
net = []        # list to store profit/loss values in unput file
maxval = 0      # keep track of the maximum net value
minval = 0      # keep track of the minimum net value

# create file object for input file
budget_csv = os.path.join('budget_data.csv')

# using a with statement, create the file object to pass to the reader
with open(budget_csv,newline='',encoding='utf-8-sig') as csvfile:

    # create the reader object
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # skip the header row
    headers = next(csvreader)

    # build the lists of months and corresponding profit/loss
    for row in csvreader:
            month.append(row[0])
            net.append(int(row[1]))


# now begin the anlaysis

# keep track of the index and the value
for index,val in enumerate(net):
    if val > maxval:
        maxval = val
        maxind = index
    elif val < minval:
        minval = val
        minind = index


#print to the terminal
print()
print('Financial Analysis')
print('-'*30)
print(f'Total Months: {len(month)}')
print(f'Total: ${sum(net):,.0f}')
print(f'Average Change: ${sum(net)/len(net):,.2f}')
print(f'Greatest Increase in profits: {month[maxind]} (${maxval:,.0f})')
print(f'Greatest Decrease in profits: {month[minind]} (${minval:,.0f})')
print()

# using with statement, create the file object to pass to the writer
with open('pybank.txt','w')  as file_out:

    # write the analysis results
    file_out.write('Financial Analysis\n')
    file_out.write('-'*30 + '\n')
    file_out.write(f'Total Months: {len(month)}\n')
    file_out.write(f'Total: ${sum(net):,.0f}\n')
    file_out.write(f'Average Change: ${sum(net)/len(net):,.2f}\n')
    file_out.write(f'Greatest Increase in profits: {month[maxind]} (${maxval:,.0f})\n')
    file_out.write(f'Greatest Decrease in profits: {month[minind]} (${minval:,.0f})\n')