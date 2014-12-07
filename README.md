pfch_final_proj
===============

These are the two scripts I used to complete my project, with my API tokens removed.

here is an explanation of my project:
For my final project, I used Twitter’s REST API and a Twitter library for python, called twitter-python, to acquire the timelines of over 500 self-identified teachers on Twitter. I then used python to parse, extract, and structure the user timeline data for a visualization program. I was interested in seeing the ways in which teachers were engaging with one another online, so I used the mentions that each Twitter user made as a way to measure this. A mention, I would argue, is telling of engagement, as the user actively chooses an individual to include in their tweet, or directs the contents of their tweet at someone. The result of my data collection and structuring is a force-directed network visualization, showing 

The acquisition and structuring of my data took place over two separate python scripts, run from the command line. Before writing my scripts however, I had to gain access to the Twitter API by acquiring access keys and tokens. Once I had these two items, I was able to begin writing my scripts. I used a library that interacts with the Twitter API called twitter-python, as it was one of the few Twitter libraries for python that can get user timeline data. All of the Twitter handles whose timelines I was interested in acquiring were stored in a csv file, housed in the same directory as the rest of my python scripts. 

The first script reads the csv file for the user’s handle, makes the call to the API and acquires the user’s timeline data, and structures the data into an individual JSON file. Because the Twitter API only allows for a certain number of requests to be made over a period of time, I had to run the script, exceed my request limit, track the last user whose timeline data I acquired and update the csv to avoid re-requesting data for users, and then run the script again. Once I had acquired the data for all of the users, I then had to structure it.

My second script extracts the data that I want from the JSON file, structures it, and writes it to a csv file. To do this, I wrote a script that reads the JSON file and selects the Twitter user’s handle and the handles of all the individuals that have been mentioned by the Twitter user. The script stores the extracted information as a dictionary, where the key is each teacher Twitter user, and the value is a list of all of the users they mention. Finally, the script writes this information to a csv. In the csv, the first column is the key/teacher/source and the second column is the value/user mentioned/target. 

Once the csv was created, I input it into Gephi, and created the visualization. 

It would be possible to use these scripts if you are another user, but you would have to have your own tokens, and make sure to update the file paths for reading and writing the JSON and csv files. 
