#!/usr/bin/env python
# coding=utf-8
import json
import sys

from flask import request, render_template

from app import app
from app.publicAcuuounts import publicAccount
from forms_login import appid_form

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages')
def message_s():
    return render_template('message.html')
@app.route('/guorpmessage')
def guorpmessage():
    return render_template('guorpmessage.html')

@app.route('/SingleMessage')
def SingleMessage():
    return render_template('SingleMessage.html')

@app.route('/sendmessage',methods = ['GET' , 'POST'])
def send_message():
    if request.method == "POST":
        data = request.get_data()
        print "sendmessage"+data
        dict1 = json.loads(data)
        print dict1
        publicAccount.just_send_message(dict1[0], dict1[1], dict1[2], dict1[3], dict1[4])
        return "successful"
    return  "Connected!"


@app.route('/meun',methods = ['GET' , 'POST'])
def set_meun():
    print "set meun"
    form = appid_form()
    if request.method == "POST" and form.validate_on_submit():
        appid = request.form.get("appid")
        secret = request.form.get("secret")
        iftest = request.form.get("radiobutton")
        menu1 = request.form.get("menu1")
        menu_Click = request.form.get("menu_Click")
        menu2 = request.form.get("menu2")
        menu_url = request.form.get("menu_url")
        menu3 = request.form.get("menu3")
        menu3_Click = request.form.get("menu3_Click")
        UserId = request.form.get("UserId")
        contexts = request.form.get("context")
        print appid
        print contexts
        publicAccount.start_set(appid, secret, iftest, menu1, menu_Click, menu2, menu_url, menu3, menu3_Click, UserId, contexts)
        return render_template('message.html')
    return render_template('meun.html',form=form)