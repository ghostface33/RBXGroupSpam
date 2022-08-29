from flask import Flask
from threading import Thread
import requests
import os
cookie = os.getenv("XD")
xsrf = ''
url = 'https://groups.roblox.com/v1/groups/%s/relationships/allies/%s'
authurl = 'https://auth.roblox.com/v2/logout'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
app=Flask("")
@app.route("/")
def index():
    return xsrf
def getXsrf():
    xsrfRequest = requests.post(authurl, headers={
        'User-Agent': userAgent
    }, cookies={
        '.ROBLOSECURITY': cookie
    })
    if xsrfRequest.headers['x-csrf-token']:
        return xsrfRequest.headers['x-csrf-token']
    else:
        return ''
Thread(target=app.run,args=("0.0.0.0",8080)).start()
while True:
 xsrf = getXsrf()
 index()



