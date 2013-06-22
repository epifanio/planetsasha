#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class QueryWindow(QtGui.QTabWidget):
    def __init__(self, parent = None):

        QtGui.QWidget.__init__(self, parent)
        self.setupUi()
        self.retranslateUi()
        self.grassvectoroption.hide()

    def connectSignals(self):

        self.connect(self.renderoptions, QtCore.SIGNAL("clicked()"), self.getRenderOptions)
        self.connect(self.renderoptions, QtCore.SIGNAL("clicked()"), self.showrenderoptions)            
        
    def setupUi(self):        
        self.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea_3 = QtGui.QScrollArea(self)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, -89, 541, 308))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.frame = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.addRlayer = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.addRlayer.setFont(font)
        self.addRlayer.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/element-cell.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addRlayer.setIcon(icon2)
        self.addRlayer.setObjectName(_fromUtf8("addRlayer"))
        self.horizontalLayout_14.addWidget(self.addRlayer)
        self.removeRlayer = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.removeRlayer.setFont(font)
        self.removeRlayer.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/element-cell-delete.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeRlayer.setIcon(icon3)
        self.removeRlayer.setObjectName(_fromUtf8("removeRlayer"))
        self.horizontalLayout_14.addWidget(self.removeRlayer)
        self.GrassRLayer = QtGui.QComboBox(self.frame)
        self.GrassRLayer.setObjectName(_fromUtf8("GrassRLayer"))
        self.horizontalLayout_14.addWidget(self.GrassRLayer)
        self.line_13 = QtGui.QFrame(self.frame)
        self.line_13.setFrameShape(QtGui.QFrame.VLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.horizontalLayout_14.addWidget(self.line_13)
        self.refreshlayerlist = QtGui.QToolButton(self.frame)
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
#####        self.refreshlayerlist.setIcon(icon1)
        self.refreshlayerlist.setObjectName(_fromUtf8("refreshlayerlist"))
        self.horizontalLayout_14.addWidget(self.refreshlayerlist)
        self.line_12 = QtGui.QFrame(self.frame)
        self.line_12.setFrameShape(QtGui.QFrame.VLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.horizontalLayout_14.addWidget(self.line_12)
        self.GrassVLayer = QtGui.QComboBox(self.frame)
        self.GrassVLayer.setObjectName(_fromUtf8("GrassVLayer"))
        self.horizontalLayout_14.addWidget(self.GrassVLayer)
        self.addVlayer = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.addVlayer.setFont(font)
        self.addVlayer.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/element-vector.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addVlayer.setIcon(icon4)
        self.addVlayer.setObjectName(_fromUtf8("addVlayer"))
        self.horizontalLayout_14.addWidget(self.addVlayer)
        self.removeVlayer = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.removeVlayer.setFont(font)
        self.removeVlayer.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
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
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/element-vector-remove.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeVlayer.setIcon(icon5)
        self.removeVlayer.setObjectName(_fromUtf8("removeVlayer"))
        self.horizontalLayout_14.addWidget(self.removeVlayer)
        self.renderoptions = QtGui.QToolButton(self.frame)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gimp_0.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renderoptions.setIcon(icon6)
        self.renderoptions.setCheckable(True)
        self.renderoptions.setObjectName(_fromUtf8("renderoptions"))
        self.horizontalLayout_14.addWidget(self.renderoptions)
        self.verticalLayout_19.addWidget(self.frame)
        self.grassvectoroption = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        self.grassvectoroption.setObjectName(_fromUtf8("grassvectoroption"))
        self.grassvectoroptions = QtGui.QHBoxLayout(self.grassvectoroption)
        self.grassvectoroptions.setObjectName(_fromUtf8("grassvectoroptions"))
        self.setPenColor = QtGui.QToolButton(self.grassvectoroption)
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
        self.grassvectoroptions.addWidget(self.setPenColor)
        self.PenColor = QtGui.QLineEdit(self.grassvectoroption)
        self.PenColor.setMaximumSize(QtCore.QSize(90, 16777215))
        self.PenColor.setObjectName(_fromUtf8("PenColor"))
        self.grassvectoroptions.addWidget(self.PenColor)
        self.setBrushColor = QtGui.QToolButton(self.grassvectoroption)
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
        self.grassvectoroptions.addWidget(self.setBrushColor)
        self.BrushColor = QtGui.QLineEdit(self.grassvectoroption)
        self.BrushColor.setMaximumSize(QtCore.QSize(90, 16777215))
        self.BrushColor.setObjectName(_fromUtf8("BrushColor"))
        self.grassvectoroptions.addWidget(self.BrushColor)
        self.PointSize = QtGui.QLineEdit(self.grassvectoroption)
        self.PointSize.setMinimumSize(QtCore.QSize(30, 0))
        self.PointSize.setMaximumSize(QtCore.QSize(40, 16777215))
        self.PointSize.setObjectName(_fromUtf8("PointSize"))
        self.grassvectoroptions.addWidget(self.PointSize)
        self.LineWidth = QtGui.QSpinBox(self.grassvectoroption)
        self.LineWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.LineWidth.setProperty(_fromUtf8("value"), 2)
        self.LineWidth.setObjectName(_fromUtf8("LineWidth"))
        self.grassvectoroptions.addWidget(self.LineWidth)
        self.Fill = QtGui.QCheckBox(self.grassvectoroption)
        self.Fill.setObjectName(_fromUtf8("Fill"))
        self.grassvectoroptions.addWidget(self.Fill)
        self.Thickness = QtGui.QCheckBox(self.grassvectoroption)
        self.Thickness.setObjectName(_fromUtf8("Thickness"))
        self.grassvectoroptions.addWidget(self.Thickness)
        self.checkBox = QtGui.QCheckBox(self.grassvectoroption)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.grassvectoroptions.addWidget(self.checkBox)
        self.verticalLayout_19.addWidget(self.grassvectoroption)
        self.splitter_3 = QtGui.QSplitter(self.scrollAreaWidgetContents_3)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.splitter_3)
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.splitter_2 = QtGui.QSplitter(self.horizontalLayoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.splitter_2)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame1 = QtGui.QFrame(self.groupBox_2)
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 58))
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.grassquery = QtGui.QHBoxLayout(self.frame1)
        self.grassquery.setObjectName(_fromUtf8("grassquery"))
        self.update = QtGui.QToolButton(self.frame1)
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

        self.update.setObjectName(_fromUtf8("update"))
        self.grassquery.addWidget(self.update)
        self.getlisttoquery = QtGui.QToolButton(self.frame1)
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gui-help.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getlisttoquery.setIcon(icon8)
        self.getlisttoquery.setObjectName(_fromUtf8("getlisttoquery"))
        self.grassquery.addWidget(self.getlisttoquery)
        self.longitude = QtGui.QLineEdit(self.frame1)
        self.longitude.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.longitude.setObjectName(_fromUtf8("longitude"))
        self.grassquery.addWidget(self.longitude)
        self.latitude = QtGui.QLineEdit(self.frame1)
        self.latitude.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.latitude.setObjectName(_fromUtf8("latitude"))
        self.grassquery.addWidget(self.latitude)
        self.gcmd = QtGui.QComboBox(self.frame1)
        self.gcmd.setObjectName(_fromUtf8("gcmd"))
        self.grassquery.addWidget(self.gcmd)
        self.gcmdexec = QtGui.QToolButton(self.frame1)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/grass_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gcmdexec.setIcon(icon7)
        self.gcmdexec.setCheckable(True)
        self.gcmdexec.setObjectName(_fromUtf8("gcmdexec"))
        self.grassquery.addWidget(self.gcmdexec)
        self.verticalLayout_4.addWidget(self.frame1)
        self.splitter_5 = QtGui.QSplitter(self.groupBox_2)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.tableWidget = QtGui.QTableWidget(self.splitter_5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item.setIcon(icon2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item.setIcon(icon4)
        self.QueryResultsRaster = QtGui.QTextEdit(self.splitter_5)
        self.QueryResultsRaster.setObjectName(_fromUtf8("QueryResultsRaster"))
        self.QueryResultsVector = QtGui.QTextEdit(self.splitter_5)
        self.QueryResultsVector.setObjectName(_fromUtf8("QueryResultsVector"))
        self.verticalLayout_4.addWidget(self.splitter_5)
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.verticalLayout_19.addWidget(self.splitter_3)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea_3)
        

    def retranslateUi(self):
        self.addRlayer.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Add Raster Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.addRlayer.setText(QtGui.QApplication.translate("OssimPlanetSasha", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.removeRlayer.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Remove Raster Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.removeRlayer.setText(QtGui.QApplication.translate("OssimPlanetSasha", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.GrassRLayer.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Raster Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.GrassVLayer.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Vector Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.addVlayer.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Add Vector Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.addVlayer.setText(QtGui.QApplication.translate("OssimPlanetSasha", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.removeVlayer.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Remove Vector Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.removeVlayer.setText(QtGui.QApplication.translate("OssimPlanetSasha", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.renderoptions.setText(QtGui.QApplication.translate("OssimPlanetSasha", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.setPenColor.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Pen", None, QtGui.QApplication.UnicodeUTF8))
        self.PenColor.setText(QtGui.QApplication.translate("OssimPlanetSasha", "111,111,111", None, QtGui.QApplication.UnicodeUTF8))
        self.setBrushColor.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Brush", None, QtGui.QApplication.UnicodeUTF8))
        self.BrushColor.setText(QtGui.QApplication.translate("OssimPlanetSasha", "111,111,111", None, QtGui.QApplication.UnicodeUTF8))
        self.PointSize.setText(QtGui.QApplication.translate("OssimPlanetSasha", "1,1", None, QtGui.QApplication.UnicodeUTF8))
        self.Fill.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.Thickness.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Thickness", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("OssimPlanetSasha", "kml", None, QtGui.QApplication.UnicodeUTF8))
        self.gcmdexec.setText(QtGui.QApplication.translate("OssimPlanetSasha", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("OssimPlanetSasha", "Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("OssimPlanetSasha", "Vector", None, QtGui.QApplication.UnicodeUTF8))
        


                                  
    
