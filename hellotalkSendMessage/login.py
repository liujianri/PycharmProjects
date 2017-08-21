#!/usr/bin/env python
# coding=utf-8

import urllib2
import httplib


def getToken(userid,test):

    if test:
        t_url = "http://qtest.hellotalk.org"
        t_wss= "wss://qtest.hellotalk.org/im/"
        host = "qtest.hellotalk.org"
    else:
        t_url = "https://web.hellotalk.com"
        t_wss = "wss://web.hellotalk.com/im/"
        host = 'web.hellotalk.com'

    url = t_url+"/im/qrToken"
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    r=res.split(",",4)
    token = r[1].split(":",1)[1]
    u = t_url+"/im/qr/d/"+eval(token)+"?userid="+str(userid)
    print u,token,

    headers = {"X-HT-Service": "ht-qr-scan"}
    conn = httplib.HTTPSConnection(host)
    t = conn.request(method='GET', url=u, headers=headers)
    print t
    return t_wss+eval(token)
