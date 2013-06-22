# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/vectoropswindow.ui'
#
# Created: Sat Jun 22 17:05:05 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VectorOpsWindow(object):
    def setupUi(self, VectorOpsWindow):
        VectorOpsWindow.setObjectName(_fromUtf8("VectorOpsWindow"))
        VectorOpsWindow.resize(704, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/SquadraCompasso.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VectorOpsWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(VectorOpsWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(VectorOpsWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 684, 482))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Go = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.Go.setAutoFillBackground(False)
        self.Go.setTabPosition(QtGui.QTabWidget.North)
        self.Go.setDocumentMode(False)
        self.Go.setTabsClosable(False)
        self.Go.setMovable(True)
        self.Go.setObjectName(_fromUtf8("Go"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.rpjshpInput = QtGui.QPushButton(self.tab)
        self.rpjshpInput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjshpInput.setObjectName(_fromUtf8("rpjshpInput"))
        self.gridLayout_3.addWidget(self.rpjshpInput, 1, 0, 1, 1)
        self.rpjshpOutput = QtGui.QPushButton(self.tab)
        self.rpjshpOutput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjshpOutput.setObjectName(_fromUtf8("rpjshpOutput"))
        self.gridLayout_3.addWidget(self.rpjshpOutput, 2, 0, 1, 1)
        self.rpjshpInput_file = QtGui.QLineEdit(self.tab)
        self.rpjshpInput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjshpInput_file.setObjectName(_fromUtf8("rpjshpInput_file"))
        self.gridLayout_3.addWidget(self.rpjshpInput_file, 1, 1, 1, 1)
        self.rpjshpOutput_file = QtGui.QLineEdit(self.tab)
        self.rpjshpOutput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjshpOutput_file.setObjectName(_fromUtf8("rpjshpOutput_file"))
        self.gridLayout_3.addWidget(self.rpjshpOutput_file, 2, 1, 1, 1)
        self.rpjGCP2 = QtGui.QPushButton(self.tab)
        self.rpjGCP2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjGCP2.setObjectName(_fromUtf8("rpjGCP2"))
        self.gridLayout_3.addWidget(self.rpjGCP2, 5, 0, 1, 1)
        self.rpjGCP1 = QtGui.QPushButton(self.tab)
        self.rpjGCP1.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjGCP1.setObjectName(_fromUtf8("rpjGCP1"))
        self.gridLayout_3.addWidget(self.rpjGCP1, 4, 0, 1, 1)
        self.rpjGCP2_file = QtGui.QLineEdit(self.tab)
        self.rpjGCP2_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjGCP2_file.setObjectName(_fromUtf8("rpjGCP2_file"))
        self.gridLayout_3.addWidget(self.rpjGCP2_file, 5, 1, 1, 1)
        self.rpjGCP1_file = QtGui.QLineEdit(self.tab)
        self.rpjGCP1_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjGCP1_file.setObjectName(_fromUtf8("rpjGCP1_file"))
        self.gridLayout_3.addWidget(self.rpjGCP1_file, 4, 1, 1, 1)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 2)
        self.line_8 = QtGui.QFrame(self.tab)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout_3.addWidget(self.line_8, 0, 0, 1, 2)
        self.line_9 = QtGui.QFrame(self.tab)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout_3.addWidget(self.line_9, 11, 0, 1, 2)
        self.line_11 = QtGui.QFrame(self.tab)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.gridLayout_3.addWidget(self.line_11, 7, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rpjConforme = QtGui.QRadioButton(self.tab)
        self.rpjConforme.setObjectName(_fromUtf8("rpjConforme"))
        self.horizontalLayout.addWidget(self.rpjConforme)
        self.rpjAffine = QtGui.QRadioButton(self.tab)
        self.rpjAffine.setChecked(True)
        self.rpjAffine.setObjectName(_fromUtf8("rpjAffine"))
        self.horizontalLayout.addWidget(self.rpjAffine)
        self.gridLayout_3.addLayout(self.horizontalLayout, 8, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 10, 0, 1, 1)
        self.line_10 = QtGui.QFrame(self.tab)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout_3.addWidget(self.line_10, 9, 0, 1, 2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.setsrs = QtGui.QComboBox(self.tab)
        self.setsrs.setMinimumSize(QtCore.QSize(0, 30))
        self.setsrs.setObjectName(_fromUtf8("setsrs"))
        self.setsrs.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.setsrs)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 10, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.rpjGo = QtGui.QPushButton(self.tab)
        self.rpjGo.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjGo.setObjectName(_fromUtf8("rpjGo"))
        self.horizontalLayout_2.addWidget(self.rpjGo)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.Go.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.trshpInput = QtGui.QPushButton(self.tab_2)
        self.trshpInput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.trshpInput.setObjectName(_fromUtf8("trshpInput"))
        self.gridLayout.addWidget(self.trshpInput, 1, 0, 1, 1)
        self.trshpOutput = QtGui.QPushButton(self.tab_2)
        self.trshpOutput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.trshpOutput.setObjectName(_fromUtf8("trshpOutput"))
        self.gridLayout.addWidget(self.trshpOutput, 2, 0, 1, 1)
        self.trshpInput_file = QtGui.QLineEdit(self.tab_2)
        self.trshpInput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.trshpInput_file.setObjectName(_fromUtf8("trshpInput_file"))
        self.gridLayout.addWidget(self.trshpInput_file, 1, 1, 1, 3)
        self.tx = QtGui.QLineEdit(self.tab_2)
        self.tx.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.tx.setAlignment(QtCore.Qt.AlignCenter)
        self.tx.setObjectName(_fromUtf8("tx"))
        self.gridLayout.addWidget(self.tx, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 2)
        self.line_15 = QtGui.QFrame(self.tab_2)
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.gridLayout.addWidget(self.line_15, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)
        self.ty = QtGui.QLineEdit(self.tab_2)
        self.ty.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.ty.setAlignment(QtCore.Qt.AlignCenter)
        self.ty.setObjectName(_fromUtf8("ty"))
        self.gridLayout.addWidget(self.ty, 4, 3, 1, 1)
        self.trshpOutput_file = QtGui.QLineEdit(self.tab_2)
        self.trshpOutput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.trshpOutput_file.setObjectName(_fromUtf8("trshpOutput_file"))
        self.gridLayout.addWidget(self.trshpOutput_file, 2, 1, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.line_14 = QtGui.QFrame(self.tab_2)
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.verticalLayout_3.addWidget(self.line_14)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.trGo = QtGui.QPushButton(self.tab_2)
        self.trGo.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.trGo.setObjectName(_fromUtf8("trGo"))
        self.horizontalLayout_4.addWidget(self.trGo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.Go.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rotshpInput = QtGui.QPushButton(self.tab_4)
        self.rotshpInput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rotshpInput.setObjectName(_fromUtf8("rotshpInput"))
        self.gridLayout_2.addWidget(self.rotshpInput, 1, 0, 1, 1)
        self.rotshpOutput = QtGui.QPushButton(self.tab_4)
        self.rotshpOutput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rotshpOutput.setObjectName(_fromUtf8("rotshpOutput"))
        self.gridLayout_2.addWidget(self.rotshpOutput, 2, 0, 1, 1)
        self.rotshpInput_file = QtGui.QLineEdit(self.tab_4)
        self.rotshpInput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rotshpInput_file.setObjectName(_fromUtf8("rotshpInput_file"))
        self.gridLayout_2.addWidget(self.rotshpInput_file, 1, 1, 1, 1)
        self.rotshpOutput_file = QtGui.QLineEdit(self.tab_4)
        self.rotshpOutput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rotshpOutput_file.setObjectName(_fromUtf8("rotshpOutput_file"))
        self.gridLayout_2.addWidget(self.rotshpOutput_file, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.tab_4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.tab_4)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 2)
        self.line_13 = QtGui.QFrame(self.tab_4)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.gridLayout_2.addWidget(self.line_13, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.angle = QtGui.QLineEdit(self.tab_4)
        self.angle.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.angle.setAlignment(QtCore.Qt.AlignCenter)
        self.angle.setObjectName(_fromUtf8("angle"))
        self.horizontalLayout_9.addWidget(self.angle)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 4, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.line_12 = QtGui.QFrame(self.tab_4)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.verticalLayout_4.addWidget(self.line_12)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.rotGo = QtGui.QPushButton(self.tab_4)
        self.rotGo.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rotGo.setObjectName(_fromUtf8("rotGo"))
        self.horizontalLayout_3.addWidget(self.rotGo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.Go.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.rpjtxtInput = QtGui.QPushButton(self.tab_3)
        self.rpjtxtInput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjtxtInput.setObjectName(_fromUtf8("rpjtxtInput"))
        self.gridLayout_4.addWidget(self.rpjtxtInput, 1, 0, 1, 1)
        self.rpjtxtGCP1 = QtGui.QPushButton(self.tab_3)
        self.rpjtxtGCP1.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjtxtGCP1.setObjectName(_fromUtf8("rpjtxtGCP1"))
        self.gridLayout_4.addWidget(self.rpjtxtGCP1, 4, 0, 1, 1)
        self.rpjtxtGCP2 = QtGui.QPushButton(self.tab_3)
        self.rpjtxtGCP2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjtxtGCP2.setObjectName(_fromUtf8("rpjtxtGCP2"))
        self.gridLayout_4.addWidget(self.rpjtxtGCP2, 5, 0, 1, 1)
        self.rpjtxtInput_file = QtGui.QLineEdit(self.tab_3)
        self.rpjtxtInput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjtxtInput_file.setObjectName(_fromUtf8("rpjtxtInput_file"))
        self.gridLayout_4.addWidget(self.rpjtxtInput_file, 1, 1, 1, 1)
        self.rpjtxtGCP1_file = QtGui.QLineEdit(self.tab_3)
        self.rpjtxtGCP1_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjtxtGCP1_file.setObjectName(_fromUtf8("rpjtxtGCP1_file"))
        self.gridLayout_4.addWidget(self.rpjtxtGCP1_file, 4, 1, 1, 1)
        self.rpjtxtGCP2_file = QtGui.QLineEdit(self.tab_3)
        self.rpjtxtGCP2_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjtxtGCP2_file.setObjectName(_fromUtf8("rpjtxtGCP2_file"))
        self.gridLayout_4.addWidget(self.rpjtxtGCP2_file, 5, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self.tab_3)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_4.addWidget(self.line_4, 3, 0, 1, 2)
        self.rpjtxtOutput = QtGui.QPushButton(self.tab_3)
        self.rpjtxtOutput.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjtxtOutput.setObjectName(_fromUtf8("rpjtxtOutput"))
        self.gridLayout_4.addWidget(self.rpjtxtOutput, 2, 0, 1, 1)
        self.rpjtxtOutput_file = QtGui.QLineEdit(self.tab_3)
        self.rpjtxtOutput_file.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.rpjtxtOutput_file.setObjectName(_fromUtf8("rpjtxtOutput_file"))
        self.gridLayout_4.addWidget(self.rpjtxtOutput_file, 2, 1, 1, 1)
        self.line_5 = QtGui.QFrame(self.tab_3)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_4.addWidget(self.line_5, 9, 0, 1, 2)
        self.line_6 = QtGui.QFrame(self.tab_3)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_4.addWidget(self.line_6, 6, 0, 1, 2)
        self.line_7 = QtGui.QFrame(self.tab_3)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_4.addWidget(self.line_7, 0, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.rpjtxtConforme = QtGui.QRadioButton(self.tab_3)
        self.rpjtxtConforme.setObjectName(_fromUtf8("rpjtxtConforme"))
        self.horizontalLayout_6.addWidget(self.rpjtxtConforme)
        self.rpjtxtAffine = QtGui.QRadioButton(self.tab_3)
        self.rpjtxtAffine.setChecked(True)
        self.rpjtxtAffine.setObjectName(_fromUtf8("rpjtxtAffine"))
        self.horizontalLayout_6.addWidget(self.rpjtxtAffine)
        self.rpjtxtHelmert = QtGui.QRadioButton(self.tab_3)
        self.rpjtxtHelmert.setObjectName(_fromUtf8("rpjtxtHelmert"))
        self.horizontalLayout_6.addWidget(self.rpjtxtHelmert)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 8, 0, 1, 2)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 642, 206))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_6.addWidget(self.textBrowser)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.addWidget(self.scrollArea_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.rpjtxtGo = QtGui.QPushButton(self.tab_3)
        self.rpjtxtGo.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.rpjtxtGo.setObjectName(_fromUtf8("rpjtxtGo"))
        self.horizontalLayout_5.addWidget(self.rpjtxtGo)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.Go.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.openFileNameButton = QtGui.QPushButton(self.tab_5)
        self.openFileNameButton.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.openFileNameButton.setObjectName(_fromUtf8("openFileNameButton"))
        self.gridLayout_5.addWidget(self.openFileNameButton, 0, 0, 1, 1)
        self.saveFileNameButton = QtGui.QPushButton(self.tab_5)
        self.saveFileNameButton.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.saveFileNameButton.setObjectName(_fromUtf8("saveFileNameButton"))
        self.gridLayout_5.addWidget(self.saveFileNameButton, 2, 0, 1, 1)
        self.openFileNameLabel = QtGui.QLineEdit(self.tab_5)
        self.openFileNameLabel.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.openFileNameLabel.setObjectName(_fromUtf8("openFileNameLabel"))
        self.gridLayout_5.addWidget(self.openFileNameLabel, 0, 1, 1, 1)
        self.saveFileNameLabel = QtGui.QLineEdit(self.tab_5)
        self.saveFileNameLabel.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.saveFileNameLabel.setObjectName(_fromUtf8("saveFileNameLabel"))
        self.gridLayout_5.addWidget(self.saveFileNameLabel, 2, 1, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.sdRadioButton = QtGui.QRadioButton(self.tab_5)
        self.sdRadioButton.setChecked(True)
        self.sdRadioButton.setObjectName(_fromUtf8("sdRadioButton"))
        self.horizontalLayout_7.addWidget(self.sdRadioButton)
        self.dsRadioButton = QtGui.QRadioButton(self.tab_5)
        self.dsRadioButton.setObjectName(_fromUtf8("dsRadioButton"))
        self.horizontalLayout_7.addWidget(self.dsRadioButton)
        self.srRadioButton = QtGui.QRadioButton(self.tab_5)
        self.srRadioButton.setObjectName(_fromUtf8("srRadioButton"))
        self.horizontalLayout_7.addWidget(self.srRadioButton)
        self.rsRadioButton = QtGui.QRadioButton(self.tab_5)
        self.rsRadioButton.setObjectName(_fromUtf8("rsRadioButton"))
        self.horizontalLayout_7.addWidget(self.rsRadioButton)
        self.drRadioButton = QtGui.QRadioButton(self.tab_5)
        self.drRadioButton.setObjectName(_fromUtf8("drRadioButton"))
        self.horizontalLayout_7.addWidget(self.drRadioButton)
        self.rdRadioButton = QtGui.QRadioButton(self.tab_5)
        self.rdRadioButton.setObjectName(_fromUtf8("rdRadioButton"))
        self.horizontalLayout_7.addWidget(self.rdRadioButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 7, 0, 1, 2)
        self.line_16 = QtGui.QFrame(self.tab_5)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.gridLayout_5.addWidget(self.line_16, 1, 0, 1, 2)
        self.line_18 = QtGui.QFrame(self.tab_5)
        self.line_18.setFrameShape(QtGui.QFrame.HLine)
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_18.setObjectName(_fromUtf8("line_18"))
        self.gridLayout_5.addWidget(self.line_18, 3, 0, 1, 2)
        self.line_17 = QtGui.QFrame(self.tab_5)
        self.line_17.setFrameShape(QtGui.QFrame.HLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.gridLayout_5.addWidget(self.line_17, 6, 0, 1, 2)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab_5)
        self.lineEdit.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_6.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 0, 2, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.tab_5)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_2, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 4, 0, 1, 2)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.convert = QtGui.QPushButton(self.tab_5)
        self.convert.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.convert.setObjectName(_fromUtf8("convert"))
        self.horizontalLayout_10.addWidget(self.convert)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 9, 0, 1, 2)
        self.line_19 = QtGui.QFrame(self.tab_5)
        self.line_19.setFrameShape(QtGui.QFrame.HLine)
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_19.setObjectName(_fromUtf8("line_19"))
        self.gridLayout_5.addWidget(self.line_19, 8, 0, 1, 2)
        self.verticalLayout_8.addLayout(self.gridLayout_5)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.Go.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.Go)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(VectorOpsWindow)
        self.Go.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VectorOpsWindow)

    def retranslateUi(self, VectorOpsWindow):
        VectorOpsWindow.setWindowTitle(QtGui.QApplication.translate("VectorOpsWindow", "Vector Operations", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjshpInput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjshpOutput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjGCP2.setText(QtGui.QApplication.translate("VectorOpsWindow", "GCP-2", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjGCP1.setText(QtGui.QApplication.translate("VectorOpsWindow", "GCP-1", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjConforme.setText(QtGui.QApplication.translate("VectorOpsWindow", "Conforme", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjAffine.setText(QtGui.QApplication.translate("VectorOpsWindow", "Affine", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("VectorOpsWindow", "SRS", None, QtGui.QApplication.UnicodeUTF8))
        self.setsrs.setItemText(0, QtGui.QApplication.translate("VectorOpsWindow", "EPSG CODE", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjGo.setText(QtGui.QApplication.translate("VectorOpsWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.Go.setTabText(self.Go.indexOf(self.tab), QtGui.QApplication.translate("VectorOpsWindow", "SHP-Reprojection", None, QtGui.QApplication.UnicodeUTF8))
        self.trshpInput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.trshpOutput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("VectorOpsWindow", "Tx", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("VectorOpsWindow", "Ty", None, QtGui.QApplication.UnicodeUTF8))
        self.trGo.setText(QtGui.QApplication.translate("VectorOpsWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.Go.setTabText(self.Go.indexOf(self.tab_2), QtGui.QApplication.translate("VectorOpsWindow", "SHP-Traslate", None, QtGui.QApplication.UnicodeUTF8))
        self.rotshpInput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.rotshpOutput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("VectorOpsWindow", "Angle", None, QtGui.QApplication.UnicodeUTF8))
        self.rotGo.setText(QtGui.QApplication.translate("VectorOpsWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.Go.setTabText(self.Go.indexOf(self.tab_4), QtGui.QApplication.translate("VectorOpsWindow", "SHP-Rotate", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtInput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtGCP1.setText(QtGui.QApplication.translate("VectorOpsWindow", "GCP-1", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtGCP2.setText(QtGui.QApplication.translate("VectorOpsWindow", "GCP-2", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtOutput.setText(QtGui.QApplication.translate("VectorOpsWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtConforme.setText(QtGui.QApplication.translate("VectorOpsWindow", "Conforme - 4p", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtAffine.setText(QtGui.QApplication.translate("VectorOpsWindow", "Affine - 6p", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtHelmert.setText(QtGui.QApplication.translate("VectorOpsWindow", "Helmert - 7p", None, QtGui.QApplication.UnicodeUTF8))
        self.rpjtxtGo.setText(QtGui.QApplication.translate("VectorOpsWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.Go.setTabText(self.Go.indexOf(self.tab_3), QtGui.QApplication.translate("VectorOpsWindow", "TXT-Reprojection", None, QtGui.QApplication.UnicodeUTF8))
        self.openFileNameButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.saveFileNameButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.sdRadioButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "S - D", None, QtGui.QApplication.UnicodeUTF8))
        self.dsRadioButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "D - S", None, QtGui.QApplication.UnicodeUTF8))
        self.srRadioButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "S - R", None, QtGui.QApplication.UnicodeUTF8))
        self.rsRadioButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "R - S", None, QtGui.QApplication.UnicodeUTF8))
        self.drRadioButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "D - R", None, QtGui.QApplication.UnicodeUTF8))
        self.rdRadioButton.setText(QtGui.QApplication.translate("VectorOpsWindow", "R - D", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("VectorOpsWindow", "Field separator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("VectorOpsWindow", "Degrees notation", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("VectorOpsWindow", "DDD MM SS.SSSS (Space Notation)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("VectorOpsWindow", "DDDdMM\'SSS.SS\"H (Proj Notation)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("VectorOpsWindow", "DDD:MM:SSS.SSSH (Grass Notation)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("VectorOpsWindow", "° \' \'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.convert.setText(QtGui.QApplication.translate("VectorOpsWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.Go.setTabText(self.Go.indexOf(self.tab_5), QtGui.QApplication.translate("VectorOpsWindow", "Degrees Converter", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
