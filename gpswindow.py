#!/usr/bin/env python
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
from mapwindow import MapWindow
from graphwindow import GraphWindow
    
class GpsWindow(QtGui.QTabWidget):
    def __init__(self, parent = None):
    
        QtGui.QWidget.__init__(self,parent)
        self.setupUi()
        self.retranslateUi()
        self.tabWidget_2.setCurrentIndex(1)
        
    def connectSignals(self):
        x=1
                
    def setupUi(self):        
        self.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.GpsGroupBox_2 = QtGui.QGroupBox(self.splitter)
        self.GpsGroupBox_2.setTitle(_fromUtf8(""))
        self.GpsGroupBox_2.setObjectName(_fromUtf8("GpsGroupBox_2"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.GpsGroupBox_2)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.tabWidget_2 = QtGui.QTabWidget(self.GpsGroupBox_2)
        self.tabWidget_2.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget_2.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        
        self.mWindow = MapWindow(self)

        self.tabWidget_2.addTab(self.mWindow, _fromUtf8("Map"))    

        self.gWindow = GraphWindow(self)
        self.tabWidget_2.addTab(self.gWindow, _fromUtf8("Graph"))

        self.verticalLayout_17.addWidget(self.tabWidget_2)
        
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.Latlabel_2 = QtGui.QLabel(self.GpsGroupBox_2)
        self.Latlabel_2.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Latlabel_2.setObjectName(_fromUtf8("Latlabel_2"))
        self.gridLayout_6.addWidget(self.Latlabel_2, 0, 0, 1, 1)
        self.Lonlabel_2 = QtGui.QLabel(self.GpsGroupBox_2)
        self.Lonlabel_2.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Lonlabel_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.Lonlabel_2.setFrameShadow(QtGui.QFrame.Plain)
        self.Lonlabel_2.setObjectName(_fromUtf8("Lonlabel_2"))
        self.gridLayout_6.addWidget(self.Lonlabel_2, 0, 2, 1, 1)
        self.GPSlon_2 = QtGui.QLineEdit(self.GpsGroupBox_2)
        self.GPSlon_2.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""))
        self.GPSlon_2.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSlon_2.setReadOnly(True)
        self.GPSlon_2.setObjectName(_fromUtf8("GPSlon_2"))
        self.gridLayout_6.addWidget(self.GPSlon_2, 0, 3, 1, 1)
        self.GPSlat_2 = QtGui.QLineEdit(self.GpsGroupBox_2)
        self.GPSlat_2.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""))
        self.GPSlat_2.setEchoMode(QtGui.QLineEdit.Normal)
        self.GPSlat_2.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSlat_2.setReadOnly(True)
        self.GPSlat_2.setObjectName(_fromUtf8("GPSlat_2"))
        self.gridLayout_6.addWidget(self.GPSlat_2, 0, 1, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_6)
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.scrollArea_2 = QtGui.QScrollArea(self.groupBox)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 215, 173))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.scrollArea = QtGui.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 172, 560))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.Datelabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Datelabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Datelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Datelabel.setObjectName(_fromUtf8("Datelabel"))
        self.gridLayout_8.addWidget(self.Datelabel, 0, 0, 1, 1)
        self.GPSTime = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSTime.setAutoFillBackground(False)
        self.GPSTime.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSTime.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSTime.setReadOnly(True)
        self.GPSTime.setObjectName(_fromUtf8("GPSTime"))
        self.gridLayout_8.addWidget(self.GPSTime, 0, 1, 1, 1)
        self.Utclabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Utclabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Utclabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Utclabel.setObjectName(_fromUtf8("Utclabel"))
        self.gridLayout_8.addWidget(self.Utclabel, 1, 0, 1, 1)
        self.GPSUtctime = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSUtctime.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSUtctime.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSUtctime.setReadOnly(True)
        self.GPSUtctime.setObjectName(_fromUtf8("GPSUtctime"))
        self.gridLayout_8.addWidget(self.GPSUtctime, 1, 1, 1, 1)
        self.Altitudelabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Altitudelabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Altitudelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Altitudelabel.setObjectName(_fromUtf8("Altitudelabel"))
        self.gridLayout_8.addWidget(self.Altitudelabel, 2, 0, 1, 1)
        self.GPSAltitude = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSAltitude.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSAltitude.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSAltitude.setReadOnly(True)
        self.GPSAltitude.setObjectName(_fromUtf8("GPSAltitude"))
        self.gridLayout_8.addWidget(self.GPSAltitude, 2, 1, 1, 1)
        self.Speedlabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Speedlabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Speedlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Speedlabel.setObjectName(_fromUtf8("Speedlabel"))
        self.gridLayout_8.addWidget(self.Speedlabel, 3, 0, 1, 1)
        self.GPSSpeed = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSSpeed.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSSpeed.setReadOnly(True)
        self.GPSSpeed.setObjectName(_fromUtf8("GPSSpeed"))
        self.gridLayout_8.addWidget(self.GPSSpeed, 3, 1, 1, 1)
        self.Climblabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Climblabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Climblabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Climblabel.setObjectName(_fromUtf8("Climblabel"))
        self.gridLayout_8.addWidget(self.Climblabel, 5, 0, 1, 1)
        self.GPSClimb = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSClimb.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSClimb.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSClimb.setReadOnly(True)
        self.GPSClimb.setObjectName(_fromUtf8("GPSClimb"))
        self.gridLayout_8.addWidget(self.GPSClimb, 5, 1, 1, 1)
        self.Pdoplabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Pdoplabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Pdoplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Pdoplabel.setObjectName(_fromUtf8("Pdoplabel"))
        self.gridLayout_8.addWidget(self.Pdoplabel, 6, 0, 1, 1)
        self.GPSPdop = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSPdop.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSPdop.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSPdop.setReadOnly(True)
        self.GPSPdop.setObjectName(_fromUtf8("GPSPdop"))
        self.gridLayout_8.addWidget(self.GPSPdop, 6, 1, 1, 1)
        self.Hdoplabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Hdoplabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Hdoplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Hdoplabel.setObjectName(_fromUtf8("Hdoplabel"))
        self.gridLayout_8.addWidget(self.Hdoplabel, 7, 0, 1, 1)
        self.GPSHdop = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSHdop.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSHdop.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSHdop.setReadOnly(True)
        self.GPSHdop.setObjectName(_fromUtf8("GPSHdop"))
        self.gridLayout_8.addWidget(self.GPSHdop, 7, 1, 1, 1)
        self.Vdoplabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Vdoplabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Vdoplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Vdoplabel.setObjectName(_fromUtf8("Vdoplabel"))
        self.gridLayout_8.addWidget(self.Vdoplabel, 8, 0, 1, 1)
        self.GPSVdop = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSVdop.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSVdop.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSVdop.setReadOnly(True)
        self.GPSVdop.setObjectName(_fromUtf8("GPSVdop"))
        self.gridLayout_8.addWidget(self.GPSVdop, 8, 1, 1, 1)
        self.Tdoplabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Tdoplabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Tdoplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Tdoplabel.setObjectName(_fromUtf8("Tdoplabel"))
        self.gridLayout_8.addWidget(self.Tdoplabel, 9, 0, 1, 1)
        self.GPSTdop = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSTdop.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSTdop.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSTdop.setReadOnly(True)
        self.GPSTdop.setObjectName(_fromUtf8("GPSTdop"))
        self.gridLayout_8.addWidget(self.GPSTdop, 9, 1, 1, 1)
        self.Gdoplabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Gdoplabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Gdoplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Gdoplabel.setObjectName(_fromUtf8("Gdoplabel"))
        self.gridLayout_8.addWidget(self.Gdoplabel, 10, 0, 1, 1)
        self.GPSGdop = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSGdop.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSGdop.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSGdop.setReadOnly(True)
        self.GPSGdop.setObjectName(_fromUtf8("GPSGdop"))
        self.gridLayout_8.addWidget(self.GPSGdop, 10, 1, 1, 1)
        self.Ephlabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Ephlabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Ephlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Ephlabel.setObjectName(_fromUtf8("Ephlabel"))
        self.gridLayout_8.addWidget(self.Ephlabel, 11, 0, 1, 1)
        self.GPSEph = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSEph.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSEph.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSEph.setReadOnly(True)
        self.GPSEph.setObjectName(_fromUtf8("GPSEph"))
        self.gridLayout_8.addWidget(self.GPSEph, 11, 1, 1, 1)
        self.Eptlabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Eptlabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Eptlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Eptlabel.setObjectName(_fromUtf8("Eptlabel"))
        self.gridLayout_8.addWidget(self.Eptlabel, 12, 0, 1, 1)
        self.GPSEpt = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSEpt.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSEpt.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSEpt.setReadOnly(True)
        self.GPSEpt.setObjectName(_fromUtf8("GPSEpt"))
        self.gridLayout_8.addWidget(self.GPSEpt, 12, 1, 1, 1)
        self.Epslabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Epslabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Epslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Epslabel.setObjectName(_fromUtf8("Epslabel"))
        self.gridLayout_8.addWidget(self.Epslabel, 13, 0, 1, 1)
        self.GPSEps = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSEps.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSEps.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSEps.setReadOnly(True)
        self.GPSEps.setObjectName(_fromUtf8("GPSEps"))
        self.gridLayout_8.addWidget(self.GPSEps, 13, 1, 1, 1)
        self.Epvlabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Epvlabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Epvlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Epvlabel.setObjectName(_fromUtf8("Epvlabel"))
        self.gridLayout_8.addWidget(self.Epvlabel, 14, 0, 1, 1)
        self.GPSEpv = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSEpv.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSEpv.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSEpv.setReadOnly(True)
        self.GPSEpv.setObjectName(_fromUtf8("GPSEpv"))
        self.gridLayout_8.addWidget(self.GPSEpv, 14, 1, 1, 1)
        self.Epdlabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Epdlabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Epdlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Epdlabel.setObjectName(_fromUtf8("Epdlabel"))
        self.gridLayout_8.addWidget(self.Epdlabel, 15, 0, 1, 1)
        self.GPSEpd = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSEpd.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSEpd.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSEpd.setReadOnly(True)
        self.GPSEpd.setObjectName(_fromUtf8("GPSEpd"))
        self.gridLayout_8.addWidget(self.GPSEpd, 15, 1, 1, 1)
        self.Epclabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Epclabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Epclabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Epclabel.setObjectName(_fromUtf8("Epclabel"))
        self.gridLayout_8.addWidget(self.Epclabel, 16, 0, 1, 1)
        self.GPSEpc = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSEpc.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSEpc.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSEpc.setReadOnly(True)
        self.GPSEpc.setObjectName(_fromUtf8("GPSEpc"))
        self.gridLayout_8.addWidget(self.GPSEpc, 16, 1, 1, 1)
        self.GPSTrack = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.GPSTrack.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
