#!/usr/bin/env
# coding:utf-8
import urllib
import urllib2
import json
import re
import time



def http_post(fro, message, to, num):
    url = 'http://qtest.hellotalk.org/sendmessage'
    if num == 1:
        values = {'from': fro, 'to': [to], 'message': {'type': 'text', 'content': message, 'push_type': 'sound'}}
    elif num == 2:
        values = {'from': fro, 'to': [to], 'message': {'type': 'image', 'url': message, 'size': 1024}}
    elif num == 3:
        values = {'from': fro, 'to': [to], 'message': {'type': 'voice', 'url': message, 'size': 14}}

    jdata = json.dumps(values)  # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)  # 生成页面请求的完整数据
    print values
    response = urllib2.urlopen(req)  # 发送页面请求
    return response.read()  # 获取服务器返回的页面信息


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'<span class="USERID">(.+?)</span>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


def mains():
    nm = 0
    # 接收帐号
    im = 'http://sz-ht.oss-cn-shenzhen.aliyuncs.com/cimg/20161116/3249418_5135361a535f644c2eb4a2412a3fbce0.jpg'  # 发的图片
    contents = ['你好呀', '这是测试数据填充', 'これはテストデータ充てん、見落としてください！，This is the test data fill，',
                '이것은 테스트 데이터 채우기,이것은 테스트 데이터 채우기 무시 주십시오!これはテストデータ充てん、見落としてください！，This is the test data fill，これはテストデータ充てん、見落としてください！，This is the test data fill，']  # 发送的文字信息
    sounds = 'http://sg-ht.oss-ap-southeast-1.aliyuncs.com/cvoc/161116/5043903_927465AD42C84D01EB7129257BC8E419.hta'  # 发送语音

    global count
    count=0
    set(count)
    while (count < counts):
        print counts
        resps = http_post(3249528, im, to, 2)
        respsd = http_post(3249528, sounds, to, 3)
        # resp = http_post(se,cont,to,1)
        time.sleep(1)
        count = count + 2
        set(count)
        print '==================='
        print count
    print '      发送完毕'


def sets(useid, co):
    global to, counts
    to = int(useid)
    counts=int(co)
def get():
    global coun
    return str(coun)
def set(c):
    global coun
    coun = c