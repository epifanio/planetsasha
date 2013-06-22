# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/grasswindow.ui'
#
# Created: Sat Jun 22 17:03:24 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GrassWindow(object):
    def setupUi(self, GrassWindow):
        GrassWindow.setObjectName(_fromUtf8("GrassWindow"))
        GrassWindow.resize(289, 222)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/512 Terminal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GrassWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(GrassWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.outimageinfo = QtGui.QTextEdit(GrassWindow)
        self.outimageinfo.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.outimageinfo.setObjectName(_fromUtf8("outimageinfo"))
        self.verticalLayout.addWidget(self.outimageinfo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.command = QtGui.QLineEdit(GrassWindow)
        self.command.setObjectName(_fromUtf8("command"))
        self.horizontalLayout.addWidget(self.command)
        self.hist = QtGui.QComboBox(GrassWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hist.sizePolicy().hasHeightForWidth())
        self.hist.setSizePolicy(sizePolicy)
        self.hist.setMinimumSize(QtCore.QSize(10, 10))
        self.hist.setMaximumSize(QtCore.QSize(25, 16777215))
        self.hist.setObjectName(_fromUtf8("hist"))
        self.horizontalLayout.addWidget(self.hist)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GrassWindow)
        QtCore.QMetaObject.connectSlotsByName(GrassWindow)

    def retranslateUi(self, GrassWindow):
        GrassWindow.setWindowTitle(QtGui.QApplication.translate("GrassWindow", "Grass Window", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
