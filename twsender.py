from iron_mq import *
import json
import tweepy
from cnf import *
import time

users = []
ironmq = IronMQ(host='mq-aws-eu-west-1-1.iron.io',
                project_id='5763516ab7409e00071268bd',
                token='_ppJdHd8vlrK9ZsUC4RmoxmoFow',
                protocol='https', port=443,
                api_version=3,
                config_file=None)

q = ironmq.queue('tweets')



def rtAll(data):
    realData = json.loads(data['body'])
    auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
    auth.set_access_token(realData['client'], realData['secret'])
    api = tweepy.API(auth)
    try:
        api.retweet(realData['tweet'])
    except Exception as e:
        print(e)





while q.size() > 0:
    print(q.size())
    msg = q.reserve(delete=True)
    rtAll(msg["messages"][0])
    time.sleep(15)
