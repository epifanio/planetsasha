# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/importwindow.ui'
#
# Created: Sun Oct  6 20:36:21 2013
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

class Ui_ImportWindow(object):
    def setupUi(self, ImportWindow):
        ImportWindow.setObjectName(_fromUtf8("ImportWindow"))
        ImportWindow.setWindowModality(QtCore.Qt.NonModal)
        ImportWindow.resize(554, 538)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImportWindow.sizePolicy().hasHeightForWidth())
        ImportWindow.setSizePolicy(sizePolicy)
        ImportWindow.setMinimumSize(QtCore.QSize(554, 431))
        self.inputPage = QtGui.QWizardPage()
        self.inputPage.setObjectName(_fromUtf8("inputPage"))
        self.layoutWidget = QtGui.QWidget(self.inputPage)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 672, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmbUrl = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbUrl.sizePolicy().hasHeightForWidth())
        self.cmbUrl.setSizePolicy(sizePolicy)
        self.cmbUrl.setMinimumSize(QtCore.QSize(0, 0))
        self.cmbUrl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cmbUrl.setObjectName(_fromUtf8("cmbUrl"))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.cmbUrl.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbUrl)
        self.cmbType = QtGui.QComboBox(self.layoutWidget)
        self.cmbType.setObjectName(_fromUtf8("cmbType"))
        self.cmbType.addItem(_fromUtf8(""))
        self.cmbType.addItem(_fromUtf8(""))
        self.cmbType.addItem(_fromUtf8(""))
        self.cmbType.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbType)
        self.cmbService = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbService.sizePolicy().hasHeightForWidth())
        self.cmbService.setSizePolicy(sizePolicy)
        self.cmbService.setObjectName(_fromUtf8("cmbService"))
        self.cmbService.addItem(_fromUtf8(""))
        self.cmbService.addItem(_fromUtf8(""))
        self.cmbService.addItem(_fromUtf8(""))
        self.cmbService.setItemText(2, _fromUtf8("CSW"))
        self.cmbService.addItem(_fromUtf8(""))
        self.cmbService.setItemText(3, _fromUtf8("OpenDAP"))
        self.cmbService.addItem(_fromUtf8(""))
        self.cmbService.addItem(_fromUtf8(""))
        self.cmbService.setItemText(5, _fromUtf8("WMS"))
        self.horizontalLayout.addWidget(self.cmbService)
        self.bboxWidget = QtGui.QWidget(self.inputPage)
        self.bboxWidget.setGeometry(QtCore.QRect(10, 90, 521, 271))
        self.bboxWidget.setObjectName(_fromUtf8("bboxWidget"))
        self.layoutWidget_2 = QtGui.QWidget(self.bboxWidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 521, 271))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.bboxLayout = QtGui.QGridLayout(self.layoutWidget_2)
        self.bboxLayout.setMargin(0)
        self.bboxLayout.setObjectName(_fromUtf8("bboxLayout"))
        self.txtE = QtGui.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtE.sizePolicy().hasHeightForWidth())
        self.txtE.setSizePolicy(sizePolicy)
        self.txtE.setMinimumSize(QtCore.QSize(50, 0))
        self.txtE.setObjectName(_fromUtf8("txtE"))
        self.bboxLayout.addWidget(self.txtE, 1, 0, 1, 1)
        self.txtW = QtGui.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtW.sizePolicy().hasHeightForWidth())
        self.txtW.setSizePolicy(sizePolicy)
        self.txtW.setMinimumSize(QtCore.QSize(50, 0))
        self.txtW.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtW.setObjectName(_fromUtf8("txtW"))
        self.bboxLayout.addWidget(self.txtW, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(220, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.txtN = QtGui.QLineEdit(self.layoutWidget_2)
        self.txtN.setObjectName(_fromUtf8("txtN"))
        self.horizontalLayout_2.addWidget(self.txtN)
        spacerItem1 = QtGui.QSpacerItem(220, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bboxLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(220, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.txtS = QtGui.QLineEdit(self.layoutWidget_2)
        self.txtS.setObjectName(_fromUtf8("txtS"))
        self.horizontalLayout_3.addWidget(self.txtS)
        spacerItem3 = QtGui.QSpacerItem(220, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.bboxLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.layoutWidget_2)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.bboxLayout.addWidget(self.graphicsView, 1, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.inputPage)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 521, 27))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.leKeywords = QtGui.QLineEdit(self.layoutWidget1)
        self.leKeywords.setObjectName(_fromUtf8("leKeywords"))
        self.horizontalLayout_6.addWidget(self.leKeywords)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.cmbMaxRec = QtGui.QComboBox(self.layoutWidget1)
        self.cmbMaxRec.setObjectName(_fromUtf8("cmbMaxRec"))
        self.cmbMaxRec.addItem(_fromUtf8(""))
        self.cmbMaxRec.setItemText(0, _fromUtf8("-1"))
        self.cmbMaxRec.addItem(_fromUtf8(""))
        self.cmbMaxRec.setItemText(1, _fromUtf8("10"))
        self.cmbMaxRec.addItem(_fromUtf8(""))
        self.cmbMaxRec.setItemText(2, _fromUtf8("20"))
        self.cmbMaxRec.addItem(_fromUtf8(""))
        self.cmbMaxRec.setItemText(3, _fromUtf8("30"))
        self.cmbMaxRec.addItem(_fromUtf8(""))
        self.cmbMaxRec.setItemText(4, _fromUtf8("40"))
        self.cmbMaxRec.addItem(_fromUtf8(""))
        self.cmbMaxRec.setItemText(5, _fromUtf8("50"))
        self.cmbMaxRec.addItem(_fromUtf8(""))
        self.cmbMaxRec.setItemText(6, _fromUtf8("100"))
        self.horizontalLayout_6.addWidget(self.cmbMaxRec)
        ImportWindow.addPage(self.inputPage)
        self.treePage = QtGui.QWizardPage()
        self.treePage.setObjectName(_fromUtf8("treePage"))
        self.verticalLayoutWidget = QtGui.QWidget(self.treePage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 451))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lblInfo = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfo.sizePolicy().hasHeightForWidth())
        self.lblInfo.setSizePolicy(sizePolicy)
        self.lblInfo.setMinimumSize(QtCore.QSize(0, 50))
        self.lblInfo.setAutoFillBackground(False)
        self.lblInfo.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);"))
        self.lblInfo.setObjectName(_fromUtf8("lblInfo"))
        self.verticalLayout_3.addWidget(self.lblInfo)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btAddTo = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btAddTo.setObjectName(_fromUtf8("btAddTo"))
        self.horizontalLayout_4.addWidget(self.btAddTo)
        self.btRem = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btRem.setObjectName(_fromUtf8("btRem"))
        self.horizontalLayout_4.addWidget(self.btRem)
        spacerItem5 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.splitter = QtGui.QSplitter(self.verticalLayoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeView = QtGui.QTreeView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(0, 353))
        self.treeView.setMaximumSize(QtCore.QSize(16777215, 250))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.listView = QtGui.QListView(self.splitter)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_3.addWidget(self.splitter)
        ImportWindow.addPage(self.treePage)

        self.retranslateUi(ImportWindow)
        QtCore.QMetaObject.connectSlotsByName(ImportWindow)

    def retranslateUi(self, ImportWindow):
        ImportWindow.setWindowTitle(_translate("ImportWindow", "Import NetCDF", None))
        self.cmbUrl.setItemText(0, _translate("ImportWindow", "-- select source --", None))
        self.cmbUrl.setItemText(1, _translate("ImportWindow", "http://www.smast.umassd.edu:8080/thredds", None))
        self.cmbUrl.setItemText(2, _translate("ImportWindow", "http://cida.usgs.gov/geonetwork/srv/en/main.home", None))
        self.cmbUrl.setItemText(3, _translate("ImportWindow", "http://cmgds.marine.usgs.gov/geonetwork/srv/en/main.home", None))
        self.cmbUrl.setItemText(4, _translate("ImportWindow", "http://www.nodc.noaa.gov/geoportal/", None))
        self.cmbUrl.setItemText(5, _translate("ImportWindow", "http://www.ngdc.noaa.gov/geoportal/", None))
        self.cmbUrl.setItemText(6, _translate("ImportWindow", "http://geoport.whoi.edu/geoportal/", None))
        self.cmbUrl.setItemText(7, _translate("ImportWindow", "http://geoport.whoi.edu/gi-cat/", None))
        self.cmbUrl.setItemText(8, _translate("ImportWindow", "http://geo.gov.ckan.org/dataset", None))
        self.cmbType.setItemText(0, _translate("ImportWindow", "-- select type --", None))
        self.cmbType.setItemText(1, _translate("ImportWindow", "Thredds", None))
        self.cmbType.setItemText(2, _translate("ImportWindow", "GeoNetwork", None))
        self.cmbType.setItemText(3, _translate("ImportWindow", "GeoCatalog", None))
        self.cmbService.setItemText(0, _translate("ImportWindow", "-- select service --", None))
        self.cmbService.setItemText(1, _translate("ImportWindow", "None", None))
        self.cmbService.setItemText(4, _translate("ImportWindow", "WCS", None))
        self.txtE.setText(_translate("ImportWindow", "-180 E", None))
        self.txtW.setText(_translate("ImportWindow", "180 W", None))
        self.txtN.setText(_translate("ImportWindow", "-90 N", None))
        self.txtS.setText(_translate("ImportWindow", "90 S", None))
        self.label_4.setText(_translate("ImportWindow", "Keywords", None))
        self.label_3.setText(_translate("ImportWindow", "Max records:", None))
        self.lblInfo.setText(_translate("ImportWindow", "URL INFO", None))
        self.btAddTo.setText(_translate("ImportWindow", ">>", None))
        self.btRem.setText(_translate("ImportWindow", "<<", None))

