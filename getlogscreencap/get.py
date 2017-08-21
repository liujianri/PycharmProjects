#!/usr/bin/env python
# coding=utf-8
import os
import time


def screenCap(logPath, ):
    if deviceOk():
        date = time.strftime("%Y%m%d%H%M%S", time.localtime())
        os.popen ('adb shell screencap -p ' + logPath + '/' + date + '.png')
        os.popen ('adb pull ' +logPath + '/' + date + '.png' + ' ' + os.getcwd())
        os.popen ('adb shell rm ' + logPath + '/' + date + '.png')
        return '完成'
    else:
        return '操作失败'
def getlog(logPath):
    if deviceOk():
        date = time.strftime("%Y%m%d%H%M%S", time.localtime())
        dirName = os.getcwd()+ '/' +date+ 'log'
        os.popen ('adb pull ' + logPath + ' ' + dirName)
        return '完成'
    else:
        return '操作失败'
def deviceOk():
    res = os.popen ("adb devices").read ().strip (' \n\r')
    array = res.split ('\n')
    return len (array) > 1
