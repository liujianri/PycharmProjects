
# coding=utf8
# !/usr/bin/python
import json
import urllib2
import urllib




def postHttp(url, postdata):

    request = urllib2.Request(url, data=postdata)
    response = urllib2.urlopen(request)
    return response.read()


def menu_data():
    data = {
        "button": [
            {
                "type": "cl",
                "name": "今",
                "key": "V1001_TODAY_MUSIC"
            },
            {
                "name": "菜单",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "搜索",
                        "url": "http://www.baidu.com/"
                    },
                    {
                        "type": "click",
                        "name": "赞一下我们",
                        "key": "V1001_GOOD"
                    }
                ]
            }
        ]
    }
    return json.dumps(data)


print postHttp("http://0.0.0.0:5002/data",menu_data())

