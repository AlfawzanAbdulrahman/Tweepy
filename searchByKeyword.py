import tweepy

# Authenticate Your Credentials

#
auth = tweepy.OAuthHandler("API key", "API secret key")

auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth)

# Method: Search by a keyword in a specific language

print("Search By keyword: ")

for tweet in api.search(q="Python", lang="en", rpp=10):
	print(f"{tweet.user.name}:{tweet.text}")
	print("\n")
