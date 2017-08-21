#!/usr/bin/env python
# coding=utf-8
import websocket
import thread
import time
import login
import json
import messageContext


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
        #room_id= "09XETRVjNDzD"      #正式服务器 测试群ID "42WbrNPVN1xD"
        #room_name = "500测试大群"   #测试服务器 500测试大群ID ：09XETRVjNDzD  测试群2 ID：49IaAMJGJKyD  测试群 ID："12EznJVUzIDD"
        test_group_list = [["12EznJVUzIDD","测试群"],["09XETRVjNDzD","500测试大群"],["49IaAMJGJKyD","测试群"]]  #测试服务器的群
        #test_group_list = [["09XETRVjNDzD", "500测试大群"]]
        group_list=[["42WbrNPVN1xD","测试群"]]
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
    def run(*args):
        time.sleep(1)
        print("thread terminating...")
        idss=ids
        i = 1
        cont = 1000
        conts=cont+1
        while i<conts:
            for l in test_group_list:
                room_id = l[0]
                room_name = l[1]
                mes = messageContext.text_message(idss,profile_ts,NK,"python 自动填充群组消息"+str(i),room_id,room_name)
                ws.send(mes)
                idss +=1
                i+=1
                print i
                if i==conts:
                    break
                time.sleep(0.2)
                voice = messageContext.voice_message(idss,profile_ts,NK,room_id,room_name)
                ws.send(voice)
                idss+=1
                i += 1
                print i
                if i == conts:
                    break
                time.sleep(0.3)
                pic = messageContext.pic_message(idss, profile_ts, NK, room_id,room_name)
                ws.send(pic)
                idss += 1
                i += 1
                print i
                if i == conts:
                    break
                time.sleep(0.3)
                correction = messageContext.correction_message(idss,profile_ts, NK,send_useid, room_id,room_name)
                ws.send(correction)
                idss += 1
                i += 1
                print i
                if i == conts:
                    break
                time.sleep(1)
        time.sleep(2)
        ws.close()
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    y = 1
    global send_useid
    send_useid = 3249443
    url = login.getToken(send_useid, True) #True 测试服务器  False 正式服务器
    print url
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

