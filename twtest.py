from models import Tweets
from models import RawTokens
from cnf import *
from iron_mq import *
import json
import tweepy


users = []
ironmq = IronMQ(host='mq-aws-eu-west-1-1.iron.io',
                project_id='5763516ab7409e00071268bd',
                token='_ppJdHd8vlrK9ZsUC4RmoxmoFow',
                protocol='https', port=443,
                api_version=3,
                config_file=None)

q = ironmq.queue('tweets')
users = []

for token in RawTokens.select():
    users.append({"client": token.client, "secret": token.secret})



# lastTweet = Tweets.select().order_by(Tweets.id.desc()).get().tid


auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(users[0]['client'], users[0]['secret'])
api = tweepy.API(auth)

for update in api.user_timeline(screen_name="daniel7447d4rb4",count=5):
    try:
        print(update.id)
        tw = Tweets(tid=update.id,send="false")
        tw.save()
    except Exception as e:
        print(e)





