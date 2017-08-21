# coding=utf8
# !/usr/bin/python


from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template, abort
import multiprocessing

import time
import longlive
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
            messag = ws.receive()
            print messag
            if messag == "stop":
                if ws in observersW:
                    ws.send("已停止")
                    W= list(reversed(observersW))
                    P = list(reversed(observersP))
                    print W
                    print P
                    ind = W.index(ws)
                    old = P[ind]
                    print old
                    old.terminate()
                else:
                    ws.send("还未开始")
            elif messag==None:
                print messag
            else:
                newSocket = WebSock(ws,messag)
                newSocket.start()
                observersW.append(ws)
                observersP.append(newSocket)
                print observersP
                print observersW


    return "Connected!"

class WebSock(multiprocessing.Process):

    def __init__(self, ws,messag):
        multiprocessing.Process.__init__(self)
        self.ws = ws
        self.messag = messag
    def run(self):
        time.sleep(1)
        if self.messag!=None:
            longlive.start(self.ws, self.messag)


if __name__ == '__main__':
    observersW = []
    observersP = []
    WP=[]
    http_server = WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()