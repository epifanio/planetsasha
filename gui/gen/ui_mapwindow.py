# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mapwindow.ui'
#
# Created: Thu Jul 25 21:30:42 2013
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
        MapWindow.resize(664, 510)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapWindow.sizePolicy().hasHeightForWidth())
        MapWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/loading.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MapWindow.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(MapWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 331))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmbDataset = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbDataset.sizePolicy().hasHeightForWidth())
        self.cmbDataset.setSizePolicy(sizePolicy)
        self.cmbDataset.setObjectName(_fromUtf8("cmbDataset"))
        self.cmbDataset.addItem(_fromUtf8(""))
        self.cmbDataset.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbDataset)
        self.btDepth = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btDepth.sizePolicy().hasHeightForWidth())
        self.btDepth.setSizePolicy(sizePolicy)
        self.btDepth.setMinimumSize(QtCore.QSize(100, 0))
        self.btDepth.setObjectName(_fromUtf8("btDepth"))
        self.horizontalLayout.addWidget(self.btDepth)
        self.btCurrent = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btCurrent.sizePolicy().hasHeightForWidth())
        self.btCurrent.setSizePolicy(sizePolicy)
        self.btCurrent.setObjectName(_fromUtf8("btCurrent"))
        self.horizontalLayout.addWidget(self.btCurrent)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.progressBar = QtGui.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setStyleSheet(_fromUtf8("background-image: url(:/icons/icons/loading.gif);"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.lbLoading = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbLoading.sizePolicy().hasHeightForWidth())
        self.lbLoading.setSizePolicy(sizePolicy)
        self.lbLoading.setMinimumSize(QtCore.QSize(30, 0))
        self.lbLoading.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lbLoading.setText(_fromUtf8(""))
        self.lbLoading.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/loading.gif")))
        self.lbLoading.setObjectName(_fromUtf8("lbLoading"))
        self.horizontalLayout_3.addWidget(self.lbLoading)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(MapWindow)
        QtCore.QMetaObject.connectSlotsByName(MapWindow)

    def retranslateUi(self, MapWindow):
        MapWindow.setWindowTitle(_translate("MapWindow", "NC Viewer", None))
        self.cmbDataset.setItemText(0, _translate("MapWindow", "--select--", None))
        self.cmbDataset.setItemText(1, _translate("MapWindow", "fvcom/hindcasts/30yr_gom3", None))
        self.btDepth.setText(_translate("MapWindow", "Depth", None))
        self.btCurrent.setText(_translate("MapWindow", "FVCOM Current", None))

import resources_rc
