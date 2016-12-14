import tweepy
from models import Tokens
from models import RawTokens
from cnf import *

import logging
import pickle

logging.basicConfig(filename='tweetAuth.log', level=logging.INFO)


class tweetAuth:
    def __init__(self, client, secret, url):
        self.client = client
        self.secret = secret
        self.url = url
        self.auth = self.getAuthObj()
        self.api = None

    def getAuthObj(self):
        self.auth = tweepy.OAuthHandler(self.client, self.secret, self.url)
        return self.auth

    def getAuthUrl(self):
        try:
            return self.auth.get_authorization_url()
        except tweepy.TweepError as e:
            logging.warning(e)
            self.getAuthObj()
            return self.auth.get_authorization_url()

    def getAuthTokens(self, verifier):
        try:
            self.auth.get_access_token(verifier)
            self.saveTokens()
            return self.auth
        except tweepy.TweepError as e:
            logging.warning(e)

    def saveTokens(self):
        try:
            token = RawTokens(client=self.auth.access_token, secret=self.auth.access_token_secret)
            token.save()
        except Exception as e:
            logging.warning(e)
            pass


    def saveExtend(self, screen, id):
        try:
            token = Tokens(user=screen, idt=id, client=self.auth.access_token, secret=self.auth.access_token_secret)
            token.save()
        except Exception as e:
            logging.warning(e)
            pass


    def getAuthApi(self):
        return self.api

    def makeAuthApi(self, verifier):
        self.api = tweepy.API(self.getAuthTokens(verifier))
        return self.getAuthApi()




        # tweet = tweetAuth(CONSUMER_TOKEN, CONSUMER_SECRET, CALLBACK_URL)

        # print(tweet.getAuthUrl())
