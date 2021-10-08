# Election_Analysis
## Project Overview - explain the purpose of this election audit analysis
A member of the Colorado Board of Elections has tasked me to complete an election audit of the US Congressional precinct election in Colorado, including analysis of the candidates and county votes.

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes for each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote
6. Get a complete list of counties in the elections
7. Calculate the total number of votes for each County
8. Calculate the percentage of the total vote from each County
9. Determine the county with the largest voter turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code, 1.38.1

## Election-Audit Results
- There were 369,711 total votes cast in this election
    - This was achieved with the following code inside a `for` loop, tallying the total number of votes as it looped through each row
    `total_votes = total_votes + 1`
- The county results were:
  - Jefferson County received 10.5% of the vote and 38,855 votes
  - Denver County received 82.8% of the vote and 306,055 votes
  - Arapahoe County received 6.7% of the vote and 24,801 votes
    - These results were achieved using a dictionary to keep track of each county (as the key) and the county's votes (as the value). As I looped through each row of the csv, I used the following code to tally the county votes
    ```
    # county does not match any existing county in the county list.
        if county_name not in county_list:
            # Add the existing county to the list of counties.
            county_list.append(county_name)
            # Begin tracking the county's vote count.
            county_votes_dict[county_name] = 0
        # Add a vote to that county's vote count.
        county_votes_dict[county_name] += 1
    ```
- The county with the largest turnout was Denver County, with 82.8% of the vote
  - Using variables `winning_county_count` and `winning_county` I was able to use the following code to reassign the variables with the county with the highest vote count as it looped through the rows
  ```
  if county_votes > winning_county_count:
            winning_county_count = county_votes
            winning_county = county_name
  ```
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
  - Diana DeGette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
    - This was achieved with similar code to the county vote counts. The percentages were calculated as `vote_percentage = float(votes) / float(total_votes) * 100` with the print statement confining the percentage to the tens place: `f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")`
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes

## Election-Audit Summary

In the end, this code was able to run through the csv file (which included the Ballot ID, County, and Candidate voted for) to summarize the number of votes for each candidate and voter turnout for each county. This code could be modified to be useful for any type of election. If the csv file is formatted the same, only minimal changes would need to be made to the code to produce similar results.

For example, if we wanted to use this code for local county elections, instead of having a county column in the csv, we could include the position that is being elected (i.e. mayor, county commissioner, city council member, etc). We could then use this code to audit vote counts, percentages, and winners for each candidate of each position all in one go.

Similarly, this could even be used for Presidential elections. We could adjust the code that keeps track of the counties to track state votes. In the primaries, we could also adjust the code to keep track of the party affiliation of each candidate.

Essentially, as long as the data is formatted the same as the input data here, the code could be adjusted slightly to keep track of votes for candidates in a variety of different categories, whether that be counties, states, elected positions, and more.
