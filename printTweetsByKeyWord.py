import tweepy

# Authenticate Your Credentials

#
auth = tweepy.OAuthHandler("API key", "API secret key")

auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth)

# Method: Print Tweets by a keyword in a specific language and specific


try:
	numOfTwwets = 10
	file = open("tweets.txt", "w+")
	for tweet in api.search(q="DePaul University", lang="en", rpp=numOfTwwets):
		file.write(f"{tweet.user.name}:{tweet.text}")
		file.write(4*"\n")

except IOError:
	file = open(file, "w+")
file.close()


print("{} tweets have been printed in the file named {} ".format(numOfTwwets, file.name))
