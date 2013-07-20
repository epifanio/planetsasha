# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mapwindow.ui'
#
# Created: Sat Jul 20 14:44:53 2013
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

class Ui_MapWindow(object):
    def setupUi(self, MapWindow):
        MapWindow.setObjectName(_fromUtf8("MapWindow"))
        MapWindow.resize(546, 467)
        self.cmbDataset = QtGui.QComboBox(MapWindow)
        self.cmbDataset.setGeometry(QtCore.QRect(30, 20, 471, 31))
        self.cmbDataset.setObjectName(_fromUtf8("cmbDataset"))
        self.cmbDataset.addItem(_fromUtf8(""))
        self.cmbDataset.addItem(_fromUtf8(""))

        self.retranslateUi(MapWindow)
        QtCore.QMetaObject.connectSlotsByName(MapWindow)

    def retranslateUi(self, MapWindow):
        MapWindow.setWindowTitle(_translate("MapWindow", "NC Viewer", None))
        self.cmbDataset.setItemText(0, _translate("MapWindow", "--select--", None))
        self.cmbDataset.setItemText(1, _translate("MapWindow", "http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc", None))

