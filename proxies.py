import random
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase


#db.create_tables([Cne, Persona, Parsed])
db = SqliteExtDatabase("proxies2.sqlite")
db.connect()

class BaseModel(Model):
   class Meta:
     database = db

class Proxies(BaseModel):
    ip = CharField(unique=True)
    protocol = CharField(unique=False)
    rate = IntegerField(default = 0)


class theProxies(BaseModel):

   def __init__(self):
      self.theList = self.readProxyList()
      self.removed = 0 
   
   def readProxyList(self):
       proxylist = []
       data = db.execute_sql("select ip from proxies order by random() limit 50")
       for proxy in data:
         proxylist.append(proxy[0])
       return proxylist

   def delProxyFromList(self,ip):
       #proxylist = readProxyList()
       if ip in self.theList:
           self.theList.remove(ip)
           self.removed += 1

   def getProxy(self):
       proxy = random.choice(self.theList)
       if(len(self.theList) < 10):
         self.theList +=  self.readProxyList()
       return {
           "http": proxy,
           "https": proxy,
       }

   def delProxyCount(self):
      return self.removed




