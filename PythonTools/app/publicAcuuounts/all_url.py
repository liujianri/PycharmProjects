#!/usr/bin/env python
# coding=utf-8
import urllib2

import time


def Authentication(appid,secret,iftest):

    if iftest:
        t_url = "http://qtest.hellotalk.org"
        set_head_url(t_url)
    else:
        t_url = "https://web.hellotalk.com"
        set_head_url(t_url)

    url = get_head_url() + "/api/htm/token?appid="+appid+"&secret="+secret
    print url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request).read()
    re = response.split(",",3)
    status = re[0].split(":",2)[1]
    print "response"+response
    if int(status) ==0:
        tokens = re[1].split(":",2)[1]
        setToken(eval(tokens))
        print "ton  "+tokens
        return True
    else:
        print "鉴权失败"
        return False


def set_head_url(u):
    global head_url
    head_url = u
def get_head_url():
    return head_url

def setToken(tokens):
    global token
    token = tokens

def getToken():
    return token

def post_callback_url():
    url = get_head_url()+"/api/htm/set_callback?access_token="+getToken()
    print "post_callback_url  "+url
    return url

def post_menu_url():
    url = get_head_url()+"/api/htm/menu?access_token="+getToken()
    print "post_menu_url  " + url
    return url
def post_send_message_url():
    url = get_head_url() + "/api/htm/message?access_token=" + getToken()
    print "send_message_url   " +url
    return url
def get_user_info_url(userid,):
    url = get_head_url() + "/api/htm/user_info?access_token="+getToken()+"&userid="+userid+"&lang=zh_CN"
    print "get_user_info_url   " + url
    return url
def post_buy_url():
    url = get_head_url() + "/api/htm/buy?access_token=" + getToken()
    print "post_buy_url   " + url
    return url

