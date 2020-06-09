#import dependencies
import csv
import os

# Add a variable to load a file from path
file_to_load = os.path.join("election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

# intialize a total vote counter 
total_votes = 0 
candidate_options = []
candidate_votes = {}
# track the winning candiate vote count adn percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#challenge
largest_county_turnout = ""
larges_county_votes = 0
with open(file_to_load) as electiond_data:
    reader = csv.reader
    print(reader)
    #read the header
    header = next(reader)
    print(header)
    #for each row in the csv file
    for row in reader:
        total_votes = total_votes + 1
    # get the candidate name 
    candidate_name = row[2]
    county_name = row[1]
    # If candidate does not match any existing candidate add into the list
    if candidate_name not in candidate_options:
        candidate_name.append(candidate_name)
        candidate_votes[candidate_name] = 0 

        candidate_votes[candidate_name] += 1

     #challengecounty 
    if county_name not in county_names:
        county_names.append(county_name)
        county_votes[county_name] +=1
    with open(file_to_save,"w") as txt_file:
       election_results = (
           f"\n Election Results\n"
           f"\n---------------------\n"
           f("Total Votes":{total_votes:,})
           f"\n-------------------------------\n"
           f"county votes: \n"

       )
       print(election_results,end = "")
       txt_file.write(electionresults)

    for country in county_votes:
        county_vote = county_votes[county]
        county_votes = int(county_votes)/int(total_votes) *100
        county_results = {
            f{county}:f{"county_percent".lf,}{county_vote}
            txt_file.write(county_votes)
        }
if(county_votes > largest_county_turnout)
    larges_county_votes = county_votes
    largest_county_turnout = county
txt_file.write(largest_county_turnout)
for candidate in candidate_votes:
    votes = candidate_votes(candidate)

candidate_results = {
    f'(candidate results') f'(vote_percentage')

}
txt.write(candidate_results) 


if(votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_candidate = candidate
    winning_percentage = vote_percentage
winning_candidate_summary = (
    f'("winning candidate':winning_candidate)
    f'(winning percentage': winning_percentage)
    f'winning vote count': winning_count_
)
txt_file.write(winning_candidate_summary)





