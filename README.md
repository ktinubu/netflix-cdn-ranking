# Netflix cdn ranking and selection
    

Writes a CSV file showing the rankings that netflix gives its CDN for streaming contentent to a user for a given movie

## Requirements

netflix-cdn-ranking uses python3 and pip. To install requirements, run:\
    `pip3 install -r requirements.txt`
  

## Instructions

### 1.Fork repo

### 2.Set the following environment variables:

`NFLIXACCOUNTS`: email and passwords\
`NFLIXLOCATION`: location of machine that code is running on\
`NFLIXMOVIES`: list of netflix movie IDs

##### Examples:

    NFLIXACCOUNTS=user1:password1,user2:password2
    NFLIXLOCATION=us-east-1
    NFLIXMOVIES=0186608,80115431,70116817

### 3.Enter directory

### 4.Run
    chmod755 getdata.sh
    getdata.sh
    
## View ouput
Output is in a csv file named rankings.csv
