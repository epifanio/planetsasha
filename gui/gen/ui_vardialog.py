# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/vardialog.ui'
#
# Created: Sun Oct 13 20:22:55 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VarDialog(object):
    def setupUi(self, VarDialog):
        VarDialog.setObjectName(_fromUtf8("VarDialog"))
        VarDialog.resize(364, 431)
        self.buttonBox = QtGui.QDialogButtonBox(VarDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 390, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(VarDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 371))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.retranslateUi(VarDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VarDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VarDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VarDialog)

    def retranslateUi(self, VarDialog):
        VarDialog.setWindowTitle(_translate("VarDialog", "Var Selection", None))

