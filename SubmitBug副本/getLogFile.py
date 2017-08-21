#!/usr/bin/env python
# coding=utf-8
import os
import zipfile
import shutil
import time
import filtersLog


def zip_dir(dirname, zipfilename):
    """
    | ##@函数目的: 压缩指定目录为zip文件
    | ##@参数说明：dirname为指定的目录，zipfilename为压缩后的zip文件路径
    | ##@返回值：无
    | ##@函数逻辑：
    """
    filelist = []
    if os.path.isfile (dirname):
        filelist.append (dirname)
    else:
        for root, dirs, files in os.walk (dirname):
            for name in files:
                filelist.append (os.path.join (root, name))

    zf = zipfile.ZipFile (zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar [len (dirname):]
        # print arcname
        zf.write (tar, arcname)
    zf.close()

def get_log(logPath, us):

    dirName = os.getcwd()+'/bugLog'

    if not os.path.exists(dirName):
        os.mkdir ('bugLog')
    date = time.strftime("%Y%m%d%H%M%S", time.localtime())
    newLog = dirName+'/'+date+'htlog'

    if deviceOk():
        if us == 2:
            command ('adb shell screencap -p ' + logPath + '/' + date + '.png')

        command ('adb pull ' + logPath + ' ' + newLog)
        fil(newLog, 1)

        if us == 2:
            command ('adb shell rm ' + logPath + '/' + date + '.png')
        zip_dir (newLog, newLog + '.zip')
        shutil.rmtree(newLog)
        return newLog + '.zip'
    else:
        print '连接失败'


def command(commands):
    os.popen(commands)

def deviceOk():
    res = os.popen ("adb devices").read ().strip (' \n\r')
    array = res.split ('\n')
    return len (array) > 1

def fil(dir, wirt):
    b = 0
    for root, dirs, files in os.walk (dir):
        for name in dirs:
            dirPath = os.path.join (root, name)
            fi = filtersLog.filters_log(dirPath, dirPath, wirt)
            a = fi.get_log_path()
            b += a
    return b