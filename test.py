import requests
from proxies import theProxies
import threading
from queue import Queue
import time
import random
lock = threading.Lock()
proxy = theProxies()



def saveIvssPersona(info, debug=False):
    with lock:
        current = threading.current_thread().name
        prox = proxy.getProxy()

        url = "http://www.tuvotacion.com/voto.php"

        payload = {"id_votacion":399871,"opcion":1526592,"ingles":""}
        headers = {
            'origin': "http://www.tuvotacion.com",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            'content-type': "application/x-www-form-urlencoded",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'referer': "http://www.tuvotacion.com/chica-popularidad-globe-tachira-2016",
            'X - Http - Forwarded - For':prox['http']
        }

        try:
            response = requests.request("POST", url, data=payload, proxies=prox,headers=headers,timeout=10)
            print(response.status_code, current)
        except Exception as e:
            pass



"""""""""""
# The worker thread pulls an item from the queue and processes it
def worker():
    while True:
        item = q.get()
        saveIvssPersona(item)
        q.task_done()


# Create the queue and thread pool.
q = Queue()
for i in range(50):
    t = threading.Thread(target=worker)
    # thread dies when main thread (only non-daemon thread) exits.
    t.daemon = True
    t.start()

# stuff work items on the queue (in this case, just a number).
start = time.perf_counter()

for i in range(4000):
    q.put({'cedula': "cela"})

q.join()
""""""""""""""