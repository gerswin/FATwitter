from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase("proxies2.sqlite")


class BaseModel(Model):
    class Meta:
        database = db


class Proxies(BaseModel):
    ip = CharField(unique=True)
    protocol = CharField(unique=False)
    rate = IntegerField(default=0)


db.connect()


def readProxyList():
    proxylist = []
    with open("p.list") as f:
        for line in f.readlines():
            try:
                currentPerson = Proxies.create(ip=line.rstrip(), protocol="http", rate=0)
                currentPerson.save()
            except IntegrityError as e:
                # print("duplicate",e)
                pass


#db.create_tables([Proxies])

readProxyList()