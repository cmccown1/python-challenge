# import dependencies
import os
import csv

# initialize variables
candidate = []  # store the candidate (vote) values from the input file
unique = []     # store a list of unique values in the candidate list
result = []     # store a list of condidate (vote) counts for each unique 

election_csv = os.path.join('election_data.csv')

with open(election_csv,newline='',encoding='utf-8-sig') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    
    #skip the header row
    headers = next(csvreader)
    # print(f'headers: {headers}')

    for row in csvreader:
         candidate.append(row[2])

for vote in candidate:
    if not vote in unique:
        unique.append(vote) 

print()
print('Election Results')
print('-'*30)
print(f'Total Votes: {len(candidate):,.0f}')
print('-'*30)

for talley in unique:
    counter = 0
    for vote in candidate:
        if talley == vote:
            counter += 1
    result.append(counter)
    print(f'{talley}: {counter/len(candidate)*100:.3f}% ({counter:,.0f})')

print('-'*30)

wincount = result[0]
winindex = 0
for index,winner in enumerate(unique):
    if result[index]>wincount:
        wincount = result[index]
        winindex = index
print(f'Winner: {unique[winindex]}')

print('-'*30)
print()



# file_out = open('pybank.txt','w') 

# file_out.write('Financial Analysis\n')
# file_out.write('------------------------------\n')
# file_out.write(f'Total Months: {len(month)}\n')
# file_out.write(f'Total: ${sum(net):,.0f}\n')
# file_out.write(f'Average Change: ${sum(net)/len(net):,.2f}\n')
# file_out.write(f'Greatest Increase in profits: {month[maxind]} (${maxval:,.0f})\n')
# file_out.write(f'Greatest Decrease in profits: {month[minind]} (${minval:,.0f})\n')

# file_out.close()