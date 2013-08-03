# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/navigationwindow.ui'
#
# Created: Sat Aug  3 17:44:48 2013
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

class Ui_NavigationWindow(object):
    def setupUi(self, NavigationWindow):
        NavigationWindow.setObjectName(_fromUtf8("NavigationWindow"))
        NavigationWindow.resize(676, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NavigationWindow.sizePolicy().hasHeightForWidth())
        NavigationWindow.setSizePolicy(sizePolicy)
        NavigationWindow.setMinimumSize(QtCore.QSize(676, 600))
        NavigationWindow.setMaximumSize(QtCore.QSize(676, 600))
        self.scrollArea = QtGui.QScrollArea(NavigationWindow)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 640, 561))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_5 = QtGui.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 638, 559))
        self.scrollAreaWidgetContents_5.setObjectName(_fromUtf8("scrollAreaWidgetContents_5"))
        self.verticalLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 639, 754))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setMargin(30)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.southeast = QtGui.QToolButton(self.verticalLayoutWidget)
        self.southeast.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.southeast.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_10.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.southeast.setIcon(icon)
        self.southeast.setObjectName(_fromUtf8("southeast"))
        self.gridLayout.addWidget(self.southeast, 7, 5, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 6, 1, 1)
        self.west = QtGui.QToolButton(self.verticalLayoutWidget)
        self.west.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_5.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.west.setIcon(icon1)
        self.west.setObjectName(_fromUtf8("west"))
        self.gridLayout.addWidget(self.west, 5, 2, 1, 1)
        self.east = QtGui.QToolButton(self.verticalLayoutWidget)
        self.east.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.east.setIcon(icon2)
        self.east.setObjectName(_fromUtf8("east"))
        self.gridLayout.addWidget(self.east, 5, 5, 1, 1)
        self.center = QtGui.QToolButton(self.verticalLayoutWidget)
        self.center.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.center.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/pan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.center.setIcon(icon3)
        self.center.setObjectName(_fromUtf8("center"))
        self.gridLayout.addWidget(self.center, 5, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.north = QtGui.QToolButton(self.verticalLayoutWidget)
        self.north.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.north.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.north.setIcon(icon4)
        self.north.setObjectName(_fromUtf8("north"))
        self.gridLayout.addWidget(self.north, 2, 4, 1, 1)
        self.zoomDell = QtGui.QToolButton(self.verticalLayoutWidget)
        self.zoomDell.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.zoomDell.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomDell.setIcon(icon5)
        self.zoomDell.setObjectName(_fromUtf8("zoomDell"))
        self.gridLayout.addWidget(self.zoomDell, 8, 2, 1, 1)
        self.northwest = QtGui.QToolButton(self.verticalLayoutWidget)
        self.northwest.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.northwest.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_9.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.northwest.setIcon(icon6)
        self.northwest.setObjectName(_fromUtf8("northwest"))
        self.gridLayout.addWidget(self.northwest, 2, 2, 1, 1)
        self.northeast = QtGui.QToolButton(self.verticalLayoutWidget)
        self.northeast.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.northeast.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_7.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.northeast.setIcon(icon7)
        self.northeast.setObjectName(_fromUtf8("northeast"))
        self.gridLayout.addWidget(self.northeast, 2, 5, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 4, 1, 1)
        self.clview = QtGui.QToolButton(self.verticalLayoutWidget)
        self.clview.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.clview.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/600px-Brosen_windrose.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clview.setIcon(icon8)
        self.clview.setObjectName(_fromUtf8("clview"))
        self.gridLayout.addWidget(self.clview, 8, 4, 1, 1)
        self.zoomAdd = QtGui.QToolButton(self.verticalLayoutWidget)
        self.zoomAdd.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.zoomAdd.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomAdd.setIcon(icon9)
        self.zoomAdd.setObjectName(_fromUtf8("zoomAdd"))
        self.gridLayout.addWidget(self.zoomAdd, 8, 5, 1, 1)
        self.southwest = QtGui.QToolButton(self.verticalLayoutWidget)
        self.southwest.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.southwest.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_8.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.southwest.setIcon(icon10)
        self.southwest.setObjectName(_fromUtf8("southwest"))
        self.gridLayout.addWidget(self.southwest, 7, 2, 1, 1)
        self.south = QtGui.QToolButton(self.verticalLayoutWidget)
        self.south.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/shapeimage_6.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.south.setIcon(icon11)
        self.south.setObjectName(_fromUtf8("south"))
        self.gridLayout.addWidget(self.south, 7, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.compassLayout = QtGui.QVBoxLayout()
        self.compassLayout.setObjectName(_fromUtf8("compassLayout"))
        self.label_25 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.compassLayout.addWidget(self.label_25)
        self.compassArea = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.compassArea.setWidgetResizable(True)
        self.compassArea.setObjectName(_fromUtf8("compassArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 91, 82))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.compassArea.setWidget(self.scrollAreaWidgetContents_2)
        self.compassLayout.addWidget(self.compassArea)
        self.verticalLayout_3.addLayout(self.compassLayout)
        self.rollLayout = QtGui.QVBoxLayout()
        self.rollLayout.setObjectName(_fromUtf8("rollLayout"))
        self.label_26 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.rollLayout.addWidget(self.label_26)
        self.rollArea = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.rollArea.setWidgetResizable(True)
        self.rollArea.setObjectName(_fromUtf8("rollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 91, 82))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.rollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.rollLayout.addWidget(self.rollArea)
        self.verticalLayout_3.addLayout(self.rollLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(50, 0))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_10.addWidget(self.label_15)
        self.Lat = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Lat.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Lat.setAlignment(QtCore.Qt.AlignCenter)
        self.Lat.setObjectName(_fromUtf8("Lat"))
        self.horizontalLayout_10.addWidget(self.Lat)
        self.Lon = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Lon.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Lon.setAlignment(QtCore.Qt.AlignCenter)
        self.Lon.setObjectName(_fromUtf8("Lon"))
        self.horizontalLayout_10.addWidget(self.Lon)
        self.Alt = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Alt.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Alt.setObjectName(_fromUtf8("Alt"))
        self.horizontalLayout_10.addWidget(self.Alt)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.line_11 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.verticalLayout.addWidget(self.line_11)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_16.setMinimumSize(QtCore.QSize(50, 0))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_14.addWidget(self.label_16)
        self.lookatLat = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lookatLat.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.lookatLat.setObjectName(_fromUtf8("lookatLat"))
        self.horizontalLayout_14.addWidget(self.lookatLat)
        self.lookatLon = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lookatLon.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.lookatLon.setObjectName(_fromUtf8("lookatLon"))
        self.horizontalLayout_14.addWidget(self.lookatLon)
        self.lookatAlt = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lookatAlt.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.lookatAlt.setObjectName(_fromUtf8("lookatAlt"))
        self.horizontalLayout_14.addWidget(self.lookatAlt)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.line_12 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.verticalLayout.addWidget(self.line_12)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_17.setMinimumSize(QtCore.QSize(50, 0))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_19.addWidget(self.label_17)
        self.NorthEast = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.NorthEast.setText(_fromUtf8(""))
        self.NorthEast.setObjectName(_fromUtf8("NorthEast"))
        self.horizontalLayout_19.addWidget(self.NorthEast)
        self.Nord = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Nord.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Nord.setAlignment(QtCore.Qt.AlignCenter)
        self.Nord.setObjectName(_fromUtf8("Nord"))
        self.horizontalLayout_19.addWidget(self.Nord)
        self.East = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.East.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.East.setAlignment(QtCore.Qt.AlignCenter)
        self.East.setObjectName(_fromUtf8("East"))
        self.horizontalLayout_19.addWidget(self.East)
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_19.addWidget(self.label_18)
        self.utmcode_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.utmcode_2.setMinimumSize(QtCore.QSize(45, 0))
        self.utmcode_2.setMaximumSize(QtCore.QSize(45, 16777215))
        self.utmcode_2.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.utmcode_2.setText(_fromUtf8(""))
        self.utmcode_2.setAlignment(QtCore.Qt.AlignCenter)
        self.utmcode_2.setObjectName(_fromUtf8("utmcode_2"))
        self.horizontalLayout_19.addWidget(self.utmcode_2)
        self.ellipse = QtGui.QComboBox(self.verticalLayoutWidget)
        self.ellipse.setMaximumSize(QtCore.QSize(150, 26))
        self.ellipse.setStyleSheet(_fromUtf8(""))
        self.ellipse.setObjectName(_fromUtf8("ellipse"))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.horizontalLayout_19.addWidget(self.ellipse)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.line_13 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.verticalLayout.addWidget(self.line_13)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.Place = QtGui.QComboBox(self.verticalLayoutWidget)
        self.Place.setStyleSheet(_fromUtf8(""))
        self.Place.setObjectName(_fromUtf8("Place"))
        self.Place.addItem(_fromUtf8(""))
        self.Place.setItemText(0, _fromUtf8(""))
        self.horizontalLayout_20.addWidget(self.Place)
        self.line_21 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_21.setFrameShape(QtGui.QFrame.VLine)
        self.line_21.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_21.setObjectName(_fromUtf8("line_21"))
        self.horizontalLayout_20.addWidget(self.line_21)
        self.refreshsqlite = QtGui.QToolButton(self.verticalLayoutWidget)
        self.refreshsqlite.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
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
        self.refreshsqlite.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/mActionDraw.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshsqlite.setIcon(icon12)
        self.refreshsqlite.setObjectName(_fromUtf8("refreshsqlite"))
        self.horizontalLayout_20.addWidget(self.refreshsqlite)
        self.line_22 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_22.setFrameShape(QtGui.QFrame.VLine)
        self.line_22.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_22.setObjectName(_fromUtf8("line_22"))
        self.horizontalLayout_20.addWidget(self.line_22)
        self.placezone = QtGui.QComboBox(self.verticalLayoutWidget)
        self.placezone.setStyleSheet(_fromUtf8(""))
        self.placezone.setObjectName(_fromUtf8("placezone"))
        self.horizontalLayout_20.addWidget(self.placezone)
        self.SendPosition = QtGui.QPushButton(self.verticalLayoutWidget)
        self.SendPosition.setMaximumSize(QtCore.QSize(30, 16777215))
        self.SendPosition.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 44px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }"))
        self.SendPosition.setObjectName(_fromUtf8("SendPosition"))
        self.horizontalLayout_20.addWidget(self.SendPosition)
        self.verticalLayout.addLayout(self.horizontalLayout_20)
        self.line_6 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_21.addWidget(self.label_19)
        self.SpeedSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpeedSpinBox.sizePolicy().hasHeightForWidth())
        self.SpeedSpinBox.setSizePolicy(sizePolicy)
        self.SpeedSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.SpeedSpinBox.setProperty("value", 1.0)
        self.SpeedSpinBox.setObjectName(_fromUtf8("SpeedSpinBox"))
        self.horizontalLayout_21.addWidget(self.SpeedSpinBox)
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_20.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_21.addWidget(self.label_20)
        self.SpeedMultipler = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.SpeedMultipler.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.SpeedMultipler.setObjectName(_fromUtf8("SpeedMultipler"))
        self.horizontalLayout_21.addWidget(self.SpeedMultipler)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem5)
        self.View = QtGui.QComboBox(self.verticalLayoutWidget)
        self.View.setStyleSheet(_fromUtf8(""))
        self.View.setObjectName(_fromUtf8("View"))
        self.View.addItem(_fromUtf8(""))
        self.View.addItem(_fromUtf8(""))
        self.horizontalLayout_21.addWidget(self.View)
        self.Head = QtGui.QComboBox(self.verticalLayoutWidget)
        self.Head.setStyleSheet(_fromUtf8(""))
        self.Head.setModelColumn(0)
        self.Head.setObjectName(_fromUtf8("Head"))
        self.Head.addItem(_fromUtf8(""))
        self.Head.setItemText(0, _fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.horizontalLayout_21.addWidget(self.Head)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.line_24 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_24.setFrameShape(QtGui.QFrame.HLine)
        self.line_24.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_24.setObjectName(_fromUtf8("line_24"))
        self.verticalLayout.addWidget(self.line_24)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.hsHeading = QtGui.QToolButton(self.verticalLayoutWidget)
        self.hsHeading.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        self.hsHeading.setCheckable(True)
        self.hsHeading.setObjectName(_fromUtf8("hsHeading"))
        self.horizontalLayout_22.addWidget(self.hsHeading)
        self.HandlingSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.HandlingSpinBox.setStyleSheet(_fromUtf8("border: 1px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background: rgb(231, 231, 231);"))
        self.HandlingSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HandlingSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.HandlingSpinBox.setMinimum(-360.0)
        self.HandlingSpinBox.setMaximum(360.0)
        self.HandlingSpinBox.setObjectName(_fromUtf8("HandlingSpinBox"))
        self.horizontalLayout_22.addWidget(self.HandlingSpinBox)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem6)
        self.hsPitch = QtGui.QToolButton(self.verticalLayoutWidget)
        self.hsPitch.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        self.hsPitch.setCheckable(True)
        self.hsPitch.setObjectName(_fromUtf8("hsPitch"))
        self.horizontalLayout_22.addWidget(self.hsPitch)
        self.PitchSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.PitchSpinBox.setStyleSheet(_fromUtf8("border: 1px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background: rgb(231, 231, 231);"))
        self.PitchSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PitchSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.PitchSpinBox.setMinimum(-90.0)
        self.PitchSpinBox.setMaximum(90.0)
        self.PitchSpinBox.setObjectName(_fromUtf8("PitchSpinBox"))
        self.horizontalLayout_22.addWidget(self.PitchSpinBox)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem7)
        self.hsRoll = QtGui.QToolButton(self.verticalLayoutWidget)
        self.hsRoll.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        self.hsRoll.setCheckable(True)
        self.hsRoll.setObjectName(_fromUtf8("hsRoll"))
        self.horizontalLayout_22.addWidget(self.hsRoll)
        self.RollSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.RollSpinBox.setStyleSheet(_fromUtf8("border: 1px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background: rgb(231, 231, 231);"))
        self.RollSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RollSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.RollSpinBox.setAccelerated(False)
        self.RollSpinBox.setMinimum(-90.0)
        self.RollSpinBox.setMaximum(90.0)
        self.RollSpinBox.setObjectName(_fromUtf8("RollSpinBox"))
        self.horizontalLayout_22.addWidget(self.RollSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.line_23 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_23.setFrameShape(QtGui.QFrame.HLine)
        self.line_23.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_23.setObjectName(_fromUtf8("line_23"))
        self.verticalLayout.addWidget(self.line_23)
        self.HandlingSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.HandlingSlider.setMinimum(-360)
        self.HandlingSlider.setMaximum(360)
        self.HandlingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HandlingSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.HandlingSlider.setTickInterval(10)
        self.HandlingSlider.setObjectName(_fromUtf8("HandlingSlider"))
        self.verticalLayout.addWidget(self.HandlingSlider)
        self.PitchSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.PitchSlider.setMinimum(-90)
        self.PitchSlider.setMaximum(90)
        self.PitchSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PitchSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.PitchSlider.setObjectName(_fromUtf8("PitchSlider"))
        self.verticalLayout.addWidget(self.PitchSlider)
        self.RollSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.RollSlider.setMinimum(-90)
        self.RollSlider.setMaximum(90)
        self.RollSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RollSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.RollSlider.setTickInterval(10)
        self.RollSlider.setObjectName(_fromUtf8("RollSlider"))
        self.verticalLayout.addWidget(self.RollSlider)
        self.line_15 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.verticalLayout.addWidget(self.line_15)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.hsZoom = QtGui.QToolButton(self.verticalLayoutWidget)
        self.hsZoom.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        self.hsZoom.setCheckable(True)
        self.hsZoom.setObjectName(_fromUtf8("hsZoom"))
        self.horizontalLayout_24.addWidget(self.hsZoom)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem8)
        self.ZoomSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZoomSpinBox.sizePolicy().hasHeightForWidth())
        self.ZoomSpinBox.setSizePolicy(sizePolicy)
        self.ZoomSpinBox.setAutoFillBackground(True)
        self.ZoomSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.ZoomSpinBox.setWrapping(False)
        self.ZoomSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ZoomSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.ZoomSpinBox.setAccelerated(True)
        self.ZoomSpinBox.setMinimum(-10000.0)
        self.ZoomSpinBox.setMaximum(27536977.99)
        self.ZoomSpinBox.setObjectName(_fromUtf8("ZoomSpinBox"))
        self.horizontalLayout_24.addWidget(self.ZoomSpinBox)
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_24.addWidget(self.label_21)
        self.ZoomStepSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.ZoomStepSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.ZoomStepSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.ZoomStepSpinBox.setMinimum(0.0)
        self.ZoomStepSpinBox.setMaximum(100000.0)
        self.ZoomStepSpinBox.setSingleStep(1.0)
        self.ZoomStepSpinBox.setProperty("value", 100.0)
        self.ZoomStepSpinBox.setObjectName(_fromUtf8("ZoomStepSpinBox"))
        self.horizontalLayout_24.addWidget(self.ZoomStepSpinBox)
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_24.addWidget(self.label_22)
        self.ZoomMultipler = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.ZoomMultipler.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.ZoomMultipler.setMinimum(0)
        self.ZoomMultipler.setObjectName(_fromUtf8("ZoomMultipler"))
        self.horizontalLayout_24.addWidget(self.ZoomMultipler)
        self.verticalLayout.addLayout(self.horizontalLayout_24)
        self.ZoomSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.ZoomSlider.setMinimum(-10000)
        self.ZoomSlider.setMaximum(27536977)
        self.ZoomSlider.setProperty("value", 5000)
        self.ZoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ZoomSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.ZoomSlider.setTickInterval(1000000)
        self.ZoomSlider.setObjectName(_fromUtf8("ZoomSlider"))
        self.verticalLayout.addWidget(self.ZoomSlider)
        self.line_14 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_14.setStyleSheet(_fromUtf8(""))
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.verticalLayout.addWidget(self.line_14)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.hsRange = QtGui.QToolButton(self.verticalLayoutWidget)
        self.hsRange.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        self.hsRange.setCheckable(True)
        self.hsRange.setObjectName(_fromUtf8("hsRange"))
        self.horizontalLayout_25.addWidget(self.hsRange)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem9)
        self.RangeSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RangeSpinBox.sizePolicy().hasHeightForWidth())
        self.RangeSpinBox.setSizePolicy(sizePolicy)
        self.RangeSpinBox.setAutoFillBackground(True)
        self.RangeSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.RangeSpinBox.setWrapping(True)
        self.RangeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RangeSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.RangeSpinBox.setAccelerated(True)
        self.RangeSpinBox.setMinimum(-10000.0)
        self.RangeSpinBox.setMaximum(27536977.99)
        self.RangeSpinBox.setProperty("value", 10000.0)
        self.RangeSpinBox.setObjectName(_fromUtf8("RangeSpinBox"))
        self.horizontalLayout_25.addWidget(self.RangeSpinBox)
        self.label_23 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_25.addWidget(self.label_23)
        self.RangeStepSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.RangeStepSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.RangeStepSpinBox.setMinimum(0.0)
        self.RangeStepSpinBox.setMaximum(100000.0)
        self.RangeStepSpinBox.setSingleStep(1.0)
        self.RangeStepSpinBox.setProperty("value", 100.0)
        self.RangeStepSpinBox.setObjectName(_fromUtf8("RangeStepSpinBox"))
        self.horizontalLayout_25.addWidget(self.RangeStepSpinBox)
        self.label_24 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_25.addWidget(self.label_24)
        self.RangeMultipler = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.RangeMultipler.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.RangeMultipler.setObjectName(_fromUtf8("RangeMultipler"))
        self.horizontalLayout_25.addWidget(self.RangeMultipler)
        self.verticalLayout.addLayout(self.horizontalLayout_25)
        self.line_16 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.verticalLayout.addWidget(self.line_16)
        self.RangeSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.RangeSlider.setMinimum(-10000)
        self.RangeSlider.setMaximum(27536977)
        self.RangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RangeSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.RangeSlider.setTickInterval(1000000)
        self.RangeSlider.setObjectName(_fromUtf8("RangeSlider"))
        self.verticalLayout.addWidget(self.RangeSlider)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_5)

        self.retranslateUi(NavigationWindow)
        self.Head.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(NavigationWindow)

    def retranslateUi(self, NavigationWindow):
        NavigationWindow.setWindowTitle(_translate("NavigationWindow", "Navigation", None))
        self.southeast.setToolTip(_translate("NavigationWindow", "SouthEast", None))
        self.west.setToolTip(_translate("NavigationWindow", "West", None))
        self.west.setText(_translate("NavigationWindow", " W", None))
        self.east.setToolTip(_translate("NavigationWindow", "East", None))
        self.east.setText(_translate("NavigationWindow", " E ", None))
        self.north.setToolTip(_translate("NavigationWindow", "North", None))
        self.northwest.setToolTip(_translate("NavigationWindow", "NordWest", None))
        self.northeast.setToolTip(_translate("NavigationWindow", "NordEast", None))
        self.southwest.setToolTip(_translate("NavigationWindow", "SouthWest", None))
        self.south.setToolTip(_translate("NavigationWindow", "South", None))
        self.south.setText(_translate("NavigationWindow", " S ", None))
        self.label_25.setText(_translate("NavigationWindow", "Heading°", None))
        self.label_26.setText(_translate("NavigationWindow", "Roll°", None))
        self.label_15.setText(_translate("NavigationWindow", "Eye", None))
        self.Lat.setToolTip(_translate("NavigationWindow", "Display Longitude value in decimal degrees", None))
        self.Lon.setToolTip(_translate("NavigationWindow", "Display Latitude value in decimal degrees", None))
        self.label_16.setText(_translate("NavigationWindow", "LookAt", None))
        self.label_17.setText(_translate("NavigationWindow", "N/E", None))
        self.Nord.setToolTip(_translate("NavigationWindow", "North - UTM coordinates - meters", None))
        self.East.setToolTip(_translate("NavigationWindow", "East - UTM coordinates - meters", None))
        self.label_18.setText(_translate("NavigationWindow", "UTM", None))
        self.utmcode_2.setToolTip(_translate("NavigationWindow", "UTM zone", None))
        self.ellipse.setToolTip(_translate("NavigationWindow", "Ellipsoid", None))
        self.ellipse.setItemText(0, _translate("NavigationWindow", "WGS-84", None))
        self.ellipse.setItemText(1, _translate("NavigationWindow", "Airy", None))
        self.ellipse.setItemText(2, _translate("NavigationWindow", "Australian National", None))
        self.ellipse.setItemText(3, _translate("NavigationWindow", "Bessel 1841", None))
        self.ellipse.setItemText(4, _translate("NavigationWindow", "Bessel 1841 (Nambia)", None))
        self.ellipse.setItemText(5, _translate("NavigationWindow", "Clarke 1866", None))
        self.ellipse.setItemText(6, _translate("NavigationWindow", "Clarke 1880", None))
        self.ellipse.setItemText(7, _translate("NavigationWindow", "Everest", None))
        self.ellipse.setItemText(8, _translate("NavigationWindow", "Fischer 1960 (Mercury)", None))
        self.ellipse.setItemText(9, _translate("NavigationWindow", "Fischer 1968", None))
        self.ellipse.setItemText(10, _translate("NavigationWindow", "GRS 1967", None))
        self.ellipse.setItemText(11, _translate("NavigationWindow", "GRS 1980", None))
        self.ellipse.setItemText(12, _translate("NavigationWindow", "Helmert 1906", None))
        self.ellipse.setItemText(13, _translate("NavigationWindow", "Hough", None))
        self.ellipse.setItemText(14, _translate("NavigationWindow", "International", None))
        self.ellipse.setItemText(15, _translate("NavigationWindow", "Krassovsky", None))
        self.ellipse.setItemText(16, _translate("NavigationWindow", "Modified Airy", None))
        self.ellipse.setItemText(17, _translate("NavigationWindow", "Modified Everest", None))
        self.ellipse.setItemText(18, _translate("NavigationWindow", "Modified Fischer 1960", None))
        self.ellipse.setItemText(19, _translate("NavigationWindow", "South American 1969", None))
        self.ellipse.setItemText(20, _translate("NavigationWindow", "WGS 60", None))
        self.ellipse.setItemText(21, _translate("NavigationWindow", "WGS 66", None))
        self.ellipse.setItemText(22, _translate("NavigationWindow", "WGS-72", None))
        self.ellipse.setItemText(23, _translate("NavigationWindow", "WGS-84", None))
        self.Place.setToolTip(_translate("NavigationWindow", "Geonames Zone", None))
        self.refreshsqlite.setToolTip(_translate("NavigationWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reload sqlite db</p></body></html>", None))
        self.placezone.setToolTip(_translate("NavigationWindow", "Geonames Place", None))
        self.SendPosition.setText(_translate("NavigationWindow", "Go", None))
        self.label_19.setText(_translate("NavigationWindow", "Pan-Step : Deg", None))
        self.SpeedSpinBox.setToolTip(_translate("NavigationWindow", "Pan Step in decimal degrees", None))
        self.label_20.setText(_translate("NavigationWindow", "* 10^-", None))
        self.SpeedMultipler.setToolTip(_translate("NavigationWindow", "PStep - 10^-x  multipler", None))
        self.View.setItemText(0, _translate("NavigationWindow", "LookAt", None))
        self.View.setItemText(1, _translate("NavigationWindow", "Camera", None))
        self.Head.setToolTip(_translate("NavigationWindow", "Heading mode", None))
        self.Head.setItemText(1, _translate("NavigationWindow", "Manual", None))
        self.Head.setItemText(2, _translate("NavigationWindow", "Auto", None))
        self.Head.setItemText(3, _translate("NavigationWindow", "N", None))
        self.Head.setItemText(4, _translate("NavigationWindow", "E", None))
        self.Head.setItemText(5, _translate("NavigationWindow", "SE", None))
        self.Head.setItemText(6, _translate("NavigationWindow", "S", None))
        self.Head.setItemText(7, _translate("NavigationWindow", "SW", None))
        self.Head.setItemText(8, _translate("NavigationWindow", "W", None))
        self.Head.setItemText(9, _translate("NavigationWindow", "NW", None))
        self.Head.setItemText(10, _translate("NavigationWindow", "NE", None))
        self.hsHeading.setText(_translate("NavigationWindow", "Heading ", None))
        self.hsPitch.setText(_translate("NavigationWindow", "Pitch", None))
        self.hsRoll.setText(_translate("NavigationWindow", "Roll ", None))
        self.hsZoom.setText(_translate("NavigationWindow", "Zoom ", None))
        self.ZoomSpinBox.setToolTip(_translate("NavigationWindow", "Zoom (altitude) value in meters", None))
        self.label_21.setText(_translate("NavigationWindow", "Step : m", None))
        self.ZoomStepSpinBox.setToolTip(_translate("NavigationWindow", "Zoom Step in meters", None))
        self.label_22.setText(_translate("NavigationWindow", "*10^", None))
        self.ZoomMultipler.setToolTip(_translate("NavigationWindow", "ZStep - 10^x  multipler", None))
        self.hsRange.setText(_translate("NavigationWindow", "Range ", None))
        self.RangeSpinBox.setToolTip(_translate("NavigationWindow", "Range (distance) in meters", None))
        self.label_23.setText(_translate("NavigationWindow", "Step : m", None))
        self.RangeStepSpinBox.setToolTip(_translate("NavigationWindow", "Zoom Step in meters", None))
        self.label_24.setText(_translate("NavigationWindow", "*10^", None))

import resources_rc
