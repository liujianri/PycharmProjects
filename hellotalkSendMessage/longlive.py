#!/usr/bin/env python
# coding=utf-8
import threading
import urllib2

import websocket
import thread
import time
import login
import json
import messageContext

y = 1
def on_message(ws, message):

    global y
    if y ==1 :
        s = json.loads(message)
        global profile_ts, NK,ids,room_id,room_name,test_group_list,group_list

        profile_ts = s['data']['profile_ts']
        ids = s["id"]
        NK = s["data"]["Config"]["my_info"]["NK"]
        if NK=="":
            NK = s["data"]["my_info"]["UN"]

        y=0
    else:
        print "发送成功，返回数据如下："
        print message


def on_error(ws, error):
    print(error)

def on_close(ws):
    print "发送完成。。。。。。。。。。。。。"
    print("### closed ###")

def on_open(ws):
    setws(ws)
    def run(*args):
        time.sleep(1)
        print("thread terminating...")
        idss=ids
        i = 1
        conts=cont+1
        while i<conts:
            for l in test_group_list:
                print test_group_list
                room_id = l[0]
                room_name = l[1]
                mes = messageContext.text_message(idss,profile_ts,NK,"python 自动填充群组消息"+str(i),room_id,room_name)
                ws.send(mes)
                idss +=1
                i+=1
                websoctSend(i)
                print i
                if i==conts:
                    break
                time.sleep(0.3)
                voice = messageContext.voice_message(idss,profile_ts,NK,room_id,room_name)
                ws.send(voice)
                idss+=1
                i += 1
                websoctSend(i)
                print i
                if i == conts:
                    break
                time.sleep(0.3)
                pic = messageContext.pic_message(idss, profile_ts, NK, room_id,room_name)
                ws.send(pic)
                idss += 1
                i += 1
                websoctSend(i)
                print i
                if i == conts:
                    break
                time.sleep(0.3)
                correction = messageContext.correction_message(idss,profile_ts, NK,send_useid, room_id,room_name)
                ws.send(correction)
                idss += 1
                i += 1
                websoctSend(i)
                print i
                if i == conts:
                    break
                time.sleep(1)
        time.sleep(2)
        ws.close()
    thread.start_new_thread(run, ())


def start(websoct,information):
    websocket.enableTrace(True)
    setwebws(websoct)
    if information != 0:

        global send_useid, test_group_list, group_list, cont
        informations=information.split(",", 5)
        test_group_list = [[get_userid(informations[3]), informations[4]]]

        if informations[0]=="test":
            iftest = True
            #test_group_list = [["12EznJVUzIDD", "测试群"], ["09XETRVjNDzD", "500测试大群"], ["49IaAMJGJKyD", "测试群"],]  # 测试服务器的群
            #test_group_list = [["65OzTTxKuxJN", ""]]
        else:
            iftest=False
            #test_group_list = [["42WbrNPVN1xD", "测试群"]]
            #test_group_list = [["01LuIRHbuKnD", "test"]]

        send_useid = int(informations[1])
        cont = int(informations[2])
        url = login.getToken(send_useid, iftest) #True 测试服务器  False 正式服务器
        print url
        ws = websocket.WebSocketApp(url,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()
    else:
        stopSend()


def get_userid(Ids):
    url = "http://qtest.hellotalk.org/api/htm/convert?userid="+str(Ids)
    request = urllib2.Request(url, "")
    response = urllib2.urlopen(request)
    re=response.read()
    d = json.loads(re)
    return d[str(Ids)]


def stopSend():
    messWs.close()
    webws.send("已停止。。。")

def websoctSend(co):
    if cont == co-1:
        webws.send("已发送完毕")
    else:
        webws.send("已发送 "+str(co-1)+" 条")

def setwebws(webwss):
    global webws
    webws = webwss

def setws(messageWs):
    global messWs
    messWs = messageWs
