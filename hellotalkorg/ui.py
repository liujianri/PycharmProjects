#!/usr/bin/env python
# coding=utf-8
import sys

import checkLogin
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow


class mywindow (QtWidgets.QWidget, Ui_MainWindow):
    def __init__ (self):
        super (mywindow, self).__init__ ()
        self.setupUi (self)
        self.pushButton.clicked.connect (self.f)
        

    def f(self):
        text = self.textEdit.toPlainText()
        self.ch(text, self.textEdit_2)

    def ch(self, text, g):
        if not text == '':
            if self.checkBox.isChecked():
                su = 0
            else:
                su = 1
            t = checkLogin.start(text,su)
            g.setText(t)
        else:
            g.setText('输入为空')

if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
    myshow = mywindow ()
    myshow.show ()
    sys.exit (app.exec_ ())
