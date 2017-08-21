#!/usr/bin/env python
# coding=utf-8
import os
import re


class filters_log:
    def __init__ (self, dirs, errfilepath, wirt):
        self.dirs = dirs  # log所在的文件夹路径
        self.errfilepath = errfilepath  # 存放log错误报告文件的文件夹路径
        self.wirt = wirt  # 是否要写错误报告

    def get_log_path (self):
        cuns = 0
        for root, dirs, files in os.walk (self.dirs):
            for name in files:
                filesPath = os.path.join (root, name)
                print name
                cun = self.read_log(filesPath)
                cuns += cun
        self.writ_errfile ('共查找到 %s 处' % cuns)
        print cuns
        return cuns

    def read_log(self, p):
        NullPointer = "Exception"

        count = 0
        f = open(p, 'r')
        lines = f.readlines ()
        for line in lines:

            if re.findall(NullPointer, line):
                l = lines.index(line)
                dd = lines [l]
                print dd
                d = os.path.basename (p) + "   " + str (lines.index (line))
                self.writ_errfile (d + "   " + dd)
                count += 1
                print str(count)+'-----------'
                print dd
                for i in range(10000):
                    h = lines[l + i+1]
                    zzz = r'(([0-9]{2}):){2}([0-9]{2})'
                    Pattern = re.compile(zzz)
                    arrary = Pattern.findall(h)
                    if len(arrary) <= 0:
                        print h
                        self.writ_errfile('                  '+h)
                    else:
                        break
        f.close()
        return count

    def writ_errfile(self, string):
        if self.wirt == 1:
            wir = 0
            errfile = "%serror.log" % (self.errfilepath)
            if not os.path.exists(errfile):
                wir = 1
            fr = open (errfile, 'a')
            if wir == 1:
                fr.write ("logName  line  message")
                fr.write ('\n')
            fr.write(string)

            fr.close()
