#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Wed Feb 04 2015 23:11:29

@author  : Vic Yu(http://vicyu.net) JonnyF(http://jonnyf.com)
'''
import sys
from PyQt4 import QtGui, QtCore
from grade import Grade


class GradeListWindow(QtGui.QMainWindow):
    """

    """
    def __init__(self, parent=None, username=None, passwd=None):
        super(GradeListWindow, self).__init__(parent)

        self.initUI()
        self.parent = parent
        self.name = username
        self.passwd = passwd

    def initUI(self):
        btn = QtGui.QPushButton(u'保存为xls到桌面', self)
        btn.clicked.connect(self.xlsdDesktop)
        self.resize(600, 400)
        self.center()

    def closeEvent(self, e):
        self.close()

    def center(self):  # 主窗口居中显示函数

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def xlsdDesktop(self):
        grades = grade.Grade(self.name, self.passwd)
        try:
            grades.verifyLogin()
            grades.generateSheet()
            QtGui.QMessageBox.warning(self, u'提醒', u'表格生成成功！请到桌面上查看')
        except:
            QtGui.QMessageBox.warning(self, u'提醒', u'表格生成错误！')


class LoginWindow(QtGui.QWidget):
    """

    """
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        # self.gradespider = GradeSpider()

        self.nameLbl = QtGui.QLabel(u'学 号:')
        self.nameLe = QtGui.QLineEdit()
        self.nameLe.setMaxLength(10)

        self.passwdLbl = QtGui.QLabel(u'密 码:')
        self.passwdLe = QtGui.QLineEdit()
        self.passwdLe.setEchoMode(QtGui.QLineEdit.Password)

        self.commitBtn = QtGui.QPushButton(u'登 录')
        self.commitBtn.clicked.connect(self.commitComfirm)

        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(self.nameLbl)
        hbox1.addWidget(self.nameLe)
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.passwdLbl)
        hbox2.addWidget(self.passwdLe)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.commitBtn)

        self.resize(200, 120)
        self.setWindowTitle(u'信息查询')
        self.setWindowIcon(QtGui.QIcon('img/logo32x.ico'))
        self.setLayout(vbox)

    def commitComfirm(self):
        name = str(self.nameLe.text())
        passwd = str(self.passwdLe.text())
        if not hasattr(self, 'grade'):
            self.grade = Grade()
        if self.grade.login(name, passwd):
            QtGui.QMessageBox.warning(self, u'提醒', u'登录成功')
            gradelistwindow = GradeListWindow(self, name, passwd)
            self.hide()
            self.close()
            gradelistwindow.show()
        else:
            QtGui.QMessageBox.warning(self, u'提醒', u'用户名或密码错误')

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Enter:
            self.commitComfirm()


def main():
    app = QtGui.QApplication(sys.argv)
    loginwindow = LoginWindow()
    loginwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
