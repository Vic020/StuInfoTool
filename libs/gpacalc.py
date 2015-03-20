#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Fri Mar 06 2015 00:32:03

@author  : Vic Yu(http://vicyu.net)

GPA计算类
'''
#issue1:应该使用装饰器重写 2015/3/18
#issue2:算法的正确性 2015/3/18


def GPA_DLNU(
        gradelist,
        transform=True,
        transformTable={
            '优秀': 90,
            '良好': 80
        }):
    gpa = float()
    gradelist = processOriginGradelist(gradelist)
    if transform is True:
        gradelist = transformGrade(gradelist, transformTable)
    return gpa


def GPA_PKU(gradelist):
    gpa = float()
    return gpa


def GPA_NorthAmerica():
    pass


def GPA_standard4_0(gradelist):
    gpa = float()
    return gpa


def GPA_standardImprovement(gradelist):
    gpa = float()
    return gpa


def GPA_standard4_3(gradelist):
    gpa = float()
    return gpa


def transformGrade(gradelist, transformTable):
    return gradelist


def processOriginGradelist(gradelist):
    return gradelist
