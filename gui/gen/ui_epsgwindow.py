# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/epsgwindow.ui'
#
# Created: Sat Jun 22 17:01:53 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EpsgWindow(object):
    def setupUi(self, EpsgWindow):
        EpsgWindow.setObjectName(_fromUtf8("EpsgWindow"))
        EpsgWindow.resize(320, 296)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/600px-Brosen_windrose.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EpsgWindow.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(EpsgWindow)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(EpsgWindow)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Code_rb = QtGui.QRadioButton(self.groupBox)
        self.Code_rb.setObjectName(_fromUtf8("Code_rb"))
        self.horizontalLayout.addWidget(self.Code_rb)
        self.Params_rb = QtGui.QRadioButton(self.groupBox)
        self.Params_rb.setObjectName(_fromUtf8("Params_rb"))
        self.horizontalLayout.addWidget(self.Params_rb)
        self.Title_rb = QtGui.QRadioButton(self.groupBox)
        self.Title_rb.setObjectName(_fromUtf8("Title_rb"))
        self.horizontalLayout.addWidget(self.Title_rb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Code_cb = QtGui.QCheckBox(self.groupBox)
        self.Code_cb.setObjectName(_fromUtf8("Code_cb"))
        self.horizontalLayout_2.addWidget(self.Code_cb)
        self.Params_cb = QtGui.QCheckBox(self.groupBox)
        self.Params_cb.setObjectName(_fromUtf8("Params_cb"))
        self.horizontalLayout_2.addWidget(self.Params_cb)
        self.Title_cb = QtGui.QCheckBox(self.groupBox)
        self.Title_cb.setObjectName(_fromUtf8("Title_cb"))
        self.horizontalLayout_2.addWidget(self.Title_cb)
        self.All_cb = QtGui.QCheckBox(self.groupBox)
        self.All_cb.setObjectName(_fromUtf8("All_cb"))
        self.horizontalLayout_2.addWidget(self.All_cb)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.Search = QtGui.QToolButton(self.groupBox)
        self.Search.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
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
"                                       stop: 0 white, stop: 1 blue);\n"
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
        self.Search.setObjectName(_fromUtf8("Search"))
        self.horizontalLayout_4.addWidget(self.Search)
        self.OutList = QtGui.QComboBox(self.groupBox)
        self.OutList.setObjectName(_fromUtf8("OutList"))
        self.horizontalLayout_4.addWidget(self.OutList)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.printout = QtGui.QTextEdit(EpsgWindow)
        self.printout.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.printout.setObjectName(_fromUtf8("printout"))
        self.verticalLayout_3.addWidget(self.printout)

        self.retranslateUi(EpsgWindow)
        QtCore.QMetaObject.connectSlotsByName(EpsgWindow)

    def retranslateUi(self, EpsgWindow):
        EpsgWindow.setWindowTitle(QtGui.QApplication.translate("EpsgWindow", "Epsg", None, QtGui.QApplication.UnicodeUTF8))
        self.Code_rb.setText(QtGui.QApplication.translate("EpsgWindow", "Code", None, QtGui.QApplication.UnicodeUTF8))
        self.Params_rb.setText(QtGui.QApplication.translate("EpsgWindow", "Params", None, QtGui.QApplication.UnicodeUTF8))
        self.Title_rb.setText(QtGui.QApplication.translate("EpsgWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.Code_cb.setText(QtGui.QApplication.translate("EpsgWindow", "Code", None, QtGui.QApplication.UnicodeUTF8))
        self.Params_cb.setText(QtGui.QApplication.translate("EpsgWindow", "Param", None, QtGui.QApplication.UnicodeUTF8))
        self.Title_cb.setText(QtGui.QApplication.translate("EpsgWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.All_cb.setText(QtGui.QApplication.translate("EpsgWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.Search.setText(QtGui.QApplication.translate("EpsgWindow", "->", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
