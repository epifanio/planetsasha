# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/querywindow.ui'
#
# Created: Sun Jun 30 22:33:39 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QueryWindow(object):
    def setupUi(self, QueryWindow):
        QueryWindow.setObjectName(_fromUtf8("QueryWindow"))
        QueryWindow.resize(750, 455)
        self.verticalLayoutWidget_2 = QtGui.QWidget(QueryWindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 721, 431))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(30)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.btnAddRast = QtGui.QToolButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAddRast.setFont(font)
        self.btnAddRast.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/element-cell.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddRast.setIcon(icon)
        self.btnAddRast.setObjectName(_fromUtf8("btnAddRast"))
        self.horizontalLayout_18.addWidget(self.btnAddRast)
        self.btnDelRast = QtGui.QToolButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnDelRast.setFont(font)
        self.btnDelRast.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/element-cell-delete.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelRast.setIcon(icon1)
        self.btnDelRast.setObjectName(_fromUtf8("btnDelRast"))
        self.horizontalLayout_18.addWidget(self.btnDelRast)
        self.refreshlayerlist = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.refreshlayerlist.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.refreshlayerlist.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/mActionDraw.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshlayerlist.setIcon(icon2)
        self.refreshlayerlist.setObjectName(_fromUtf8("refreshlayerlist"))
        self.horizontalLayout_18.addWidget(self.refreshlayerlist)
        self.btnAddVect = QtGui.QToolButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAddVect.setFont(font)
        self.btnAddVect.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/element-vector.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddVect.setIcon(icon3)
        self.btnAddVect.setObjectName(_fromUtf8("btnAddVect"))
        self.horizontalLayout_18.addWidget(self.btnAddVect)
        self.btnDelVect = QtGui.QToolButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelVect.setFont(font)
        self.btnDelVect.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/element-vector-remove.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelVect.setIcon(icon4)
        self.btnDelVect.setObjectName(_fromUtf8("btnDelVect"))
        self.horizontalLayout_18.addWidget(self.btnDelVect)
        self.renderoptions = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.renderoptions.setMinimumSize(QtCore.QSize(20, 0))
        self.renderoptions.setMaximumSize(QtCore.QSize(30, 16777215))
        self.renderoptions.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/gimp_0.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renderoptions.setIcon(icon5)
        self.renderoptions.setCheckable(True)
        self.renderoptions.setObjectName(_fromUtf8("renderoptions"))
        self.horizontalLayout_18.addWidget(self.renderoptions)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.setPenColor = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.setPenColor.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.setPenColor.setObjectName(_fromUtf8("setPenColor"))
        self.horizontalLayout_8.addWidget(self.setPenColor)
        self.PenColor = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.PenColor.setMaximumSize(QtCore.QSize(90, 16777215))
        self.PenColor.setObjectName(_fromUtf8("PenColor"))
        self.horizontalLayout_8.addWidget(self.PenColor)
        self.setBrushColor = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.setBrushColor.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.setBrushColor.setObjectName(_fromUtf8("setBrushColor"))
        self.horizontalLayout_8.addWidget(self.setBrushColor)
        self.BrushColor = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.BrushColor.setMaximumSize(QtCore.QSize(90, 16777215))
        self.BrushColor.setObjectName(_fromUtf8("BrushColor"))
        self.horizontalLayout_8.addWidget(self.BrushColor)
        self.PointSize = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.PointSize.setMinimumSize(QtCore.QSize(30, 0))
        self.PointSize.setMaximumSize(QtCore.QSize(40, 16777215))
        self.PointSize.setObjectName(_fromUtf8("PointSize"))
        self.horizontalLayout_8.addWidget(self.PointSize)
        self.LineWidth = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.LineWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.LineWidth.setProperty("value", 2)
        self.LineWidth.setObjectName(_fromUtf8("LineWidth"))
        self.horizontalLayout_8.addWidget(self.LineWidth)
        self.Fill = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.Fill.setObjectName(_fromUtf8("Fill"))
        self.horizontalLayout_8.addWidget(self.Fill)
        self.Thickness = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.Thickness.setObjectName(_fromUtf8("Thickness"))
        self.horizontalLayout_8.addWidget(self.Thickness)
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_8.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.layerTable = QtGui.QTableWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerTable.sizePolicy().hasHeightForWidth())
        self.layerTable.setSizePolicy(sizePolicy)
        self.layerTable.setObjectName(_fromUtf8("layerTable"))
        self.layerTable.setColumnCount(1)
        self.layerTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.layerTable.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_5.addWidget(self.layerTable)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.getlisttoquery = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.getlisttoquery.setMinimumSize(QtCore.QSize(0, 20))
        self.getlisttoquery.setMaximumSize(QtCore.QSize(23, 23))
        self.getlisttoquery.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.getlisttoquery.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gui-help.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getlisttoquery.setIcon(icon6)
        self.getlisttoquery.setObjectName(_fromUtf8("getlisttoquery"))
        self.horizontalLayout.addWidget(self.getlisttoquery)
        self.update = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.update.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/grass_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update.setIcon(icon7)
        self.update.setObjectName(_fromUtf8("update"))
        self.horizontalLayout.addWidget(self.update)
        self.longitude = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.longitude.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.longitude.setObjectName(_fromUtf8("longitude"))
        self.horizontalLayout.addWidget(self.longitude)
        self.latitude = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.latitude.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.latitude.setObjectName(_fromUtf8("latitude"))
        self.horizontalLayout.addWidget(self.latitude)
        self.gcmd = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.gcmd.setObjectName(_fromUtf8("gcmd"))
        self.horizontalLayout.addWidget(self.gcmd)
        self.gcmdexec = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.gcmdexec.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.gcmdexec.setIcon(icon7)
        self.gcmdexec.setCheckable(True)
        self.gcmdexec.setObjectName(_fromUtf8("gcmdexec"))
        self.horizontalLayout.addWidget(self.gcmdexec)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(QueryWindow)
        QtCore.QMetaObject.connectSlotsByName(QueryWindow)

    def retranslateUi(self, QueryWindow):
        QueryWindow.setWindowTitle(QtGui.QApplication.translate("QueryWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddRast.setToolTip(QtGui.QApplication.translate("QueryWindow", "Add raster layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddRast.setText(QtGui.QApplication.translate("QueryWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelRast.setToolTip(QtGui.QApplication.translate("QueryWindow", "Remove Raster Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelRast.setText(QtGui.QApplication.translate("QueryWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddVect.setToolTip(QtGui.QApplication.translate("QueryWindow", "Add Vector Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddVect.setText(QtGui.QApplication.translate("QueryWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelVect.setToolTip(QtGui.QApplication.translate("QueryWindow", "Remove Vector Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelVect.setText(QtGui.QApplication.translate("QueryWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.renderoptions.setText(QtGui.QApplication.translate("QueryWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.setPenColor.setText(QtGui.QApplication.translate("QueryWindow", "Pen", None, QtGui.QApplication.UnicodeUTF8))
        self.PenColor.setText(QtGui.QApplication.translate("QueryWindow", "111,111,111", None, QtGui.QApplication.UnicodeUTF8))
        self.setBrushColor.setText(QtGui.QApplication.translate("QueryWindow", "Brush", None, QtGui.QApplication.UnicodeUTF8))
        self.BrushColor.setText(QtGui.QApplication.translate("QueryWindow", "111,111,111", None, QtGui.QApplication.UnicodeUTF8))
        self.PointSize.setText(QtGui.QApplication.translate("QueryWindow", "1,1", None, QtGui.QApplication.UnicodeUTF8))
        self.Fill.setText(QtGui.QApplication.translate("QueryWindow", "Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.Thickness.setText(QtGui.QApplication.translate("QueryWindow", "Thickness", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("QueryWindow", "kml", None, QtGui.QApplication.UnicodeUTF8))
        item = self.layerTable.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("QueryWindow", "GRASS Layer(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.gcmdexec.setText(QtGui.QApplication.translate("QueryWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
