# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/warnmsgwindow.ui'
#
# Created: Sat Jun 22 16:56:32 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WarnMsgWindow(object):
    def setupUi(self, WarnMsgWindow):
        WarnMsgWindow.setObjectName(_fromUtf8("WarnMsgWindow"))
        WarnMsgWindow.resize(480, 77)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/epi.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WarnMsgWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(WarnMsgWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.worningmessage = QtGui.QGroupBox(WarnMsgWindow)
        self.worningmessage.setTitle(_fromUtf8(""))
        self.worningmessage.setObjectName(_fromUtf8("worningmessage"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.worningmessage)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.label = QtGui.QLabel(self.worningmessage)
        self.label.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_21.addWidget(self.label)
        self.verticalLayout.addWidget(self.worningmessage)

        self.retranslateUi(WarnMsgWindow)
        QtCore.QMetaObject.connectSlotsByName(WarnMsgWindow)

    def retranslateUi(self, WarnMsgWindow):
        WarnMsgWindow.setWindowTitle(QtGui.QApplication.translate("WarnMsgWindow", "Warning", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WarnMsgWindow", "Be sure one of the avaiable View Type icons is checked.", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
