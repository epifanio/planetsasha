#!/usr/bin/env python
import os
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from layerlistwindow import LayerListWindow

from gen.ui_querywindow import Ui_QueryWindow

class QueryWindow(QWidget, Ui_QueryWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setLayout(self.verticalLayout_2)
        self.layerTable.setColumnWidth(0,200)   
        
        #FIXME sender not found self.connect(self.refreshlayerlist, SIGNAL("clicked()"), self.refreshlayer)
        #FIXME self.connect(self.refreshlayerlist, SIGNAL("clicked()"), self.showrenderoptions)
        self.connect(self.btnAddRast, SIGNAL("clicked()"), self.showRasterLayerList)
        self.connect(self.btnAddVect, SIGNAL("clicked()"), self.showVectorLayerList)


        #FIXME self.connect(self.btnDelRast, SIGNAL("clicked()"), self.removeraster)
        #FIXME self.connect(self.btnDelVect, SIGNAL("clicked()"), self.removevector)        

    def showRasterLayerList(self):
        self.layerlistwin = LayerListWindow('raster')
        self.layerlistwin.btnDone.clicked.connect(self.onAddLayers)
        self.layerlistwin.show()

    def showVectorLayerList(self):
        self.layerlistwin = LayerListWindow('vector')
        self.layerlistwin.btnDone.clicked.connect(self.onAddLayers)
        self.layerlistwin.show() 

    @pyqtSlot(QModelIndex)
    def onAddLayers(self):
        self.slayers = self.layerlistwin.getSelected()
        self.layerTable.setColumnCount(1)
        rows = self.layerTable.rowCount() + len(self.slayers)
        row = self.layerTable.rowCount()
        self.layerTable.setRowCount(rows)
        for l in self.slayers:
            item = QTableWidgetItem(l)
            item.setTextAlignment(Qt.AlignCenter)
            item.setCheckState(Qt.Unchecked)
            
            self.layerTable.setItem(row, 0, item)
            row = row + 1

