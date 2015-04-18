#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Mon Mar 16 2015 01:29:07

@author  : Vic Yu(http://vicyu.net) JonnyF(http://jonnyf.com)
'''
from libs.webgrade import GradeSpider
from libs.htmlprocess import *
from libs.generatexls import Generatexls


class Grade(object):
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
        self.gradespider = GradeSpider()

    def verifyLogin(self, name=None, passwd=None):
        if name is not None:
            self.name = name
        if passwd is not None:
            self.passwd = passwd
        return self.gradespider.login(self.name, self.passwd)

    def close(self):
        return self.gradespider.close()

    def getAllGrade(self):
        html = self.gradespider.getAllGrade()
        gradelist = htmlProcessAllGrade(html)
        return gradelist

    def getTermGrade(self):
        html = self.gradespider.getTermGrade()
        gradelist = htmlProcessTermGrade(html)
        return gradelist

    def getGPA(self, type='DLNU'):
        pass

    def generateSheet(self):
        resultlist = self.getAllGrade()
        generatexls = Generatexls()
        generatexls.generatexls(resultlist)
