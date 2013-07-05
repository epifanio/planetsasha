# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/layerlistwindow.ui'
#
# Created: Sat Jun 29 17:02:04 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LayerListWindow(object):
    def setupUi(self, LayerListWindow):
        LayerListWindow.setObjectName(_fromUtf8("LayerListWindow"))
        LayerListWindow.resize(491, 419)
        self.lstLayers = QtGui.QListView(LayerListWindow)
        self.lstLayers.setGeometry(QtCore.QRect(10, 70, 471, 301))
        self.lstLayers.setObjectName(_fromUtf8("lstLayers"))
        self.btnFetch = QtGui.QPushButton(LayerListWindow)
        self.btnFetch.setGeometry(QtCore.QRect(380, 30, 98, 31))
        self.btnFetch.setObjectName(_fromUtf8("btnFetch"))
        self.txtSearch = QtGui.QLineEdit(LayerListWindow)
        self.txtSearch.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.btnDone = QtGui.QPushButton(LayerListWindow)
        self.btnDone.setGeometry(QtCore.QRect(400, 380, 81, 31))
        self.btnDone.setObjectName(_fromUtf8("btnDone"))

        self.retranslateUi(LayerListWindow)
        QtCore.QMetaObject.connectSlotsByName(LayerListWindow)

    def retranslateUi(self, LayerListWindow):
        LayerListWindow.setWindowTitle(QtGui.QApplication.translate("LayerListWindow", "Layer(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFetch.setText(QtGui.QApplication.translate("LayerListWindow", "Fetch", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDone.setText(QtGui.QApplication.translate("LayerListWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))

