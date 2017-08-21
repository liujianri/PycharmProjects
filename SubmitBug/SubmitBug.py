#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib
import cookielib
import re
import os
import getLogFile
import time
import shutil


cookie = cookielib.MozillaCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
global CSRF_Token
global assigned_to_id
global fixed_version_id
global priority_id
global category_id

# 登录前获取token的header
getToken_header = {
    'Authorization': 'Basic aGVsbG90YWxrX3JlZG1pbmU6eWlrZUA0MTY=',
    'Host': '120.25.239.138:18097',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
}


# 开始登录
def start_login(login_token, url, username, password):
    login_data = {
        'utf8': '✓',
        'authenticity_token': login_token,
        'back_url': 'http://120.25.239.138:18097/',
        'username': username,
        'password': password,
        'login': '登录 »'
    }

    login_headers = {
        'Authorization': 'Basic aGVsbG90YWxrX3JlZG1pbmU6eWlrZUA0MTY=',
        'Host': '120.25.239.138:18097',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }
    send_post(url, login_data, login_headers)


def submit_bug(submitBugToken, url, attachments1Token, filename, title, contents, date):
    submitBug_data = {
        'utf8': '✓',
        'authenticity_token': submitBugToken,
        'issue[tracker_id]': '1',
        'issue[subject]': title,
        'issue[description]': contents,
        'issue[status_id]': '1',
        'was_default_status': '1',
        'issue[priority_id]': priority_id,
        'issue[assigned_to_id]': assigned_to_id,
        'issue[category_id]': category_id,
        'issue[fixed_version_id]': fixed_version_id,
        'issue[parent_issue_id]': '',
        'issue[start_date]': date,
        'issue[due_date]': '',
        'issue[estimated_hours]': '',
        'attachments[1][filename]': filename,
        'attachments[1][description]': '',
        'attachments[1][token]': attachments1Token,
        'attachments[dummy][file]': ('', '', 'application/octet-stream'),
        'commit': '创建'
    }
    submitBug_headers = {
        'Authorization': 'Basic aGVsbG90YWxrX3JlZG1pbmU6eWlrZUA0MTY=',
        'Host': '120.25.239.138:18097',
        'Content-Type': 'multipart/form-data',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }
    res = send_post(url, submitBug_data, submitBug_headers)
    bugid = extract_string (res.read (), '<h2>Bug #(.*?)</h2>')
    print '提交成功id:', bugid


# 上传附件并且得到附件的attachments token
def upload_attachments(ids, filename, typ, FilePath):

    fil = open(FilePath, "rb")
    FileData = fil.read()
    length = str(os.path.getsize(FilePath))
    print length

    attac_headers = {
        'Authorization': 'Basic aGVsbG90YWxrX3JlZG1pbmU6eWlrZUA0MTY=',
        'Host': '120.25.239.138:18097',
        'Content-Type': 'application/octet-stream',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': ':application/js',
        'X-CSRF-Token': CSRF_Token,
        'Connection': 'keep-alive',
        'Content-Length': length
    }
    UploadUrl = 'http://120.25.239.138:18097/uploads.js?attachment_id=' + ids + '&filename=' + filename + '&content_type=' + typ
    request = urllib2.Request(UploadUrl, data = FileData, headers = attac_headers)
    con = opener.open(request).read()
    Rule = r'.val\(\'(.*?)\'\)'
    tt = extract_string(con, Rule)
    print tt
    fil.close()
    return tt


