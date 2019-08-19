import tweepy

# Authenticate Your Credentials

auth = tweepy.OAuthHandler("API key", "API secret key")

auth.set_access_token("Access token", "Access token secret")


# API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Method: TimeLine Last 20 Tweets on Your Timeline

timeline = api.home_timeline()
for tweet in timeline:
	print(f"{tweet.user.name} said {tweet.text}")
