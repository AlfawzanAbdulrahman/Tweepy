import tweepy

# Authenticate Your Credentials

#
auth = tweepy.OAuthHandler("API key", "API secret key")

auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth)

# Method: Print all top Trends.

print("Trends: ")
trend = api.trends_place(1)
for t in trend[0]["trends"]:
	print(t["name"])
