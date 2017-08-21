# coding=utf8
# !/usr/bin/python

import threading
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template, abort

import longlive
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
        print "ttttt"
        while True:
            message = ws.receive()
            if message=="stop":
                newSocket = WebSock(ws, 0)
            else:
                newSocket = WebSock(ws, message)
            newSocket.start()
    return "Connected!"

class WebSock(threading.Thread):

    def __init__(self, ws,messages):
        threading.Thread.__init__(self)
        self.ws = ws
        self.messages = messages

    def run(self):
        time.sleep(1)
        print self.messages

        longlive.start(self.ws,self.messages)

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()