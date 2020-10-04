import os
import tweepy as tw
import pandas as pd

def get_last_tweet_id(username): 
        tweets = api.user_timeline(screen_name=username,count = 1) 
        return tweets[0].id

consumer_key = 'your_key' 
consumer_secret = 'your_key' 
access_token = 'your_key' 
access_token_secret = 'your_key' 

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

file = open("text_to_post.txt", "r")
i = 0
for line in file:
	i+=1
	text_to_post = str(line)
	media_name = "photos/img_"+str(i)+".jpg"
	media = api.media_upload(media_name)
	if i == 1:
		api.update_status(status=text_to_post, media_ids=[media.media_id])
	else:
		tweetid = get_last_tweet_id('your_username')
		api.update_status(status=text_to_post, media_ids=[media.media_id], in_reply_to_status_id = tweetid)

print('Done')