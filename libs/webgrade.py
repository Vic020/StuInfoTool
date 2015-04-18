#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Wed Feb 04 2015 18:55:39

@author  : Vic Yu(http://vicyu.net)

@brief   :
'''
import requests
import re


class GradeSpider(object):
    """
    信息门户的爬虫
    提供登录、登出、总成绩、和本学期成绩方法
    """
    def __init__(self, name=None, passwd=None):
        super(GradeSpider, self).__init__()

        self.initVar()

        self.headers['zjh'] = name
        self.headers['mm'] = passwd
        if self.headers['zjh'] is not None and self.headers['mm'] is not None:
            self.login(self.headers['zjh'], self.headers['mm'])

    def initVar(self):
        """
        初始化所有成员变量
        self.URLs表示所有url地址
        """
        self.baseURL = 'http://210.30.1.60/'
        self.URLs = {'login':
                     self.baseURL + 'loginAction.do',
                     'AllGrade':
                     self.baseURL + 'gradeLnAllAction.do?oper=fainfo',
                     'TermGrade':
                     self.baseURL + 'bxqcjcxAction.do?pageSize=300',
                     'logout':
                     self.baseURL + 'logout.do'
                     }
        self.headers = {'ldap': 'auth',
                        'zjh': None,
                        'mm': None}
        self.session = None

    def login(self, name=None, passwd=None):
        """
        登录
        成功返回True 失败返回False
        """
        self.headers['zjh'] = name
        self.headers['mm'] = passwd

        self.session = requests.session()

        response = self.session.post(self.URLs['login'], data=self.headers)
        html = response.text
        reslist = re.findall(r'errorTop', html)
        if len(reslist) > 0:
            self.session = None
            return False
        return True

    def logout(self):
        if self.session is None:
            return
        response = self.session.post(self.URLs['logout'])
        html = response.text
        reslist = re.findall(r'welcomeMessage', html)
        if len(reslist) > 0:
            self.session = None
            return True
        return False

    def getAllGrade(self):
        if self.session is None:
            return
        response = self.session.get(self.URLs['AllGrade'])
        html = response.text
        return html

    def getTermGrade(self):
        if self.session is None:
            return
        response = self.session.get(self.URLs['TermGrade'])
        html = response.text
        return html

    def close(self):
        return self.logout()
