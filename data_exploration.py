# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "H9xp5a91XNCTVTozToBH5Cnxc"
consumer_secret = "av6KrAgP1VfBEVxtdwO2rJppHE4nad1DcPNbqHCmBXlnrR6PnZ"
access_token = "969399719125336064-BjEeNcwLmGFeDCXqhkhULzFbj48zG2x"
access_token_secret = "wlCzvVtSLHgZdrjQzNBhmNEWCQxbydoxVOuyASlz5v1R8" 

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

