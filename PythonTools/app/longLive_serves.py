#!/usr/bin/env python
# coding=utf-8
import multiprocessing
import sys
import time

from flask import request

import request_message
from app import app
from app.send_gurop_message import group_longLive
from app.send_single_message import send_singleMessage

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
observersW = []
observersP = []
WP=[]
serversW = []
serversP = []


@app.route('/longLive/')
def message():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        print "longLive"
        while True:
            messag = ws.receive()
            print messag
            if messag !=None:
                dict1 = messag.split(",",7)
                print dict1
                if dict1[0] == "request_message":
                    if dict1[1] == "stop":
                        print "request_message stop"
                    else:
                        print "request_message start..."
                        request_message.set_ws(ws)
                elif dict1[0]=="guorpmessage":
                    print "send guorpmessage"
                    if dict1[1] == "stop":
                        if ws in observersW:
                            ws.send("已停止")
                            W = list(reversed(observersW))
                            P = list(reversed(observersP))
                            ind = W.index(ws)
                            old = P[ind]
                            print "guorpmessage stop ws and process  "
                            old.terminate()
                        else:
                            ws.send("还未开始")
                    elif dict1[1] == "start":
                        newSocket = WebSock(ws, messag)
                        newSocket.start()
                        observersW.append(ws)
                        observersP.append(newSocket)
                        print observersP
                        print observersW
                    else:
                        print "页面错误"
                        ws.send("页面错误")
                elif dict1[0] =="single_message":
                    if dict1[1] == "stop":
                        if ws in serversW:
                            ws.send("已停止")
                            sW = list(reversed(serversW))
                            sP = list(reversed(serversP))
                            ind = sW.index(ws)
                            sold = sP[ind]
                            print "request_message stop"
                            sold.terminate()
                        else:
                            ws.send("还未开始")
                    elif dict1[1] == "start":

                        newSocketProcess = WebSockProcess(ws, messag)
                        newSocketProcess.start()
                        serversW.append(ws)
                        serversP.append(newSocketProcess)
                        print serversP
                        print serversW
                        print "single_message start"
                    else:
                        print "页面错误"
                        ws.send("页面错误")

            else:
                print messag

    return "Connected"

class WebSock(multiprocessing.Process):

    def __init__(self, ws,messag):
        multiprocessing.Process.__init__(self)
        self.ws = ws
        self.messag = messag
    def run(self):
        time.sleep(1)
        if self.messag!=None:
            print "new process : " + self.messag
            group_longLive.start(self.ws, self.messag)
class WebSockProcess(multiprocessing.Process):

    def __init__(self, ws,messag):
        multiprocessing.Process.__init__(self)
        self.ws = ws
        self.messag = messag
    def run(self):
        time.sleep(1)
        if self.messag!=None:
            print "new WebSockProcess : " + self.messag
            send_singleMessage.send_single_message(self.ws, self.messag)
            