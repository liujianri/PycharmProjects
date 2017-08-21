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
        print '提交bug'
        monkey_submit(content)

def monkey_submit(contents):
    url = 'http://120.25.239.138:18097/login/'
    buildNewBugUrl = 'http://120.25.239.138:18097/projects/ht_android/issues/new'
    submitBugUrl = 'http://120.25.239.138:18097/projects/ht_android/issues'
    username = 'maple'                   # 登录名
    password = 'maple1234'               # 登录秘密
    haveLog = 2                          # 1 表示上传截图  2 表示上传log和截图 3 表示只上传log  其他数字表示没有附件
    logPath = '/sdcard/hellotalk/htlog'  # log在手机中的地址
    title = 'monkey 自动化压力测试 Crash'                # bug 标题
    contents = contents             # bug 文字内容
    fixed_version = '2.3.0.202'         # 填入提交的版本号
    assigned_to = 'hzf'# 填入指派人 参数为：bean dengpeng hzf liling luochuan maple rocktest slw tujing xieqian zbq zhangpan
    prioritymun = 3 # 严重等级 1表示低  2 普通 3 高  4 紧急 5立刻
    category = 17  # 17表示概率问题，3 表示修改问题引入 4 表示新增需求引入 5 表示漏测 9表示用户反馈
    SubmitBug.start_submit_bug(url, buildNewBugUrl, submitBugUrl, username, password, haveLog, logPath, title, contents, fixed_version, assigned_to,prioritymun,category)

def submit():
    url = 'http://120.25.239.138:18097/login/'
    buildNewBugUrl = 'http://120.25.239.138:18097/projects/ht_android/issues/new'
    submitBugUrl = 'http://120.25.239.138:18097/projects/ht_android/issues'
    username = 'maple'                   # 登录名
    password = 'maple1234'               # 登录秘密
    haveLog = 1                          # 1 表示上传截图  2 表示上传log和截图 3 表示只上传log  其他数字表示没有附件
    logPath = '/sdcard/hellotalk/htlog'  # log在手机中的地址
    title = '评论回复@体不是蓝色'                # bug 标题
    contents = "我回复别人的@体不是蓝色，如图"             # bug 文字内容
    fixed_version = '2.3.0.202'         # 填入提交的版本号
    assigned_to = 'zbq'# 填入指派人 参数为：bean dengpeng hzf liling luochuan maple rocktest slw tujing xieqian zbq zhangpan
    prioritymun = 2 # 严重等级 1表示低  2 普通 3 高  4 紧急 5立刻
    category = 3  # 17表示概率问题，3 表示修改问题引入 4 表示新增需求引入 5 表示漏测 9表示用户反馈
    SubmitBug.start_submit_bug(url, buildNewBugUrl, submitBugUrl, username, password, haveLog, logPath, title, contents, fixed_version, assigned_to,prioritymun,category)

if __name__ == '__main__':
    monkey_start('10000')  # 开始测试 括号中输入monkey次数
    #submit() #普通提交bug monkey 时注释掉