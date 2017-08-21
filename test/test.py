#!/usr/bin/env python
# coding=utf-8
import sys
import os
from PyQt5 import QtWidgets
from first import Ui_MainWindow


class mywindow (QtWidgets.QWidget, Ui_MainWindow):
    def __init__ (self):
        super (mywindow, self).__init__ ()
        self.setupUi (self)
        self.btn.clicked.connect (self.f)

    def f(self):
        text = self.textEdit.toPlainText()
        self.ch(text, self.textEdit_2)

    def ch(self, text, g):
        if not text == '':
            os.popen ('adb shell monkey -p com.hellotalk -s 500 10')
            g.setText(text)

        else:
            g.setText('输入为空')

if __name__ == "__main__":


    app = QtWidgets.QApplication (sys.argv)
    myshow = mywindow ()
    myshow.show ()
    sys.exit (app.exec_ ())

