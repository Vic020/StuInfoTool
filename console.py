#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Mon Mar 16 2015 01:32:27

@author  : JonnyF(http://jonnyf.com)
'''
import sys
import getopt
import grade
import os


def Usage():
    print 'StulnfoTool usage:'
    print '-h,--help: print help message.'
    print '-u:Input username'
    print '-p:Input password'


def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'hu:p:', ['u=', 'p='])
    except getopt.GetoptError, err:
        print str(err)
        Usage()
        sys.exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            Usage()
            sys.exit(1)
        elif o in ('-u'):
            username = a
        elif o in ('-p'):
            password = a
        else:
            print 'unhandled option'
            exit(3)

    if username != '' and password != '':
        grades = grade.Grade(username, password)
        gradespider = grades.verifyLogin()
        if gradespider:
            grades.generateSheet()
            print 'Successful Please go to the desktop view'
            os.system('C:\Users\Jonny\Desktop\AllResult.xls')
        else:
            print 'username or password error'
    else:
        Usage()

if __name__ == '__main__':
    main(sys.argv)
