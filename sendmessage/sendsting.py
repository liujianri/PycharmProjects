#!/usr/bin/env python
# coding=utf-8
import sys

import time

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

import send_http
import getSender
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
global too
global counts
class mywindow (QtWidgets.QWidget, Ui_MainWindow):
    def __init__ (self):
        super (mywindow, self).__init__ ()
        self.setupUi (self)
        self.pushButton.clicked.connect (self.f)
    def f(self):
        global too
        global counts
        counts = self.lineEdit.toPlainText()
        to = self.lineEdit_2.toPlainText()
        if counts=='' or to =='':
            self.label_3.setText('输入为空')
        else:
            too = int(getSender.start(to)[0])
            self.progressBar.setMaximum(int(counts))
            self.label_3.setText('正在发送')
            self.work =WorkThread()
            self.work.finishSignal.connect(self.setprogr)
            self.work.start()

    def setprogr(self,count):
        if count==self.get():
            self.label_3.setText('发送完毕')
        else:
            self.label_3.setText(str(count))
            self.progressBar.setValue(count)

    def set(self):
        return too
    def get(self):
        return int(counts)


class WorkThread(QThread):
    finishSignal = pyqtSignal(int)
    def __int__(self):
        super(WorkThread,self).__init__()

    def run(self):
        my= mywindow()
        to=my.set()
        counts =my.get()
        print to,counts
        im = 'http://sz-ht.img-cn-shenzhen.aliyuncs.com/cimg/20170726/3249443_e85831f2a0f2841889bf33d6c5e798fc.jpg'  #发的图片
        contents ='이것은 테스트 데이터 채우기,이것은 테스트 데이터 채우기 무시 주십시오!これはテストデータ充てん、見落としてください！，This is the test data fill，これはテストデータ充てん、見落としてください！，This is the test data fill，'   #发送的文字信息
        sounds = 'http://sz-ht.oss-cn-shenzhen.aliyuncs.com/cvoc/20170726/3249443_782648602d769015abc55f5c5089a7c5.hta'  #发送语音

        count = 0
        while count < counts:

            Sends = getSender.start('') #发送帐号
            #Sends = [3249528]
            Sends = list(set(Sends))  #去重复

            for send in Sends:
                se = int(send)
                if se == to:
                    continue
                send_http.http_post(se,im,to,2)
                count +=1
                self.finishSignal.emit(count)
                print count
                if count==counts:
                    break
                time.sleep(1)
                send_http.http_post(se,sounds,to,3)
                count +=1
                self.finishSignal.emit(count)
                print count
                if count==counts:
                    break
                time.sleep(1)
                send_http.http_post(se,contents,to,1)
                count +=1
                self.finishSignal.emit(count)
                print count
                if count==counts:
                    break
                time.sleep(1)




if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
    myshow = mywindow ()
    myshow.show ()
    sys.exit (app.exec_ ())