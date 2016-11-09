# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
import requests
import nltk
from textblob import TextBlob

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

cfg = {
        "consumer_key" : "mHkUkEadhj0vb6lJoNRUNem2A",
        "consumer_secret" : "LIoMZWcPvOtx2E8mrX36ZxlaNWDvTuLyPJZn2MYPlv70wekd7Z",
        "access_token" : "791422914583298050-m0XgfqVnPO7hJSH2Oe37nuNQxLNnu6X",
        "access_token_secret" : "8dpUtkGfsRJNdeUl3Ya140EPWYx8tG7mzbArAlD7TIPED"
    }

api = get_api(cfg)
avgSub = 0.0
avgPol = 0.0
count = 0
term = input("Please enter search term: ")
results = api.search(q = term)

for tweet in results:
    print(tweet.text)
    avgSub = TextBlob(tweet.text).sentiment.subjectivity
    avgPol += TextBlob(tweet.text).sentiment.polarity
    count += 1

avgSub = avgSub/count
avgPol = avgPol/count

print("Average subjectivity is " + str(avgSub))
print("Average polarity is " + str(avgPol))
