#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Mon Mar 02 2015 00:46:33

@author  : Vic Yu(http://vicyu.net)
'''
#issue1:无法判断网页数据是否会出现重复数据 2015/3/15
from bs4 import BeautifulSoup


def htmlProcessAllGrade(html):
    """
    传入html原文，返回数据对象字典
    字典结构如下：
    resultlist =
    {
        '课程名1':[
            学分,
            成绩,
            课程属性,
            课程号,
            课序号,
            英文课程名]，
        '课程名2':[学分,成绩,课程属性,课程号,课序号,英文课程名]，
    }
    """
    resultlist = dict()
    root = BeautifulSoup(html)
    table = root.find_all('table', 'titleTop2')
    if len(table) > 0:
        table = table[0]
    trs = table.find_all('tr', 'odd')
    for tr in trs:
        td = tr.find_all('td')
        resultlist[' '.join(td[2].string.split())] = [
            ' '.join(td[4].string.split()),
            ' '.join(td[6].findChild('p').string.split()),
            ' '.join(td[5].string.split()),
            ' '.join(td[0].string.split()),
            ' '.join(td[1].string.split()),
            ' '.join(td[3].string.split())]
    return resultlist


def htmlProcessTermGrade(html):
    """
    传入html原文，返回数据对象字典
    字典结构如下：
    resultlist =
    {
        '课程名1':[
            学分,
            成绩,
            课程属性,
            课程号,
            课序号,
            英文课程名]，
        '课程名2':[学分,成绩,课程属性,课程号,课序号,英文课程名]，
    }
    """
    resultlist = dict()
    root = BeautifulSoup(html)
    table = root.find_all('table', 'titleTop2')
    if len(table) > 0:
        table = table[0]
    trs = table.find_all('tr', 'odd')
    for tr in trs:
        td = tr.find_all('td')
        resultlist[' '.join(td[2].string.split())] = [
            ' '.join(td[4].string.split()),
            ' '.join(td[6].string.split()),
            ' '.join(td[5].string.split()),
            ' '.join(td[0].string.split()),
            ' '.join(td[1].string.split()),
            ' '.join(td[3].string.split())]
    return resultlist
