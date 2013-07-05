#!/usr/bin/env python
import os
import sys
import platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gen.ui_layerlistwindow import Ui_LayerListWindow

from psinit import *

class LayerListWindow(QWidget, Ui_LayerListWindow):
    def __init__(self,t, parent = None):
        QWidget.__init__(self, parent)
        self.type = t

        #self.rasterpath = os.path.join(getEnv()['GISDBASE'],getEnv()['LOCATION_NAME'],getEnv()['MAPSET'],'cellhd/')
        #self.vectorpath = os.path.join(getEnv()['GISDBASE'],getEnv()['LOCATION_NAME'],getEnv()['MAPSET'],'vector/')
        self.setupUi(self)
        
        self.type = t
        self.model = QStandardItemModel(self)

        self.vectList = []
        self.rastList = []
        self.selectedLayer = None
        self.model.insertColumn(0,[QStandardItem('click fetch..')])
        self.lstLayers.setModel(self.model)

        if t == 'raster':
            self.setWindowTitle('Select raster layer')
        elif t == 'vector':
            self.setWindowTitle('Select vector layer')

        self.connect(self.btnFetch, SIGNAL("clicked()"), self.populateListModel)
        self.connect(self.txtSearch, SIGNAL("textChanged(QString )"), self.filterListModel)
        self.connect(self.btnDone, SIGNAL("clicked()"), self.done)
        
    def getSelected(self):
        lst = []
        for i in self.lstLayers.selectedIndexes():
            lst.append(self.model.itemFromIndex(i).text())       
        return lst
    
    def filterListModel(self):
        self.model.clear()
        li = self.updateModel(self.type, pattern = self.txtSearch.text())
        self.model.insertColumn(0, li)
        
    def populateListModel(self):
        self.model.clear()
        if self.type == 'raster':
            self.rastList = getLayerList('rast')

        elif self.type == 'vector':
            self.vectList = getLayerList('vect')

            
        li = self.updateModel(self.type)
        if len(li) > 1:
            self.model.insertColumn(0,li)
        else:
            self.model.insertColumn(0,[QStandardItem('No Data..')])
            
    def updateModel(self, ltype, pattern='*'):
        lst = list()
        if ltype == 'raster':
            for name in self.rastList:
                if pattern == '*':
                    item = QStandardItem(name)
                    item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
                    lst.append(item)
                else:
                    if name.startswith(pattern):
                        item = QStandardItem(name)
                        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
                        lst.append(item)
                        
        elif ltype == 'vector':
            for name in self.vectList:
                if pattern == '*':
                        item = QStandardItem(name)
                        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
                        lst.append(item)
                else:
                    if name.startswith(pattern):
                        item = QStandardItem(name)
                        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
                        lst.append(item)
        return lst

    def done(self):
        self.close()
