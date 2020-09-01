#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 22:35
# @Author  : yuzhenyu
# @File    : base.py

import os
import time
from selenium import webdriver

from common.logs import Log
from common.read_config import Read_config

log=Log()

class Base_page:

    def __init__(self,driver):
        self.driver = driver

    def open_brower(self):
        brower=Read_config.read()
        try:
            if brower == "Chrome":
                self.driver=webdriver.Chrome()
                log.info("打开谷歌浏览器成功")
            else:
                log.error("浏览器配置有误")
            self.driver.get()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            return self.driver
        except Exception as e:
            log.error("打开浏览器报错",e)