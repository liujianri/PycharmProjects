#!/usr/bin/env python
# coding=utf-8
import sys
import os
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
import get

class mywindow (QtWidgets.QWidget, Ui_MainWindow):
    def __init__ (self):
        super (mywindow, self).__init__ ()
        self.setupUi (self)
        self.pushButton.clicked.connect (self.f)
        self.pushButton_2.clicked.connect (self.ch)
    def f(self):
        self.lab.setText(get.screenCap('/sdcard/'))
    def ch(self):
        self.lab.setText(get.getlog('/sdcard/hellotalk/htlog'))


if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
    myshow = mywindow ()
    myshow.show ()
    sys.exit (app.exec_ ())

