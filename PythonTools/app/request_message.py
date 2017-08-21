#!/usr/bin/env python
# coding=utf-8
from flask import  request, render_template, abort
from geventwebsocket import WebSocketError

from app import app

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


@app.route('/data',methods = ['GET' , 'POST'])
def get_data():
    if request.method == "POST":
        data = request.get_data()
        print data
        send_message(data)
        return "successful"
    return  "Connected!"


def set_ws(w):
    global ws
    ws = w

def close_ws(w):
    ws.close()

def send_message(data):
    print "send_message : "+data
    try:
        try:
            ws.send(data)
        except NameError,e:
            print "'ws' is not defined"
    except WebSocketError:
        print "'ws' is close"
