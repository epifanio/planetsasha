# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sashamainwindow.ui'
#
# Created: Sat Jun 29 18:32:23 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SashaMainWindow(object):
    def setupUi(self, SashaMainWindow):
        SashaMainWindow.setObjectName(_fromUtf8("SashaMainWindow"))
        SashaMainWindow.resize(1005, 861)
        self.centralwidget = QtGui.QWidget(SashaMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(20, 30, 971, 761))
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        SashaMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SashaMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSasha = QtGui.QMenu(self.menubar)
        self.menuSasha.setObjectName(_fromUtf8("menuSasha"))
        SashaMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SashaMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SashaMainWindow.setStatusBar(self.statusbar)
        self.actionNavigation = QtGui.QAction(SashaMainWindow)
        self.actionNavigation.setObjectName(_fromUtf8("actionNavigation"))
        self.actionQuery = QtGui.QAction(SashaMainWindow)
        self.actionQuery.setObjectName(_fromUtf8("actionQuery"))
        self.actionGPS = QtGui.QAction(SashaMainWindow)
        self.actionGPS.setObjectName(_fromUtf8("actionGPS"))
        self.actionData = QtGui.QAction(SashaMainWindow)
        self.actionData.setObjectName(_fromUtf8("actionData"))
        self.menuSasha.addAction(self.actionNavigation)
        self.menuSasha.addAction(self.actionQuery)
        self.menuSasha.addAction(self.actionGPS)
        self.menuSasha.addAction(self.actionData)
        self.menubar.addAction(self.menuSasha.menuAction())

        self.retranslateUi(SashaMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SashaMainWindow)

    def retranslateUi(self, SashaMainWindow):
        SashaMainWindow.setWindowTitle(QtGui.QApplication.translate("SashaMainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSasha.setTitle(QtGui.QApplication.translate("SashaMainWindow", "Sasha", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNavigation.setText(QtGui.QApplication.translate("SashaMainWindow", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuery.setText(QtGui.QApplication.translate("SashaMainWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGPS.setText(QtGui.QApplication.translate("SashaMainWindow", "GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionData.setText(QtGui.QApplication.translate("SashaMainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))

