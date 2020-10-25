import os
import tweepy as tw
import pandas as pd
import os

def get_last_tweet_id(username): 
	tweets = api.user_timeline(screen_name=username,count = 1) 
	return tweets[0].id
def post_line(text):
	tweets = []
	length_of_text = len(text)
	if length_of_text<280:
		tweets.append(text)
		return tweets
	last_dot_tweet, counter = 0, -1
	while counter != length_of_text - 2:
		position_of_dot = text[counter+1:].find('.')
		counter += position_of_dot + 1
		if counter-last_dot_tweet>280:
			tweets.append(text[last_dot_tweet:counter-position_of_dot])
			last_dot_tweet = counter - position_of_dot
	tweets.append(text[last_dot_tweet:length_of_text])
	return tweets

consumer_key = 'your_key' 
consumer_secret = 'your_key' 
access_token = 'your_key' 
access_token_secret = 'your_key' 

username = 'username'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

file = open("text_movies.txt", "r")
line_number = -1
for line in file:
	line_number += 1 
	tweets_to_post = post_line(line)
	media_name = "./posters_of_movies/IMG_"+str(line_number)+".PNG"
	if os.path.isfile(media_name):
		media = api.media_upload(media_name)
	if line_number == 0:
			api.update_status(status=tweets_to_post[0])
	else:
		tweetid = get_last_tweet_id(username)
		if os.path.isfile(media_name):
			api.update_status(status=tweets_to_post[0], media_ids=[media.media_id], in_reply_to_status_id = tweetid)
		else:
			api.update_status(status=tweets_to_post[0], in_reply_to_status_id = tweetid)
	for tweet in tweets_to_post[1:]:
		tweetid = get_last_tweet_id(username)
		api.update_status(status=tweet, in_reply_to_status_id = tweetid)

print('Done')