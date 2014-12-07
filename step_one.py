import twitter
import csv
import time
import json
teachers = []

api = twitter.Api(consumer_key='', 
consumer_secret='',
access_token_key='', 
access_token_secret='')

with open('twitterteachers.csv','r') as f:
	reader = csv.reader(f)

	for row in reader:
		teacher_handle = row[0]

		print(teacher_handle)
	
		all_of_this_teacher_tweets = []


		#here is the problem, you can only get 200 tweets at a time and you 
		#have to know the last tweet id you did in order ask for the next 200 starting from that id
		#so lets try to find the last 3000 tweets 

		try_to_find = 3000


		number_of_trys = 3000 / 200


		#so lets loop for that number of times (15) and keep track of what the last id was 
		#we dont know what the last id is yet, so lets just make it zero
		last_tweet_id = 0

		for try_number in range(0, number_of_trys):


			#if this is the first try (last_tweet_id == 0) then we cannot use that parameter yet
			if last_tweet_id == 0:

				statuses = api.GetUserTimeline(screen_name=teacher_handle,count=200)

			else:

				statuses = api.GetUserTimeline(screen_name=teacher_handle,count=200, max_id=last_tweet_id)


			#so now we have 200 tweets lets loop through them, add them to the big list and keep track of the tweet ids
			for a_status in statuses:
				last_tweet_id = a_status.id

				a_status = str(a_status)

				a_status = json.loads(a_status)
				
		
				

				all_of_this_teacher_tweets.append(a_status)


			#if the number of tweets is equal to one that means we have got them all (it is only return their first one)
			if len(statuses) == 1:

				#break the for loop since we don't need to try anymore we have them all
				break

			print "I have ", len(all_of_this_teacher_tweets), " tweets from this teacher so far!"
			time.sleep(2)



		#now you need to save the big list here as json using the teacher's handel as the filename

		with open('teacher/'+teacher_handle+'.json', 'w') as f:
 			f.write(json.dumps(all_of_this_teacher_tweets,indent=4))




