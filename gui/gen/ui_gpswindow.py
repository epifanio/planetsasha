# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gpswindow.ui'
#
# Created: Sat Jul  6 14:09:26 2013
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

class Ui_GpsWindow(object):
    def setupUi(self, GpsWindow):
        GpsWindow.setObjectName(_fromUtf8("GpsWindow"))
        GpsWindow.resize(877, 691)
        self.layoutWidget = QtGui.QWidget(GpsWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 20, 809, 610))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(30)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab_7)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.WebMap = QtWebKit.QWebView(self.tab_7)
        self.WebMap.setProperty("url", QtCore.QUrl(_fromUtf8("about:blank")))
        self.WebMap.setObjectName(_fromUtf8("WebMap"))
        self.verticalLayout_10.addWidget(self.WebMap)
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_8)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.tabWidget)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.GPSSend = QtGui.QCheckBox(self.layoutWidget)
        self.GPSSend.setStyleSheet(_fromUtf8(""))
        self.GPSSend.setObjectName(_fromUtf8("GPSSend"))
        self.gridLayout_8.addWidget(self.GPSSend, 17, 0, 1, 1)
        self.Datelabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSTime = QtGui.QLineEdit(self.layoutWidget)
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
        self.Utclabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSUtctime = QtGui.QLineEdit(self.layoutWidget)
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
        self.Altitudelabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSAltitude = QtGui.QLineEdit(self.layoutWidget)
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
        self.Speedlabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSSpeed = QtGui.QLineEdit(self.layoutWidget)
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
        self.Climblabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSClimb = QtGui.QLineEdit(self.layoutWidget)
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
        self.Pdoplabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSPdop = QtGui.QLineEdit(self.layoutWidget)
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
        self.Hdoplabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSHdop = QtGui.QLineEdit(self.layoutWidget)
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
        self.Vdoplabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSVdop = QtGui.QLineEdit(self.layoutWidget)
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
        self.Tdoplabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSTdop = QtGui.QLineEdit(self.layoutWidget)
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
        self.Gdoplabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSGdop = QtGui.QLineEdit(self.layoutWidget)
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
        self.Ephlabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSEph = QtGui.QLineEdit(self.layoutWidget)
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
        self.Eptlabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSEpt = QtGui.QLineEdit(self.layoutWidget)
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
        self.Epslabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSEps = QtGui.QLineEdit(self.layoutWidget)
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
        self.Epvlabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSEpv = QtGui.QLineEdit(self.layoutWidget)
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
        self.Epdlabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSEpd = QtGui.QLineEdit(self.layoutWidget)
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
        self.Epclabel = QtGui.QLabel(self.layoutWidget)
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
        self.GPSEpc = QtGui.QLineEdit(self.layoutWidget)
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
        self.GPSTrack = QtGui.QLineEdit(self.layoutWidget)
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
        self.Tracklabel = QtGui.QLabel(self.layoutWidget)
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
        self.StartGps = QtGui.QPushButton(self.layoutWidget)
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
        self.gridLayout_8.addWidget(self.StartGps, 17, 1, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Latlabel_2 = QtGui.QLabel(self.layoutWidget)
        self.Latlabel_2.setStyleSheet(_fromUtf8(" QFrame, QLabel, QToolTip {\n"
"     border: 1px solid gray;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"     background-image: url(images/welcome.png);\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Latlabel_2.setObjectName(_fromUtf8("Latlabel_2"))
        self.horizontalLayout.addWidget(self.Latlabel_2)
        self.GPSlat = QtGui.QLineEdit(self.layoutWidget)
        self.GPSlat.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""))
        self.GPSlat.setEchoMode(QtGui.QLineEdit.Normal)
        self.GPSlat.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSlat.setReadOnly(True)
        self.GPSlat.setObjectName(_fromUtf8("GPSlat"))
        self.horizontalLayout.addWidget(self.GPSlat)
        self.Lonlabel_2 = QtGui.QLabel(self.layoutWidget)
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
        self.horizontalLayout.addWidget(self.Lonlabel_2)
        self.GPSlon = QtGui.QLineEdit(self.layoutWidget)
        self.GPSlon.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""))
        self.GPSlon.setAlignment(QtCore.Qt.AlignCenter)
        self.GPSlon.setReadOnly(True)
        self.GPSlon.setObjectName(_fromUtf8("GPSlon"))
        self.horizontalLayout.addWidget(self.GPSlon)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GpsWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GpsWindow)

    def retranslateUi(self, GpsWindow):
        GpsWindow.setWindowTitle(_translate("GpsWindow", "GPS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("GpsWindow", "Map", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("GpsWindow", "Graph", None))
        self.GPSSend.setText(_translate("GpsWindow", "SendPosition", None))
        self.Datelabel.setText(_translate("GpsWindow", "Date", None))
        self.Utclabel.setText(_translate("GpsWindow", "UTC", None))
        self.Altitudelabel.setText(_translate("GpsWindow", "Altitude", None))
        self.Speedlabel.setText(_translate("GpsWindow", "Speed", None))
        self.Climblabel.setText(_translate("GpsWindow", "Climb", None))
        self.Pdoplabel.setText(_translate("GpsWindow", "Pdop", None))
        self.Hdoplabel.setText(_translate("GpsWindow", "Hdop", None))
        self.Vdoplabel.setText(_translate("GpsWindow", "Vdop", None))
        self.Tdoplabel.setText(_translate("GpsWindow", "Tdop", None))
        self.Gdoplabel.setText(_translate("GpsWindow", "Gdop", None))
        self.Ephlabel.setText(_translate("GpsWindow", "Eph", None))
        self.Eptlabel.setText(_translate("GpsWindow", "Ept", None))
        self.Epslabel.setText(_translate("GpsWindow", "Eps", None))
        self.Epvlabel.setText(_translate("GpsWindow", "Epv", None))
        self.Epdlabel.setText(_translate("GpsWindow", "Epd", None))
        self.Epclabel.setText(_translate("GpsWindow", "Epc", None))
        self.Tracklabel.setText(_translate("GpsWindow", "Track", None))
        self.StartGps.setText(_translate("GpsWindow", "Start/Stop ", None))
        self.Latlabel_2.setText(_translate("GpsWindow", "Lat", None))
        self.Lonlabel_2.setText(_translate("GpsWindow", "Lon", None))

from PyQt4 import QtWebKit
