#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Fri Mar 06 2015 00:32:03

@author  : Vic Yu(http://vicyu.net)

GPA计算类
'''
Type_DLNU = 0
Type_PKU = 1
Type_NorthAmerica = 2
Type_Standard4_0 = 3
Type_StandardImprovement = 4
Type_Standard4_3 = 5


def GPA(
        gradelist,
        type_=Type_DLNU,
        transform=True,
        transformTable={
            '优秀': 90,
            '良好': 80,
            '中等': 70,
            '合格': 60,
            '不合格': 50,
        }):
    '''
        计算GPA
        gradelist: 由webgrade获得
        type_: 计算GPA类型
        transform: 是否转换中文等地
        transformTable: 中文等地转换表
    '''
    gradelist = processOriginGradelist(gradelist)
    if transform is True:
        gradelist = transformGrade(gradelist, transformTable)
    gpa = getGPA(gradelist, type_)
    return gpa


def getGPA(gradelist, type_=Type_DLNU):
    '''
        各个GPA算法
        返回：GPA浮点型数据
    '''
    gpa = float()
    if type_ == Type_DLNU:
        return gpa
    if type_ == Type_PKU:
        return gpa
    if type_ == Type_NorthAmerica:
        return gpa
    if type_ == Type_Standard4_0:
        return gpa
    if type_ == Type_Standard4_3:
        return gpa
    if type_ == Type_StandardImprovement:
        return gpa


def transformGrade(gradelist, transformTable):
    '''
        中文等地转换
        根据transformTable转换
        gradelist = [
            (grade1, credit1),
            (grade2, credit2),
        ]
    '''
    return gradelist


def processOriginGradelist(gradelist):
    '''
        成绩数据转换，只需要学分和成绩
        gradelist = [
            (grade1, credit1),
            (grade2, credit2),
        ]
    '''
    return gradelist
