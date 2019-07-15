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
access_token = "xxxxxx"
access_token_secret = "xxxxxxx"
consumer_key = "xxxxxx"
consumer_secret = "xxxxxxx"

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
