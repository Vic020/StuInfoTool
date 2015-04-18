#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On 2015-04-18 08:11:26

@author  : JonnyF(http://jonnyf.com)

生成excel类
'''
import os
import xlwt


class Generatexls(object):

    def __init__(self):
        self.wbk = xlwt.Workbook(encoding='utf-8')

    def getDesktopPath(self):
        return os.path.join(os.path.expanduser("~"), 'Desktop')

    def generatexls(self, resultlist, tablename='AllGrade'):
        sheet = self.wbk.add_sheet(tablename)

        sheet.write(0, 0, "课程名")
        sheet.write(0, 1, "学分")
        sheet.write(0, 2, "成绩")
        sheet.write(0, 3, "课程属性")
        sheet.write(0, 4, "课程号")
        sheet.write(0, 5, "课序号")
        sheet.write(0, 6, "英文课程名")

        index = 1
        for k, v in resultlist.iteritems():
            sheet.write(index, 0, k)
            sheet.write(index, 1, v[0])
            sheet.write(index, 2, v[1])
            sheet.write(index, 3, v[2])
            sheet.write(index, 4, v[3])
            sheet.write(index, 5, v[4])
            sheet.write(index, 6, v[5])
            index += 1

        filepath = self.getDesktopPath()
        if filepath == '':
            self.wbk.save('../AllResult.xls')
        else:
            self.wbk.save(filepath+'\AllResult.xls')
