#!/usr/bin/env
#coding:utf-8

import urllib2
import json
import getSender
import time

def http_post(fro,message,to,num):
    url='http://qtest.hellotalk.org/sendmessage'
    if num ==1 :
        values={'from':fro,'to':[to],'message':{'type':'text','content':message,'push_type':'sound'}}
    elif num ==2 :
        values={'from':fro,'to':[to],'message':{'type':'image','url':message,'size':1024}}
    elif num == 3:
        values={'from':fro,'to':[to],'message':{'type':'voice','url':message,'size':14}}

    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    urllib2.urlopen(req)         # 发送页面请求
                       # 获取服务器返回的页面信息
