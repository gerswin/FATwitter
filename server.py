
import logging
import json
import flask
from flask import Flask
from flask import request
from models import Tokens
from models import Sms
from cnf import *
from login import tweetAuth
from collections import Counter
import re

app = Flask(__name__)

tweets = tweetAuth(CONSUMER_TOKEN, CONSUMER_SECRET, CALLBACK_URL)
logging.basicConfig(filename='server.log', level=logging.INFO)


@app.route("/")
def send_token():

    return flask.render_template('index.html')


@app.route("/start")
def start_verification():

    try:
        return flask.redirect(tweets.getAuthUrl())
    except Exception as e:
        print(e)
        return flask.render_template('err.html', err= 'Error! Failed to get request token')


@app.route("/verify")
def get_verification():
    verifier = request.args['oauth_verifier']

    try:
        api = tweets.makeAuthApi(verifier)
    except Exception as e:
        logging.warning(e)
        print("verify",e)

    try:
        me = api.me()

        tweets.saveExtend(me.screen_name, me.id)
    except Exception as e:
        logging.warning(e)
        print("verify", e)

    return flask.redirect(flask.url_for('start'))

@app.route("/lostokens")
def the_tokens():

        return flask.render_template('mt.html', tokens=Tokens.select())

@app.route("/sms")
def the_sms():
        sms = Sms.select()
        text = []
        for s in sms:
            if len(s.sender) > 5:
                if not "MOVISTAR" in s.sender:
                    if not "Movistar te informa" in s.fullsms:
                        words = re.findall(r'\w+', s.fullsms.lower())
                        s.cm = Counter(words).most_common(10)
                        text.append(s)
        text.reverse()
        return flask.render_template('sms.html', sms=text)

@app.route("/savesms")
def save_sms():
    sms = request.args['sms']
    fullsms = request.args['fullsms']
    route = request.args['route']
    sender = request.args['sender']
    text = Sms(sms=sms,fullsms=fullsms,route=route,sender=sender)
    text.save()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/done")
def start():

    api = tweets.getAuthApi()
    try:
        return flask.render_template('tweets.html', tweets=api.user_timeline(FOLLOW_USER))
    except Exception as e:
        logging.warning(e)
        return flask.redirect(flask.url_for('send_token'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
