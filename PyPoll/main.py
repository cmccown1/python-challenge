# import dependencies
import os, csv

# initialize variables
candidate = []  # store the candidate (vote) values from the input file
unique = []     # store a list of unique values in the candidate list
result = []     # store a list of candidate (vote) counts for each unique 

# set the file path for the input file
election_csv = os.path.join('election_data.csv')

# open, read, close the input file using with
# create the file object to pass to the reader
with open(election_csv,newline='',encoding='utf-8-sig') as csvfile:

    #create the reader object    
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #skip the header row
    headers = next(csvreader)

    # store the candidate (vote) values    
    for row in csvreader:
         candidate.append(row[2])



# begin the analysis

# build a list of unique candidates who received at least one vote
for vote in candidate:
    if not vote in unique:
        unique.append(vote) 


# write to file while printing to terminal so as not to repeat the analyis a second time
# (could also create a bunch variables to store things)

# define the ouput path and filename
output = 'pypoll.txt'

# open, write to, and close the text file within a with statement
with open(output,'w') as file_out:

    # print the header and total votes
    print('Election Results')
    print('-'*30)
    print(f'Total Votes: {len(candidate):,.0f}')
    print('-'*30)

    # write same to text file
    file_out.write('Election Results\n')
    file_out.write('-'*30 + '\n')
    file_out.write(f'Total Votes: {len(candidate):,.0f}\n')
    file_out.write('-'*30 + '\n')

    # loop through the unique candidates and count the vote totals that match each candidate
    for talley in unique:
        voteCount = 0
        for vote in candidate:
            if talley == vote:
                voteCount += 1
        # store the vote count for each unique candidate to determine the winner
        # the results are stored in the same order as the list of unique candidates
        result.append(voteCount)

        # print the vote count for each unique candidate
        print(f'{talley}: {voteCount/len(candidate)*100:.3f}% ({voteCount:,.0f})')

        # write same to output file
        file_out.write(f'{talley}: {voteCount/len(candidate)*100:.3f}% ({voteCount:,.0f})\n')


    # print/write a separator line for readability
    print('-'*30)
    file_out.write('-'*30 + '\n')

    # use the ordered list of unique candidates and the ordered list of results to determine the winner
    wincount = result[0]
    winindex = 0
    for index,winner in enumerate(result):
        if result[index] > wincount:
            wincount = result[index]
            winindex = index

    # print the winner
    print(f'Winner: {unique[winindex]}')
    print('-'*30)

    # write same to output file
    file_out.write(f'Winner: {unique[winindex]}\n')
    file_out.write('-'*30 + '\n')
        