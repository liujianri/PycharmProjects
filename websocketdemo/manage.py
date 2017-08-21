# coding=utf8
# !/usr/bin/python

import threading
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template, abort


import sendss
import time

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('message.html')


@app.route('/message/')
def message():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        sendss.sets(3249500,10)
        while True:
            message = ws.receive()
            print message
            if message=="stop":
                mess="0"
            else:
                mess= message.split("=",1)[1]
            print mess
            newSocket = WebSocket(ws,int(mess))
            if message=="stop":
                print message
                newSocket.setDaemon(False)
            else:
                newSocket.start()
    return "Connected!"

class WebSocket(threading.Thread):
    def __init__(self, ws,count):
        threading.Thread.__init__(self)
        self.ws = ws
        self.count=count
    def run(self):
        time.sleep(1)
        co = 0
        while co < self.count:

            time.sleep(1)
            co += 1
            self.ws.send(str(co))
            print co
        self.ws.send("发送完毕")
        print "send ok"



if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()