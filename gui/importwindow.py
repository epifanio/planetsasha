#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_importwindow import Ui_ImportWindow
import os

import xml.etree.ElementTree as et
import urllib2


class Catalog(object):
    def __init__(self,h,t):
        self.li = list()
        self.href = h
        self.title = t
        
class ImportWindow(QWizard, Ui_ImportWindow):
    GN = 'GeoNetwork'
    GP = 'GeoPortal'
    TH = 'Thredds'
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.resize(752,497)
   	#imgQ = ImageQt.ImageQt(img)
        pixMap = QPixmap.fromImage(QImage("gui/images/qgis_world.png"))

        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)
        pixMap = pixMap.scaled(QSize(400,200))
        scene.addPixmap(pixMap)               
        self.graphicsView.repaint()
        self.graphicsView.show()
        
        self.bboxWidget.setLayout(self.bboxLayout)
        
        self.button(QWizard.NextButton).clicked.connect(self.OnNextPage)
        self.button(QWizard.FinishButton).clicked.connect(self.close)
        self.cmbService.currentIndexChanged.connect(self.toggleBBox)

    def toggleBBox(self):
    
        if self.cmbService.currentIndex() == 1:
            self.bboxWidget.hide()
        else:
            self.bboxWidget.show()
    def validate(self):

        return 0
        
        
    def OnNextPage(self):
        
        url_i = self.cmbUrl.currentIndex()
        type_i = self.cmbType.currentIndex()
        service_i = self.cmbService.currentIndex()
        if url_i < 1 or type_i < 1 or service_i < 1:
            print 'select url, type, service.'
            #return None
            
        self.url_s = self.cmbUrl.currentText()
        self.type_s = self.cmbType.currentText()
        self.service_s = self.cmbService.currentText()
        self.bbox = None
        self.keywords = None
        self.maxrec = None
        self.row = 0
        self.col = 0
        
        self.model = QStandardItemModel(self)

        self.treeView.setModel(self.model)
        
        
        self.type_s = ImportWindow.TH
        
        if self.type_s == ImportWindow.GN:
            self.fetchGNData()
        elif self.type_s == ImportWindow.GP:
            self.fetchGCData()
        if self.type_s == ImportWindow.TH:
            self.fetchTHData()
        
        


    def fetchTHData2(self, url, count = 0, item = None):
        xml= urllib2.urlopen(url)
        tree = et.parse(xml)
        root = tree.getroot()
        
        for elem in root.findall('.'):

            for i in elem.getchildren():
                print i
                href = i.get('{http://www.w3.org/1999/xlink}href')
                title = i.get('{http://www.w3.org/1999/xlink}title')
                
                url2 = ''
                if href is not None:
                    
                    if href.startswith('/thredds'):
                        #print href
                        url2 = 'http://www.smast.umassd.edu:8080' + href
                    else:
                        url2 = 'http://www.smast.umassd.edu:8080/thredds/' + href
                        item = None
                    
                    
                    #print url2 + ':::' + str(self.row)  
                    if item is None:
                        item = QStandardItem(title)
                        self.model.setItem(self.row,0,item)                        
                        self.row = self.row + 1
                        
                    else:

                        item.appendRow(QStandardItem(title))
                        
                    self.fetchTHData2(url2, count + 1, item)

        return
          

    def fetchTHData(self):

        self.fetchTHData2('http://www.smast.umassd.edu:8080/thredds/catalog.xml')

        
        
            
            
        
    def fetchGNData(self):
    
        xml = self.url_s + "/thredds.xml"
        
    def fetchGPData(self):
    
        xml = self.url_s + "/thredds.xml"     
        
    

