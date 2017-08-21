#!/usr/bin/env python
# coding=utf-8
import os
import re


class filters_log:
    def __init__ (self, dirs, errfilepath, wirt):
        self.dirs = dirs
        self.errfilepath = errfilepath
        self.wirt = wirt

    def get_log_path (self):
        cuns = 0
        for root, dirs, files in os.walk (self.dirs):
            for name in files:
                filesPath = os.path.join (root, name)
                cun = self.read_log(filesPath)
                cuns += cun
        self.writ_errfile ('共查找到 %s 处' % cuns)
        print cuns
        return cuns

    def read_log(self, p):
        NullPointer = "java.lang.NullPointerException"
        IllegalState = "java.lang.IllegalStateException"
        IllegalArgument = "java.lang.IllegalArgumentException"
        ArrayIndexOutOfBounds = "java.lang.ArrayIndexOutOfBoundsException"
        RuntimeException = "java.lang.RuntimeException"
        SecurityException = "java.lang.SecurityException"

        count = 0
        f = open(p, 'r')
        lines = f.readlines ()
        for line in lines:
            if (re.findall (NullPointer, line) or re.findall (IllegalState, line) or re.findall (IllegalArgument,
                                                                                                 line) or re.findall (
                ArrayIndexOutOfBounds, line) or re.findall (RuntimeException, line) or re.findall (SecurityException,
                                                                                                   line)):
                dd = lines[lines.index(line)]
                d = os.path.basename(p)+"   "+str(lines.index(line))
                self.writ_errfile(d+"   "+dd)
                count += 1
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
            fr.write('\n')
            fr.close()