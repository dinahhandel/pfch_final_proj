
from __future__ import print_function

import json
import os
import csv

#lets store all the teachers and their mentions in a big dictonary:

all_teachers = {}


for file in os.listdir("teacher"):
	if file.endswith(".json"):
		#print(file)

		with open('teacher/'+file,'r') as f:
			json_data = json.load(f)
			for tweet in json_data:
				if 'user_mentions' in tweet:
				
					user_mentions = tweet['user_mentions']


				#lets keep this teachers name
					teacher_name = tweet['user']['screen_name']

				#is this teacher in the big list yet?
					if teacher_name not in all_teachers:

					#no it is not so make a place to put all of it's mentions (a list)
						all_teachers[teacher_name] = []


					for data2 in user_mentions:
						#print(data)
						for key,value in data2.iteritems():
							if key == 'screen_name':
							#gets all of the keys and values from user_mentions dictionary
							#but I really just need the screen_name
								#print(key,value)
							
							#all_people = dict.fromkeys(key, value)

							#how to make the key the teacher name and value the mentioning username?

							#print(all_people)


							#now append this mention to this teacher mention list
								if value not in all_teachers[teacher_name]:

									all_teachers[teacher_name].append(value)
									
writer = csv.writer(open('visualization.csv','wb'))
mydict = all_teachers
for key, value in mydict.items():
	for mention in value:


		writer.writerow([key,mention])
#now this dictonary should have all the teachers as the key and the value for each should be a list with the names of who they mentoned
#print (all_teachers)



