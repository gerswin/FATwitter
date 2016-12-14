from requests import session
import time
import random
def vote(login):
    payload = {
        'clave': '00000',
        'confirma_clave': "00000",
        'email':login+'@divismail.ru',
        'nick': login
    }
    cant = ['1526595', '1526598', '1526597', '1526589', '1526601', '1526588', '1526599', '1526599', '1526596',
            '1526594', '1526590']

    #payload2 = {"id_votacion": 399871, "opcion": 1526592, "ingles": ""}
    payload2 = {"id_votacion": 399871, "opcion":random.choice(cant), "ingles": ""}

    url = "http://www.tuvotacion.com/voto.php"

    headers = {
        'origin': "http://www.tuvotacion.com",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'referer': "http://www.tuvotacion.com/chica-popularidad-globe-tachira-2016"

    }
    with session() as c:
        c.post('http://www.tuvotacion.com/inscripcion.php', data=payload,allow_redirects=False)
        try:
            response = c.request("POST", url, data=payload2, headers=headers,timeout=10)
            print(response.status_code)
        except Exception as e:
            print(e)
            pass
    time.sleep(2)

for i in range(6000,7000):
    vote("%012d" % ( i, ))