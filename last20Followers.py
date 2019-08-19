import tweepy

# Authenticate Your Credentials

#
auth = tweepy.OAuthHandler("API key", "API secret key")

auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth)

# Method: Printing the last 20 followers:

user = api.get_user("YourUserName")
print("User Details:")
print(user.name)
print(user.description)
print(user.location)

print("The Last 20 Followers: ")
for f in user.followers():
	print(f.name)
