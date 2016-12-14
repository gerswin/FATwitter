from stem import Signal
from stem.control import Controller
import requests
import time

def renew():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate("my_password")
        controller.signal(Signal.NEWNYM)
        controller.close()




for i in range(1,1000):
    proxies = {
        'http': 'http://127.0.0.1:8118',
    }
    url = "http://www.tuvotacion.com/voto.php"

    payload = {"id_votacion": 399871, "opcion": 1526592, "ingles": ""}
    headers = {
        'origin': "http://www.tuvotacion.com",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'referer': "http://www.tuvotacion.com/chica-popularidad-globe-tachira-2016"

    }

    try:
        response = requests.request("POST", url, data=payload, headers=headers,proxies=proxies, timeout=10)
        print(response.status_code)
    except Exception as e:
        pass

    renew()
    time.sleep(10)


