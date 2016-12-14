from requests import session
import time
import random
def vote(login):
    payload = {
        'session[username_or_email]': '00000',
        'session[password]': "00000",
        'email':login+'@divismail.ru',
        'nick': login
    }
#    cant = ['1526595','1526592','1526591', '1526598', '1526597', '1526589', '1526601', '1526588', '1526599', '1526599', '1526596',
#            '1526594', '1526590']
    cant = ['1541237']
    #payload2 = {"id_votacion": 399871, "opcion": 1526592, "ingles": ""}
    payload2 = {"id_votacion": 404129, "opcion":random.choice(cant), "ingles": ""}

    url = "https://twitter.com/sessions"

    headers = {
        'origin': "https://twitter.com",
        'x-devtools-emulate-network-conditions-client-id': "4B5424CA-7DFD-4F69-8486-0FECFBFDE4B7",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'dnt': "1",
        'referer': "https://twitter.com/",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "es,en-US;q=0.8,en;q=0.6,zh-TW;q=0.4,zh;q=0.2",
        'cookie': "guest_id=v1%3A146852902150175742; lang=en; _gat=1; kdt=B6PSDDSDg41GrsYDVKB0L91VLadDyR84yUifZThI; remember_checked_on=1; dnt=1; _ga=GA1.2.1810714049.1468529029; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCD2SJutVAToMY3NyZl9p%250AZCIlMzc3ZjQ1MzliNTdmZTdkZDE0OTI0NTExZTk0ZmJlNDc6B2lkIiVmZWVk%250AYjUzNWQ2ZWQwMzhmYmVhNDFhZmMyYjY3MWMyZjoJdXNlcmwrCQBgF9JbgnMK--fdd397691003b530bcfd332e8a50c7b300339b70",
        'cache-control': "no-cache",
        'postman-token': "19f92dab-3c5d-a526-1978-dd198cf88d52"
    }

    with session() as c:
        c.post('http://www.tuvotacion.com/inscripcion.php', data=payload,allow_redirects=False)
        try:
            response = c.request("POST", url, data=payload2, headers=headers,timeout=10)
            print(response.status_code)
        except Exception as e:
            print(e)
            pass
#    time.sleep(2)

for i in range(90000,91000):
    vote("%012d" % ( i, ))