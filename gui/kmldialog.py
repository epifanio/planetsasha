#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_kmldialog import Ui_KmlDialog
import os




apppath = os.path.abspath(os.path.dirname(sys.argv[0]))
imagepath = '%s/icons/' % (apppath)
filem = '%s/conf/filem.conf' % (apppath)
configfile = '%s/conf/conf.xml' % (apppath)




class KmlSettings(QDialog, Ui_KmlDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.VectorPolygonColorName = "#9da7ff"
        self.VectorLineColorName = "#3eff6b"
        self.polygoncolor.clicked.connect(self.setVectorPolygonColor)
        self.linecolor.clicked.connect(self.setVectorLineColor)
        self.buttonBox.accepted.connect(self.accept)

    def getSettings(self, key):
        if key == 'extrudetype':
            return self.ExtrudeType.currentText()
        elif key == 'lwidth':
            return self.LineWidth.value()
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
        elif key == 'altitudemode':
            return self.AltitudeMode.currentText()
        elif key == 'offset':
            return self.Offset.value()    
        elif key == 'polycolor':
            return self.VectorPolygonColorName           
        elif key == 'linecolor':
            return self.VectorLineColorName
            
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
                       