"\n"
"\n"
"\n"
""))
        self.GPSTrack.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSTrack.setReadOnly(True)
        self.GPSTrack.setObjectName(_fromUtf8("GPSTrack"))
        self.gridLayout_8.addWidget(self.GPSTrack, 4, 1, 1, 1)
        self.Tracklabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.Tracklabel.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Tracklabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Tracklabel.setObjectName(_fromUtf8("Tracklabel"))
        self.gridLayout_8.addWidget(self.Tracklabel, 4, 0, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.GPSSend = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.GPSSend.setStyleSheet(_fromUtf8(""))
        self.GPSSend.setObjectName(_fromUtf8("GPSSend"))
        self.horizontalLayout_9.addWidget(self.GPSSend)
        self.StartGps = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.StartGps.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
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
        self.StartGps.setCheckable(True)
        self.StartGps.setObjectName(_fromUtf8("StartGps"))
        self.horizontalLayout_9.addWidget(self.StartGps)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_15.addWidget(self.scrollArea_2)
        self.verticalLayout_16.addWidget(self.splitter)
        
    def retranslateUi(self):
    
        self.Latlabel_2.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Lat", None, QtGui.QApplication.UnicodeUTF8))
        self.Lonlabel_2.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Lon", None, QtGui.QApplication.UnicodeUTF8))
        self.Datelabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.Utclabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "UTC", None, QtGui.QApplication.UnicodeUTF8))
        self.Altitudelabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Altitude", None, QtGui.QApplication.UnicodeUTF8))
        self.Speedlabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.Climblabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Climb", None, QtGui.QApplication.UnicodeUTF8))
        self.Pdoplabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Pdop", None, QtGui.QApplication.UnicodeUTF8))
        self.Hdoplabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Hdop", None, QtGui.QApplication.UnicodeUTF8))
        self.Vdoplabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Vdop", None, QtGui.QApplication.UnicodeUTF8))
        self.Tdoplabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Tdop", None, QtGui.QApplication.UnicodeUTF8))
        self.Gdoplabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Gdop", None, QtGui.QApplication.UnicodeUTF8))
        self.Ephlabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Eph", None, QtGui.QApplication.UnicodeUTF8))
        self.Eptlabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Ept", None, QtGui.QApplication.UnicodeUTF8))
        self.Epslabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Eps", None, QtGui.QApplication.UnicodeUTF8))
        self.Epvlabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Epv", None, QtGui.QApplication.UnicodeUTF8))
        self.Epdlabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Epd", None, QtGui.QApplication.UnicodeUTF8))
        self.Epclabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Epc", None, QtGui.QApplication.UnicodeUTF8))
        self.Tracklabel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Track", None, QtGui.QApplication.UnicodeUTF8))
        self.GPSSend.setText(QtGui.QApplication.translate("OssimPlanetSasha", "SendPosition", None, QtGui.QApplication.UnicodeUTF8))
        self.StartGps.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Start/Stop ", None, QtGui.QApplication.UnicodeUTF8))    
