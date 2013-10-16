#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_vardialog import Ui_VarDialog
import os




apppath = os.path.abspath(os.path.dirname(sys.argv[0]))
imagepath = '%s/icons/' % (apppath)
filem = '%s/conf/filem.conf' % (apppath)
configfile = '%s/conf/conf.xml' % (apppath)


from functools import partial

class VarSettings(QDialog, Ui_VarDialog):
    def __init__(self, _ncvarlist, _reqdict):
        QDialog.__init__(self)
        self.setupUi(self)
        self.outdict = _reqdict
        self.cmbList = dict()
        for k in _reqdict.keys():
            self.cmbBox = QComboBox()
            #self.cmbBox.setObjectName(k)
            ##print k
            self.cmbList[k] = self.cmbBox
            #w = 0
            #self.connect(self.cmbBox, SIGNAL('currentIndexChanged(int)'), self.OnCmbBoxChanged())

            #self.bind(self.cmbBox, key=k)

        #sys.exit(1)    
        ##print 'done'
        row  = 0    
        for k in _reqdict.keys():
            self.cmbList[k].setObjectName(k)
            self.cmbList[k].addItem('--select-' + k + '-var--')
            for val in _ncvarlist:
                self.cmbList[k].addItem(val)
                
            self.cmbList[k].currentIndexChanged.connect(self.OnCmbBoxChanged)
            

            self.gridLayout.addWidget(QLabel(k),row,0)
            self.gridLayout.addWidget(self.cmbList[k],row,1)
            
            row = row + 1

    def OnCmbBoxChanged(self, *args):
        obj = str(self.sender().objectName())
        #print obj
        #print self.cmbList[obj].currentText()
        
        self.outdict[obj] = str(self.cmbList[obj].currentText())
     
    def getSettings(self, key):
        #print self.outdict
        return self.outdict[key]
        """
        self.polygoncolor.clicked.connect(self.setVectorPolygonColor)
        self.linecolor.clicked.connect(self.setVectorLineColor)
        self.buttonBox.accepted.connect(self.accept)

    def getVar(self, key):
        if key == 'extrudetype':
            return self.ExtrudeType.currentText()
        elif key == 'tesselate':
            if self.Tessellate.isChecked():
                return 1                  
            else:
                return 0
        elif key == 'extrude':
            if self.Extrude.isChecked():
                return 1                  
            else:
                return 0                

            
    def setVectorPolygonColor(self):
        VectorPolygonColor = QColorDialog.getColor()
        self.VectorPolygonColorName = VectorPolygonColor.name()
        if VectorPolygonColor.isValid():
            self.polygoncolorlabel.setStyleSheet("QWidget { background-color: %s }" % VectorPolygonColor.name() )

    def setVectorLineColor(self):
        VectorLineColor = QColorDialog.getColor()
        self.VectorLineColorName = VectorLineColor.name()
        if VectorLineColor.isValid():
            self.linecolorlabel.setStyleSheet("QWidget { background-color: %s }" % VectorLineColor.name() )    

        """                 
