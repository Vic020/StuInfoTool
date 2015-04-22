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
            u'优秀': 90.0,
            u'良好': 80.0,
            u'中等': 70.0,
            u'及格': 60.0,
            u'不及格': 50.0,
            u'通过': 60.0,
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
            (credit1, grade1),
            (credit2, grade2),
        ]
    '''
    newgradelist = list()
    for (credit, grade) in gradelist:
        if type(grade) == unicode:
            grade = transformTable[grade]
        newgradelist.append((credit, grade))
    return newgradelist


def processOriginGradelist(gradelist):
    '''
        成绩数据转换，只需要学分和成绩
        gradelist = [
            (credit1, grade1),
            (credit2, grade2),
        ]
    '''
    newgradelist = list()
    for key in gradelist.keys():
        try:
            grade = float(gradelist[key][0])
            credit = float(gradelist[key][1])
        except UnicodeEncodeError:
            credit = gradelist[key][1]
        finally:
            newgradelist.append((grade, credit))
    print newgradelist
