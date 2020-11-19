# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:16:12 2020

@author: Bast
"""

import requests
import os



CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TOKEN = 'AAAAAAAAAAAAAAAAAAAAAF%2FeJQEAAAAAquGJRCtd1IUpbpoZiblp2n7IhoQ%3DU6SLWo0f3zcXe6rQERNCJAja8VI5TRHMTVOeafSDYAtcNtkfLV'
API_CALL = "https://api.twitter.com/1.1/statuses/show.json?id=1219755883690774529"
RES = requests.get(API_CALL,
                    headers={'Authorization': f'Bearer {TOKEN}'})

test = RES.json()
print(test)
firstKey = list(test.keys())[0]
if(firstKey != "errors"):
    print(test["created_at"])
    print(test["text"])
    print(test["user"]["location"])


# created_at, text, user location retweeted_status 'extended_tweet': {'full_text':


entries = os.listdir('LockdownDays/')
for entry in entries:
    # Using readlines() 
    print(entry)
    file1 = open("LockdownDays/"+entry, 'r') 
    Lines = file1.readlines() 

    # Strips the newline character 
    for line in Lines:
        print("TRAITEMENT LINE: ", line.strip())
        API_CALL = "https://api.twitter.com/1.1/statuses/show.json?id="+line.strip()
        tweet = requests.get(API_CALL,
                           headers={'Authorization': f'Bearer {TOKEN}'})
        
        my_json = tweet.json()
        
# http=1240410520705998848
# http=1240410518634053633
# http=1240406148882325505
# http=1240410518239744002
# http=1240410514745892865
# http=1240410505870704640
# http=1240399122072567810
# http=1240410502938931201
# http=1240410501718380545
# http=1240410496433623042
# http=1240410476472868864