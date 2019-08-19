import tweepy

# Authenticate Your Credentials

#
auth = tweepy.OAuthHandler("API key", "API secret key")

auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth)

# Method: List of peope who you blocked:

print("\n")
print("Blocked people: ")
for b in api.blocks():
	print(b.name)
