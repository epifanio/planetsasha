#!/usr/bin/env python

import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_ossimwindow import Ui_OssimWindow


class OssimWindow(QWidget, Ui_OssimWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.cbApps.currentIndexChanged.connect(self.onSelectApp)
        
    def onSelectApp(self):
        
        aindex = self.cbApps.currentIndex()
        appname = self.cbApps.currentText()
        XML_PATH = './xml/'
        xml  = XML_PATH + appname + '.xml'
        print xml
        
        tree = et.parse(xml)
        root = tree.getroot()
        
        #print 'Fetching data from ' + url
        for dataset in root.iter('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset'):
            
            dsname = dataset.get('name')
            #dataset.get('ID')
            urlPath = dataset.get('urlPath')
            if urlPath is not None:
                item = QStandardItem(dsname)
                item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)  
                if rootItem is None:
                   self.model.appendRow(item)
                else:
                    rootItem.appendRow(item)
         
                        
        for catalogref in root.iter('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef'):
            href = catalogref.get('{http://www.w3.org/1999/xlink}href')
            title = catalogref.get('{http://www.w3.org/1999/xlink}title')
            
            if href is None:
                return  #FIXME needs testing and may need to change to continue or break
            
            url_key = ''
            if rootItem:
                prev = self.xmlMap[str(rootItem.text())]
                
                prev = prev.rsplit('/',1)[0]
                if href.startswith('/thredds'):
                    url_key = prev + '/' + href[8:]
                else:
                    url_key = prev + '/' + href   
            else:
                if not href.startswith('/thredds'):
                    url_key = self.url_base + '/thredds/' + href
                else:
                    url_key = self.url_base + href        
