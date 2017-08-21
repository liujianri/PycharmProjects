#!/usr/bin/env python
# coding=utf-8
import hashlib
import json

import time

def callback_data(callback_msg_url,callback_buy_url):
    data = {
        "t": 1487923582016,
        "msg_url": callback_msg_url,
        "buy_url": callback_buy_url
    }
    return json.dumps(data)

def menu_data(menu1,menu_Click,menu2,menu_url,menu3,menu3_Click):
    data = {
        "button": [
            {
                "type": "click",
                "name": menu1,
                "key": menu_Click
            },
            {
                "name": menu2,
                "sub_button": [
                    {
                        "type": "view",
                        "name": "网址",
                        "url": menu_url
                    },
                    {
                        "type": "click",
                        "name": menu3,
                        "key": menu3_Click
                    }
                ]
            }
        ]
    }
    return json.dumps(data)

def send_text_message_data(UserId,text_content):
    t = time.time()
    server_ts = int(round(t * 1000))

    time_local = time.localtime(int(t))
    send_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    m2 = hashlib.md5()
    m2.update( str(server_ts))
    msg_id = m2.hexdigest()
    print "data_"+UserId
    data = {
        "t":server_ts,
        "toid":UserId ,
        "msg":{
            "from_nickname": "maple",
            #optional 默认是公众号名称，如果from_nickname 有值，则展示改名称
            "head_url ":"http://ht-head.oss-cn-shenzhen.aliyuncs.com/cs_logo.jpg",
            #optional 字段，如果有该字段，那么这条消息展示新的头像
            #上面两个字段是为了展示老师名称设置的
            "msg_id": msg_id, #消息的唯一标示符
            "msg_type": "text",
            "send_time": send_time,
            "text": {
                "text": text_content,
            }
        }
    }
    return json.dumps(data)

def post_buy_data():

    data= {
            "t":1487923582016,
            "userid":"72XKzJDRVTVD" , #发起购买的用户id
            "data":{
                "subject" : "com.hellotalk.yoli_english", #subject 描述，
                "total_fee" : 198, #产品价格，RMB ，可以自定义
                "product_name" : "native English teach", #产品名字，支付时候产品名字
            }
    }

    return json.dumps(data)