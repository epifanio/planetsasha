#!/usr/bin/env python
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
     
class MapWindow(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.setupUi()
        self.retranslateUi()
        
    def setupUi(self):        
        self.setObjectName(_fromUtf8("tab_7"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.WebMap = QtWebKit.QWebView(self)
        self.WebMap.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.WebMap.setObjectName(_fromUtf8("WebMap"))
        self.verticalLayout_10.addWidget(self.WebMap)

    def retranslateUi(self):
        x=1
