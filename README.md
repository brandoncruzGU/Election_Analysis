# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. The audit compared the number of votes that each candidate recieved to determine the winner of the election. The board also wanted to know which county had the most amount of voters who voted during this election.

These are the main objectives that we will address in this analysis:

Determining the largest voter turnout:
  1. Calculate the total number of votes from above.
  2. Calculate the number of votes casted in each county.
  3. Calculate the percentage of votes casted by each county.
  4. Determine the county with the largest amount of voters who participated in this election.

Determining the election results:
  1. Use the total number of votes cast.
  2. Get a complete list of candidates who recieved votes.
  4. Calculate the total number of votes each candidate recieved.
  5. Calculate the percentage of votes each candidate won.
  6. Determine the winner of the elections based on popular vote.



## Resources
  >Data Source: election_results.csv
  >Software: Python 3.6.1, Visual Studio Code, 1.38.1
  
## Election Audit Results
There were a total of 369,711 votes cast in this election. 

By using a for loop to calculate the number of votes per county, we find that the largest voter turnout is from residents in Denver county.
![county_for_loop](https://user-images.githubusercontent.com/107777321/179902187-be4e436b-d2e4-42de-b019-83394f13f0fa.png)


82.8% (306,055) of the total votes were cast by residents in Denver county.
10.5% (38,855) of the total votes were cast by residents in Jefferson county.
6.7% (24,801) of the total votes were cast by residents in Arapahoe county.

By slightly adjusting the variables in the for loop, we were able to identify which candidate won the race. The candidates in this election are Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. After identifying the candidates in this election, we created the for loop below to calculate the amount of votes each candidate recieved.

![Screenshot 2022-07-19 220103](https://user-images.githubusercontent.com/107777321/179900970-8d3df909-b93c-493e-bb28-0d3bd7b6ef31.png)

Raymon Anthony Doane recieved 11, 606 votes which is "3.1%" of the total votes. 
Charles Casper Stockham recieved 85,213 votes which is 23.0% of the total votes.
Diana DeGette recieved 272,892 votes which is 73.8% of the total votes. 

This means that Diana DeGette recieved the most of amount of votes and is the winner of this election.
    
## Election Audit Summary
This script used in this audit provides the opportunity to conduct similar studies for other elections in Colorado as well as other types of elections. We can use the script here to analyze other levels of elections such as school boards, city councils, senatores, etc.

The script can also be adjusted to analyze elections within different geographical areas. This script can be changed to include state or federal level elections. We can also look at the way the state divides their congressional seats to calculate the election results based on those regions as well.
