#!/usr/bin/env python
# coding=utf-8
import os
import getLogFile
import shutil


class monkey:
    def __init__(self, cmd, logPath):
        self.cmd = cmd
        self.logPath = logPath

    def run(self):
        if getLogFile.deviceOk():
            print "monkey 运行中，请勿断开手机连接！！"
            mon = os.popen(self.cmd)
            mone = self.check_monkey(mon)
            if mone == 1:
                dr = os.getcwd()+'/'
                getLogFile.command('adb pull ' + self.logPath + ' ' + dr)
                count = getLogFile.fil(dr+'htlog/', 0)
                shutil.rmtree(dr+'htlog')
                print 'monkey 执行完毕，共 %s 处 crash' %count
                print count
                return count
            else:
                print 'monkey 运行失败'
                return 0
        else:
            print "未连接手机，执行测试失败"
            return 0
    def check_monkey(self, mon):
        array = mon.read().strip (' \n\r')
        arr = array.split ('\n')
        if arr[6] == '** No activities found to run, monkey aborted.':
            print arr[6]
            return 0
        else:
            return 1