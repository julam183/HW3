# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy
import requests

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def tweet(image, message):
    cfg = {
        "consumer_key" : "mHkUkEadhj0vb6lJoNRUNem2A",
        "consumer_secret" : "LIoMZWcPvOtx2E8mrX36ZxlaNWDvTuLyPJZn2MYPlv70wekd7Z",
        "access_token" : "791422914583298050-m0XgfqVnPO7hJSH2Oe37nuNQxLNnu6X",
        "access_token_secret" : "8dpUtkGfsRJNdeUl3Ya140EPWYx8tG7mzbArAlD7TIPED"
    }

    api = get_api(cfg)
    img = 'temp.jpg'
    request = requests.get(image, stream = True)
    if request.status_code == 200:
        with open(img, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    api.update_with_media(img, status = message)
    print("success")

url = "https://s-media-cache-ak0.pinimg.com/564x/3c/d2/a8/3cd2a844037b921028481f9f3f82d21f.jpg"
message = "#UMSI-206 #Proj3 #UMSI206"
tweet(url, message)