# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mapwindow.ui'
#
# Created: Wed Jul 24 21:04:07 2013
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
        MapWindow.resize(562, 386)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapWindow.sizePolicy().hasHeightForWidth())
        MapWindow.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtGui.QWidget(MapWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 541, 31))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cmbDataset = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cmbDataset.setObjectName(_fromUtf8("cmbDataset"))
        self.cmbDataset.addItem(_fromUtf8(""))
        self.cmbDataset.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.cmbDataset)

        self.retranslateUi(MapWindow)
        QtCore.QMetaObject.connectSlotsByName(MapWindow)

    def retranslateUi(self, MapWindow):
        MapWindow.setWindowTitle(_translate("MapWindow", "NC Viewer", None))
        self.cmbDataset.setItemText(0, _translate("MapWindow", "--select--", None))
        self.cmbDataset.setItemText(1, _translate("MapWindow", "http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc", None))

