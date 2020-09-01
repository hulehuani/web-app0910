#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:12
# @Author  : yuzhenyu
# @File    : logs.py

import time
import logging
import os


class Log:
    """
    对公共的日志的封装。
     每天都会生成一个当天的日志文本，如果当天执行多次，则都在一个文本里。目前没有设置日志文本大小
    """

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Log, "_instance"):
            Log._instance = Log(*args, **kwargs)
        return Log._instance

    def save_log(self):
        file = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
        self.filename = os.path.join(file, "logs", "%s.logs" % time.strftime("%Y_%M_%D"))
        self.logger = logging.getLogger()
        #设定日志等级
        self.logger.setLevel(logging.DEBUG)
        #设定日志格式
        self.formater = logging.Formatter(
            "[%(asctime)s] %(name)s][%(filename)s:%(lineno)d] [%(levelname)s][%(message)s")

    def output_consle_logs(self):
        """
        把日志输出到控制台
        :return:
        """
        self.consle = logging.StreamHandler()
        self.consle.setLevel(logging.DEBUG)
        self.consle.setFormatter(self.formater)
        self.logger.addHandler(self.consle)

    def output_file_logs(self):
        """
        把日志暂时输出到文本里
        :return:
        """
        self.file_log = logging.FileHandler()
        self.file_log.setLevel(logging.DEBUG)
        self.file_log.setFormatter(self.formater)
        self.logger.addHandler(self.file_log)

    def judge_log(self, level, msg):
        """
        判断日志等级
        :param level: 日志等级
        :param msg: 自定义日志信息
        :return:
        """
        if level == "debug":
            self.logger.debug(msg)
        elif level == "info":
            self.logger.info(msg)
        elif level == "warning":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "critical":
            self.logger.critical(msg)

    @staticmethod
    def debug(self,msg):
        self.judge_log("debug",msg)

    @staticmethod
    def info(self,msg):
        self.judge_log("info", msg)

    @staticmethod
    def warning(self,msg):
        self.judge_log("warning", msg)

    @staticmethod
    def error(self,msg):
        self.judge_log("error", msg)

    @staticmethod
    def critical(self,msg):
        self.judge_log("critical", msg)
