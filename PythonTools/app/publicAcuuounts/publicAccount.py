# coding=utf8
# !/usr/bin/python
import json
import urllib2

from app.publicAcuuounts import all_url, post_data


def postHttp(url, postdata):

    request = urllib2.Request(url, data=postdata)
    response = urllib2.urlopen(request)
    return response.read()



def set_accounts_callback_url(callback_msg_url,callback_buy_url):  # 设置回调信息和购买的url
    data = post_data.callback_data(callback_msg_url, callback_buy_url)
    print postHttp(all_url.post_callback_url(), data)

def set_accounts_menu(menu1,menu_Click,menu2,menu_url,menu3,menu3_Click):  #设置菜单
    data = post_data.menu_data(menu1, menu_Click, menu2, menu_url, menu3, menu3_Click)
    print data
    print "set menu  "+postHttp(all_url.post_menu_url(), data)

def send_text_meassege(UserId,text_content):
    data = post_data.send_text_message_data(UserId, text_content)
    print postHttp(all_url.post_send_message_url(), data)

def get_url_info(userid):  #获取某个用户的信息
    postHttp(all_url.get_user_info_url(userid), "")

def buy():  #发起购买
    data = post_data.post_buy_data()
    postHttp(all_url.post_buy_url(), data)

def get_userid(Ids):
    url = "http://qtest.hellotalk.org/api/htm/convert?userid="+str(Ids)
    re=postHttp(url=url,postdata ="")
    d = json.loads(re)
    return d[str(Ids)]

def start_set(appid,secret,iftest,menu1,menu_Click,menu2,menu_url,menu3,menu3_Click,UserId,contexts):


    if iftest=="test":
        iftes = True
    else:
        iftes = False

    UsersId = get_userid(UserId)
    print UsersId

    all_url.Authentication(appid, secret, iftes) #鉴权 获取token
    #set_accounts_callback_url(callback_msg_url, callback_buy_url)
    set_accounts_menu(menu1,menu_Click,menu2,menu_url,menu3,menu3_Click)
    send_text_meassege(UsersId,contexts)
def just_send_message(appid, secret,UserId, contexts,iftest):

    if iftest=="test":
        iftes = True
    else:
        iftes = False

    UsersId = get_userid(UserId)
    print UsersId
    all_url.Authentication(appid, secret, iftes)
    # set_accounts_callback_url(callback_msg_url, callback_buy_url)
    send_text_meassege(UsersId, contexts)