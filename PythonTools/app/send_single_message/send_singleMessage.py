#!/usr/bin/env python
# coding=utf-8


import time

from app.send_single_message import getSender

global too
global counts

def send_single_message(ws,messag):
    ws.send("正在发送。。。。")
    to=int(getSender.start(messag.split(",",5)[2])[0])
    counts =int(messag.split(",",5)[3])
    print to,counts
    im = 'http://sz-ht.img-cn-shenzhen.aliyuncs.com/cimg/20170726/3249443_e85831f2a0f2841889bf33d6c5e798fc.jpg'  #发的图片
    contents ='이것은 테스트 데이터 채우기,이것은 테스트 데이터 채우기 무시 주십시오!これはテストデータ充てん、見落としてください！，This is the test data fill，これはテストデータ充てん、見落としてください！，This is the test data fill，'   #发送的文字信息
    sounds = 'http://sz-ht.oss-cn-shenzhen.aliyuncs.com/cvoc/20170726/3249443_782648602d769015abc55f5c5089a7c5.hta'  #发送语音
    count = 0
    Sends = getSender.start('')  # 发送帐号
    # Sends = [3249528]
    Sends = list(set(Sends))  # 去重复
    while count < counts:

        for send in Sends:
            se = int(send)
            if se == to:
                continue
            getSender.http_posts(se, im, to, 2)
            count +=1
            ws.send(str(count))
            print count
            if count==counts:
                break
            time.sleep(1)
            getSender.http_posts(se, sounds, to, 3)
            count +=1
            ws.send(str(count))
            print count
            if count==counts:
                break
            time.sleep(1)
            getSender.http_posts(se, contents, to, 1)
            count +=1
            ws.send(str(count))
            print count
            if count==counts:
                break
            time.sleep(1)
    ws.send("发送完毕")