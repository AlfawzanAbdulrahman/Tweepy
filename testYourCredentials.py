import tweepy

# Authenticate Your Credentials

#
auth = tweepy.OAuthHandler("API key", "API secret key")

auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth)

# Checking for your Credentials

try:
    api.verify_credentials()
    print("Your Credentials Are Correct")
except:
    print("Error With Your Credentials")
