#!/usr/bin/env python

import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_ossimwindow import Ui_OssimWindow

import xml.etree.ElementTree as et


class OssimWindow(QWidget, Ui_OssimWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.cbApps.currentIndexChanged.connect(self.onSelectApp)
        
    def onSelectApp(self):
        
        aindex = self.cbApps.currentIndex()
        appname = self.cbApps.currentText()
        XML_PATH = './conf/xml/'
        xml  = XML_PATH + appname + '.xml'
        print xml
        
        tree = et.parse(xml)
        root = tree.getroot()
        
        #print root
        lst = root.findall('param')
        #print len(lst)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(lst))
        self.row = 0
        lst = None
        
        #param = root.getChild(0)
        for param in root.iter('param'):
            
            if param.attrib['type'] == 'option':
                self.addOption(param)
            elif param.attrib['type'] == 'input':
                self.addInput(param)
            
        
    def addOption(self, param):
        #print 'option'
        #print param.find('name').text
        #self.tableWidget.clear()
        
        #print self.row
        item = QTableWidgetItem()
        item.setText(param.find('name').text)
        self.tableWidget.setVerticalHeaderItem(self.row, item)        
        item = QTableWidgetItem()
        value = param.find('value').text
        if value is None:
            item.setText(' ')
        else:
            item.setText(value)    
        self.tableWidget.setItem(self.row, 0, item)
        

        item = QTableWidgetItem()
        descr = param.find('descr').text
        if descr is None:
            item.setText(' ')
        else:
            item.setText(descr)    
        self.tableWidget.setItem(self.row, 1, item)
                
        self.row = self.row + 1
        
        
    def addInput(self, param):
        print 'input'  
        
        pnameItem = QTableWidgetItem()
        pnameItem.setText(param.find('name').text)
        self.tableWidget.setVerticalHeaderItem(self.row, pnameItem)        
        pvalItem = QTableWidgetItem()
        value = param.find('value').text
        if value is None:
            pvalItem.setText(' ')
        else:
            pvalItem.setText(value)    
        self.tableWidget.setItem(self.row, 0, pvalItem)
        

        pdescrItem = QTableWidgetItem()
        descr = param.find('descr').text
        if descr is None:
            pdescrItem.setText(' ')
        else:
            pdescrItem.setText(descr)    
        self.tableWidget.setItem(self.row, 1, pdescrItem)
                
        self.row = self.row + 1          
