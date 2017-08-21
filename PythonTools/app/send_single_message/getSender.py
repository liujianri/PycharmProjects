#!/usr/bin/env python
# coding=utf-8
import json
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
def checkMessage(showuse):
    check_headers = {
        'Authorization': 'Basic aGVsbG90YWxrX3JlZG1pbmU6eWlrZUA0MTY=',
        'Host': '120.25.239.138:18097',
        'Host': 'station3.hellotalk.org',
        'Referer':'http://station3.hellotalk.org/htmall/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    url='http://ww2.hellotalk.com/htmall/userlist/index/?search_cmd=&showuser='+showuse+'&_=1490681610950'
    return send_post(url,'',check_headers).read()
def getImg(html):
    reg = r'<span class="USERID">(.+?)</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

def extract_string(results, Rules):
    Pattern = re.compile(Rules)
    arrary = Pattern.findall(results)
    if len(arrary)==0:
        return '未找到数据'
    else:
        return arrary[0]
def start(showuse):
    url = 'http://ww2.hellotalk.com/htmall/Public/checkLogin/'
    start_login(url)
    results = checkMessage(showuse)
    return getImg(results)
def http_posts(fro, message, to, num, ):
    url='http://qtest.hellotalk.org/sendmessage'
    if num ==1 :
        values={'from':fro,'to':[to],'message':{'type':'text','content':message,'push_type':'sound'}}
    elif num ==2 :
        values={'from':fro,'to':[to],'message':{'type':'image','url':message,'size':1024}}
    elif num == 3:
        values={'from':fro,'to':[to],'message':{'type':'voice','url':message,'size':14}}
    print "sending "
    print values
    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    urllib2.urlopen(req)         # 发送页面请求
                       # 获取服务器返回的页面信息