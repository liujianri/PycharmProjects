#!/usr/bin/env python
# coding=utf-8
import SubmitBug
import monkeyRun


def monkey_start(testCount):
    cmd = 'adb shell monkey -p com.hellotalk -s 500 --kill-process-after-error --ignore-timeouts --monitor-native-crashes --throttle 500 -v -v '+testCount
    mo = monkeyRun.monkey(cmd, '/sdcard/hellotalk/htlog')
    co = mo.run()
    if not co == 0:
        content = ('共查找到 %s 处Crash' % co)
        submit(content)

def submit(contents):
    url = 'http://120.25.239.138:18097/login/'
    buildNewBugUrl = 'http://120.25.239.138:18097/projects/ht_android/issues/new'
    submitBugUrl = 'http://120.25.239.138:18097/projects/ht_android/issues'
    username = 'maple'                   # 登录名
    password = 'maple1234'               # 登录秘密
    haveLog = 2                          # 1 表示上传截图  2 表示上传log和截图 3 表示只上传log  其他数字表示没有附件
    logPath = '/sdcard/hellotalk/htlog'  # log在手机中的地址
    title = 'monkey 压力测试Crash'                # bug 标题
    contents = contents             # bug 文字内容
    fixed_version = '2.3.1.190'         # 填入提交的版本号
    assigned_to = 'maple'               # 填入指派人 参数为：bean dengpeng hzf liling luochuan maple rocktest slw tujing xieqian zbq zhangpan
    SubmitBug.start_submit_bug(url, buildNewBugUrl, submitBugUrl, username, password, haveLog, logPath, title, contents, fixed_version, assigned_to)

if __name__ == '__main__':
    monkey_start('100')  # 开始测试 括号中输入monkey次数