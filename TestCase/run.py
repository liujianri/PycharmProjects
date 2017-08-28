#!/usr/bin/env python
# coding=utf-8
#!flask/bin/python
from app import app
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
http_server = WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
http_server.serve_forever()