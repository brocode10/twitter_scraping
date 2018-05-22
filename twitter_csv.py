#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:33:23 2018

@author: shonak
"""
from __future__ import print_function
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv

from pymongo import MongoClient

#Variables that contains the user credentials to access Twitter API 
access_token = "997064128249262080-DGEtTgqYfwIOjq72zFcBLy0rbqLPes1"
access_token_secret = "j5AumygTwpPPe4UqVbSP7FdtGfZ6nLowPXWAsmjAbHgAb"
consumer_key = "kb4zGrnI4Dth9gZlUGiwviCL0"
consumer_secret = "ZdyTjtYhZ4jwobXHWnXiTnb2WilFAbZm73PPYONAvfBPZpmygE"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)


#####United Airlines
# Open/Create a file to append data
csvFile = open('tech.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=("technology"),count=100,
                           lang="en",
                           since="2017-04-03").items():
   print (tweet.created_at, tweet.text)
   #print (tweet.text)
   csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
   #csvWriter.writerow([tweet.text.encode('utf-8')])