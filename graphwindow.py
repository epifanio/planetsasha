#!/usr/bin/env python
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class GraphWindow(QtGui.QWidget):

    def __init__(self, parent = None):
    
        QtGui.QWidget.__init__(self, parent)
        self.setupUi()
        self.retranslateUi()
        
        
    def setupUi(self):
        
        self.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.Satellite = QtGui.QTextBrowser(self)
        self.Satellite.setObjectName(_fromUtf8("Satellite"))
        self.verticalLayout_11.addWidget(self.Satellite)
        
    def retranslateUi(self):
        x=1
            
