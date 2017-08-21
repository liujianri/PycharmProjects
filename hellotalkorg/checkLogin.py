#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import cookielib
import re


cookie = cookielib.MozillaCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

def send_post(url, data, send_headers):
    post_data = urllib.urlencode(data)
    # 提交，发送数据
    req = urllib2.Request(url, data=post_data, headers=send_headers)
    # 获取提交后返回的信息
    content = opener.open(req)
    return content

def start_login(url):
    login_data = {
        'account': 'maple',
        'password': 'maple1234',
        'opentab': '',
        'lang_type': 'zh'
    }

    login_headers = {
        'Authorization': 'Basic aGVsbG90YWxrX3JlZG1pbmU6eWlrZUA0MTY=',
        'Host': 'station3.hellotalk.org',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Origin':'http://station3.hellotalk.org',
        'Referer':'http://station3.hellotalk.org/htmall/Public/login/',
        'Content-Length':'54'
    }
    send_post(url, login_data, login_headers)
def checkMessage(showuser,urls):
    check_headers = {
        'Authorization': 'Basic aGVsbG90YWxrX3JlZG1pbmU6eWlrZUA0MTY=',
        'Host': '120.25.239.138:18097',
        'Host': 'station3.hellotalk.org',
        'Referer':'http://station3.hellotalk.org/htmall/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    url='http://'+urls+'/htmall/userlist/index/?search_cmd=&showuser='+showuser+'&_=1490600332144'
    return send_post(url,'',check_headers).read()
def getUserID(results):
    rule = 'class="USERID">(.*?)</span>'
    return extract_string(results,rule)

def getEmail(results):
    rule = 'class="EMAIL">(.*?)</span>'
    return extract_string(results,rule)
def getID(results):
    rule = 'class="USERNAME">(.*?)</span>'
    return extract_string(results,rule)
def getNickName(results):
    rule = 'class="NICKNAME">(.*?)</span>'
    return extract_string(results,rule)

def extract_string(results, Rules):
    Pattern = re.compile(Rules)
    arrary = Pattern.findall(results)
    if len(arrary)==0:
        return '未找到数据'
    else:
        return arrary[0]
def start(user,test):
    if test == 1:
        urls = 'ww2.hellotalk.com'
    else:
        urls = 'station3.hellotalk.org'
    url = 'http://'+urls+'/htmall/Public/checkLogin/'
    start_login(url)
    results = checkMessage(user,urls)
    return 'JID：'+getUserID(results)+'\n'+'ID：'+getID(results)+'\n'+'邮箱：'+getEmail(results)+'\n'+'呢称：'+getNickName(results)
