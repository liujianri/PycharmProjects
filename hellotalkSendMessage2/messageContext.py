#!/usr/bin/env python
# coding=utf-8
import hashlib
import json
import time

def text_message(ids,sender_ts,send_name,mes_context,room_id,room_name):

    t = time.time()
    server_ts = int(round(t * 1000))

    time_local = time.localtime(int(t))
    send_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)


    m2 = hashlib.md5()
    m2.update(mes_context+str(server_ts))
    msg_id=m2.hexdigest()

    d = {
                "id": int(ids),
                "typ": "muc",
                "cmd": 28745,
                "from": "me",
                "to": room_id,
                "status": 0,
                "data": {
                    "msg_id": msg_id,
                    "server_ts": int(server_ts),
                    "send_time": send_time,
                    "msg_type": "text",
                    "msg_model": "normal",
                    "room_id": room_id,
                    "room_name": room_name,
                    "sender_ts": int(sender_ts),
                    "sender_id": "me",
                    "sender_name": send_name,
                    "text": {
                        "text": mes_context
                    }
                }
    }

    mes= json.dumps(d)
    return mes
def voice_message(ids,sender_ts,send_name,room_id,room_name):

    t = time.time()
    server_ts = int(round(t * 1000))

    time_local = time.localtime(int(t))
    send_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)


    m2 = hashlib.md5()
    m2.update("zaijian jeih so"+str(server_ts))
    msg_id=m2.hexdigest()

    d = {
            "id": int(ids),
            "typ": "muc",
            "cmd": 28745,
            "from": "me",
            "to": room_id,
            "status": 0,
            "data": {
                "msg_id": msg_id,
                "server_ts": int(server_ts),
                "send_time": send_time,
                "msg_type": "voice",
                "msg_model": "normal",
                "room_id": room_id,
                "room_name": room_name,
                "sender_ts": int(sender_ts),
                "sender_id": "me",
                "sender_name": send_name,
                "voice": {
                    "url": "https://sh-ht.oss-cn-shanghai.aliyuncs.com/cvoc/20170803/0_10e46852552281c51fff4a7fcb0f2c38.mp3",
                    "size": 191007,
                    "type": "mp3",
                    "duration": 11
                }
            }
    }

    mes = json.dumps(d)

    return mes
def pic_message(ids,sender_ts,send_name,room_id,room_name):
    t = time.time()
    server_ts = int(round(t * 1000))

    time_local = time.localtime(int(t))
    send_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    m2 = hashlib.md5()
    m2.update("zaijian jeih so" + str(server_ts))
    msg_id = m2.hexdigest()

    d = {
    "id": int(ids),
    "typ": "muc",
    "cmd": 28745,
    "from": "me",
    "to": room_id,
    "status": 0,
    "data": {
        "msg_id": msg_id,
        "server_ts": int(server_ts),
        "send_time": send_time,
        "msg_type": "image",
        "msg_model": "normal",
        "room_id": room_id,
        "room_name": room_name,
        "sender_ts": int(sender_ts),
        "sender_id": "me",
        "sender_name": send_name,
        "image": {
            "url": "https://sz-ali-cdn-img.nihaotalk.com/cimg/20170803/0_38e7a27ace88a00101fd9b9da730580e.jpg",
            "name": "38e7a27ace88a00101fd9b9da730580e.jpg",
            "type": "jpg",
            "size": 1880287,
            "width": 1080,
            "height": 1920
        }
    }
}

    mes = json.dumps(d)

    return mes
def correction_message(ids,sender_ts,send_name,send_useid,room_id,room_name):
    t = time.time()
    server_ts = int(round(t * 1000))

    time_local = time.localtime(int(t))
    send_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    m2 = hashlib.md5()
    m2.update("zaijian jeih so" + str(server_ts))
    msg_id = m2.hexdigest()

    d = {
            "id": int(ids),
            "typ": "muc",
            "cmd": 28745,
            "from": "me",
            "to": room_id,
            "status": 0,
            "data": {
                "msg_id": msg_id,
                "server_ts": int(server_ts),
                "send_time": send_time,
                "msg_type": "correction",
                "msg_model": "normal",
                "room_id": room_id,
                "room_name": room_name,
                "sender_ts": int(sender_ts),
                "sender_id": "me",
                "sender_name": send_name,
                 "correction": {
                    "comment": "",
                    "userid": send_useid,
                    "body": [
                        {
                            "source": "自动填充改错消息",
                            "target": "改错消息自动填充"
                        }
                    ]
                }
            }
        }

    mes = json.dumps(d)

    return mes