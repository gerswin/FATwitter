from peewee import *
from playhouse.db_url import connect

#db = SqliteDatabase('tokens.db')
db = connect('mysql://root:16745665@159.203.155.203:3306/fernando')

class Tokens(Model):
    user = CharField(unique=True)
    idt = CharField()
    client = CharField()
    secret = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.


class RawTokens(Model):
    client = CharField(unique=True)
    secret = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Tweets(Model):
    tid = CharField(unique=True)
    send = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.


class Sms(Model):
    sender = CharField()
    fullsms = CharField()
    sms =CharField()
    read=BooleanField(default=False)
    route = CharField()
    class Meta:
        database = db # This model uses the "people.db" database.



db.connect()
#db.create_tables([Tokens, RawTokens], safe=True)
#db.create_tables([Sms], safe=True)

