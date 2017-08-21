#!/usr/bin/env python
# coding=utf-8
import unittest
from appium import webdriver
import os
import time

class logInTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['app'] = os.path.abspath('/Users/liu/Desktop/iso/hellotalk/HelloTalk_Binary.app')

        self.wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(30)
    def tearDown(self):
        self.wd.quit()

    def test_login(self):
        flag = self.isElementExist("OK")
        if flag:
            self.wd.find_element_by_accessibility_id("OK").click()
        self.wd.find_element_by_accessibility_id("Already have an account? Log In").click()
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("test1001@ttt.com")
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys("test1001")
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[7]/UIAButton[1]").click()
        time.sleep(10)
        self.wd.find_element_by_accessibility_id("OK").click()
        self.wd.find_element_by_accessibility_id("")
    def isElementExist(self,param):
        try:
            self.wd.find_element_by_accessibility_id(param)
            return True
        except:
            return False
if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(logInTestCase("test_login"))
        # 执行测试
        runner = unittest.TextTestRunner()
        runner.run(suite)