# 获取token
def get_token(url, header, fixed_version, assigned_to):
    resq = urllib2.Request(url, headers=header)
    result = opener.open(resq).read()
    tokenRule = '<input type="hidden" name="authenticity_token" value="(.*?)"'  # 登录参数里面有一个token参数，是加载到页面中并且是动态的，需要爬出来
    if url == 'http://120.25.239.138:18097/projects/ht_android/issues/new':  # 判断如果是新建bug页面,同时获取下X-CSRF-Token 用于上传文件
        global CSRF_Token
        global assigned_to_id
        global fixed_version_id
        csrftoken = '<meta name="csrf-token" content="(.*?)" />'
        CSRF_Token = extract_string(result, csrftoken)
        assigned_to_id = extract_string(result, r"<option value=\"([0-9]{2})\">"+assigned_to+"</option>")
        print "assigned_to", assigned_to_id
        fixed_version_id = extract_string(result, '<option value="(.*?)">'+fixed_version+'</option>')
        print "the CSRF_Token is: ", CSRF_Token
    access_token = extract_string(result, tokenRule)
    print "the token is: ", access_token
    return access_token


def extract_string(results, Rules):
    Pattern = re.compile(Rules)
    arrary = Pattern.findall(results)
    return arrary[0]


def send_post(url, data, send_headers):
    post_data = urllib.urlencode(data)
    # 提交，发送数据
    req = urllib2.Request(url, data=post_data, headers=send_headers)
    # 获取提交后返回的信息
    content = opener.open(req)
    return content


def start_submit_bug(url, buildNewBugUrl, submitBugUrl, username, password, haveLog, logPath, title, contents, fixed_version, assigned_to,prioritymun,category):
    """
        | ##@参数说明：dirname为手机端log目录,haveLog = 1 表示有log，此时必现传文件路径进来。
            当haveLog ！= 1 时 表示没有log ，此时文件路径传个空值即可
            title bug标题 contents bug文字内容
        """
    token = get_token(url, getToken_header, fixed_version, assigned_to)
    start_login(token, url, username, password)  # 登录
    submitBugToken = get_token(buildNewBugUrl, getToken_header, fixed_version, assigned_to)  # 获取提交bug的令牌
    date = time.strftime('%Y-%m-%d', time.localtime(time.time())) # 获取当前时间
    global priority_id
    global category_id
    priority_id = prioritymun
    category_id = category
    print contents


    if haveLog == 2:
        if getLogFile.deviceOk():
            logZipPath = getLogFile.get_log (logPath, 2)
            if os.path.exists (logZipPath):
                filename = os.path.basename (logZipPath)  # 获取文件名
                ids = '1'
                attachments1Token = upload_attachments(ids, filename, 'zip', logZipPath)  # 上传log
                submit_bug (submitBugToken, submitBugUrl, attachments1Token, filename, title, contents, date)
            else:
                print '获取log压缩文件失败'
        else:
            print '未连接手机，获取log失败，不能提交bug'
    elif haveLog == 1:
        if getLogFile.deviceOk():
            getLogFile.command ('adb shell screencap -p ' + logPath + '/' + date + '.png')
            getLogFile.command ('adb pull ' + logPath + '/' + date + '.png' + ' ' + os.getcwd())
            getLogFile.command ('adb shell rm ' + logPath + '/' + date + '.png')
            screenshotPath = os.getcwd() + '/' + date + '.png'
            if os.path.exists(screenshotPath):
                filename = os.path.basename(screenshotPath)
                attachments1Token = upload_attachments ('1', filename, 'png', screenshotPath)  # 上传截图
                os.remove(screenshotPath)
                submit_bug (submitBugToken, submitBugUrl, attachments1Token, filename, title, contents, date)
        else:
            print '连接手机失败'
    elif haveLog == 3:
        if getLogFile.deviceOk():
            logZipPath = getLogFile.get_log (logPath, 3)
            if os.path.exists (logZipPath):
                filename = os.path.basename (logZipPath)  # 获取文件名
                ids = '1'
                attachments1Token = upload_attachments(ids, filename, 'zip', logZipPath)  # 上传log
                submit_bug (submitBugToken, submitBugUrl, attachments1Token, filename, title, contents, date)
            else:
                print '获取log压缩文件失败'
        else:
            print '未连接手机，获取log失败，不能提交bug'
    else:
        submit_bug (submitBugToken, submitBugUrl, '', '', title, contents, date)