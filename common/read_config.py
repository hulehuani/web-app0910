#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 22:09
# @Author  : yuzhenyu
# @File    : read_config.py

import configparser
import os

from common.logs import Log


log=Log()

class Read_config:
    """
    读取配置文件section，以一个列表的形式返回出去。
    """
    def __init__(self):
        config_name=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_filename=os.path.join(config_name,"config\config.ini")

    @staticmethod
    def read(self):
        try:
            cf=configparser.ConfigParser()
            cf.read(self.config_filename)
            log.info("读取配置文件成功")
        except Exception as error:
            log.error("读取文件失败，原因是",error)
        #获取section的键
        options=cf.options("config")
        #获取section的值
        items=cf.items()