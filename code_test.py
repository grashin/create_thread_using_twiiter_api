def post_line(text):
	tweets = []
	print('text = ', text)
	print('len==', len(text))
	if len(text)<280:
		tweets.append(text)
		print('tweets = ', tweets)
		return tweets
	last_dot_tweet, counter = 0, -1
	for i in range(10):
		# print(text[counter+2])
		position_of_dot = text[counter+1:].find('.')
		counter += position_of_dot + 1
		print('pos of dot = ', position_of_dot, last_dot_tweet, counter)
		if counter-last_dot_tweet>280:
			tweets.append(text[last_dot_tweet:counter-position_of_dot])
			last_dot_tweet = counter - position_of_dot
	tweets.append(text[last_dot_tweet:counter])
	print('tweets = ', tweets)
	return tweets

file = open("text_movies.txt", "r")

for line in file:
	tweets = post_line(line)
