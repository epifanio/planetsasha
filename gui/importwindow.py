#!/usr/bin/env python
import os
import sys
import time

#Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#gui
from gen.ui_importwindow import Ui_ImportWindow

#extra
from owslib.csw import CatalogueServiceWeb
import xml.etree.ElementTree as et
import urllib2
import urlparse


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

        self.xmlMap = dict()

        self.debug = 1
        self.url_prefix = '/thredds/'
        
        #self.datac= [][]
   	#imgQ = ImageQt.ImageQt(img)
        pixMap = QPixmap.fromImage(QImage("gui/images/qgis_world.png"))
        self.dslist = []
        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)
        pixMap = pixMap.scaled(QSize(400,200))
        scene.addPixmap(pixMap)               
        self.graphicsView.repaint()
        self.graphicsView.show()

        self.treeView.setEditTriggers(QTreeView.NoEditTriggers)

        self.treeView.setSelectionMode(  QAbstractItemView.ExtendedSelection  )
        
        self.bboxWidget.setLayout(self.bboxLayout)
        #self.treeView.setSelectionMode(QAbstractItemView.MultiSelection)

        self.btAddTo.clicked.connect(self.onAddToList)
        
        self.button(QWizard.NextButton).clicked.connect(self.OnNextPage)
        self.button(QWizard.FinishButton).clicked.connect(self.onClose)
        self.cmbService.currentIndexChanged.connect(self.toggleBBox)
        self.treeView.doubleClicked.connect(self.onSelect)


    def onAddToList(self):
        for index in self.treeView.selectedIndexes():
            item = self.model.itemFromIndex(index)
            if not item.hasChildren() and item.text() != '--Fetch--':
                self.lmodel.appendRow(QStandardItem(item.text()))

    def onSelect(self, index):
        item = self.model.itemFromIndex(index)
        
        if item.text() == '--Fetch--': #PSasha.FETCH_TEXT
            item.setText('Fetching data..')
            pindex = self.model.parent(index)
            pitem = self.model.itemFromIndex(pindex)
            
            ptext  = str(pitem.text())
            urlN = str(self.xmlMap[ptext])
            
            #if not urlN.startswith('/thredds'):
            #    urlN =  self.url_prefix + urlN
            #print urlN
            #print ptext
            
            self.fetchTHData(urlN, pitem)

            #pparent = self.model.itemFromIndex(pindex.parent())
            #if pparent:
            #    print pparent.text() + 'xxxxxxy'
            #    print ptext + 'yyzzz'




            #prefix = urlN.rsplit('/',1)[0]
            ##print prefix
            #if not prefix.endswith('.xml'):
            #    self.url_prefix = prefix + '/'
            #
            #print self.url_prefix
 
            #remove fetching data text...


    def fetchTHData(self, urlnext ='thredds/catalog.xml', rootItem = None):

        #if urlnext.startswith('/thredds'):
        #    url = urlparse.urljoin(self.url_base, urlnext)
        #else:    
        #    url = urlparse.urljoin(self.url_base, '/thredds/' + urlnext)
        if urlnext == 'thredds/catalog.xml':
            url = urlparse.urljoin(self.url_base, urlnext)
        else:    
            url = urlnext
        #print url

        xml = ''
        try:
            xml= urllib2.urlopen(url)
        except:
            print 'error:' + url
            if rootItem is not None:
                rootItem.child(0).setText('?? error ??')
                #TODO show the error on a error window in ui
                return

        tree = et.parse(xml)
        root = tree.getroot()
        
        #print 'Fetching data from ' + url
        if url != '': #FIXME unwanted check
            for elem in root.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset'):
                dsname = elem.get('name')
                #elem.get('ID')
                urlPath = elem.get('urlPath')
                if urlPath is None:
                    for elem in root.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset/{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset'):
                        
                        urlPath = elem.get('urlPath')

                        if urlPath is not None:
                            dsname = elem.get('name') 
                            #print dsname + 'qqqq'
                            item = QStandardItem(dsname)
                            item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)  
                            if rootItem is None:
                                self.model.appendRow(item)
                            else:
                                rootItem.appendRow(item)
                                #self.model.appendRow(rootItem)
                        


        for elem in root.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef') or root.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset/{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef'):
            href = elem.get('{http://www.w3.org/1999/xlink}href')
            title = elem.get('{http://www.w3.org/1999/xlink}title')
            
            if href is None:
                return
            url_next = ''
            url_key = ''

            #print href
            if rootItem:
                prev = self.xmlMap[str(rootItem.text())]
                
                prev = prev.rsplit('/',1)[0]
                if href.startswith('/thredds'):
                    url_key = prev + '/' + href[8:]
                else:
                    url_key = prev + '/' + href   
                print url_key
            else:
                 
                if not href.startswith('/thredds'):
                    url_key = self.url_base + '/thredds/' + href
                    #url_next = self.url_prefix + href.rsplit('/',1)[0]
                else:
                    url_key = self.url_base + href



            #print url_key

            self.xmlMap[title] = url_key
            #if self.debug == 2:
            #print title + "::" + self.xmlMap[title]
               
            item = QStandardItem(title)
            item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)  
            item.appendRow(QStandardItem('--Fetch--'))
            loadIcon = QIcon()
            loadIcon.addPixmap(QPixmap(":/icons/icons/loading.gif"), QIcon.Normal, QIcon.Off)
            item.setIcon(loadIcon)

            if rootItem is None:
                self.model.appendRow(item)
            else:
                rootItem.appendRow(item)
                #self.model.appendRow(rootItem)    

        
        if rootItem is not None:
            rootItem.removeRow(0)


        return

       
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
            
        self.url_s = str(self.cmbUrl.currentText())
        self.type_s = self.cmbType.currentText()
        self.service_s = self.cmbService.currentText()
        self.bbox = None
        self.keywords = None
        self.maxrec = None
        self.row = 0
        self.col = 0
        
        self.model = QStandardItemModel(self)
        self.treeView.setModel(self.model)
 
        self.lmodel = QStandardItemModel(self)
        self.listView.setModel(self.lmodel)
        
        self.type_s = ImportWindow.TH #D code
        self.url_s = 'http://www.smast.umassd.edu:8080/thredds'
        
        
        self.url_base = self.url_s.rsplit('/',1)[0]
        if self.type_s == ImportWindow.GN:
            self.fetchGNData()
        elif self.type_s == ImportWindow.GP:
            self.fetchGCData()
        if self.type_s == ImportWindow.TH:
            self.fetchTHData()


    def fetchTHData2(self, url, count = 0, item = None):        
        base = url.rsplit('/',1)[0]
        #print base
        xml= urllib2.urlopen(url)
        tree = et.parse(xml)
        root = tree.getroot()
    #    for e in root:
    #        print e

        for elem in root.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}dataset/{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef'):
            href = elem.get('{http://www.w3.org/1999/xlink}href')
            title = elem.get('{http://www.w3.org/1999/xlink}title')
            print href
            
            url2 = ''
            if href is not None:

                    url2 = base + '/' + href
                    print url2 + '::yy'
                    #item = None
                    self.fetchTHData2(url2, count + 1, item)    
            
        for elem in root.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef'):
            href = elem.get('{http://www.w3.org/1999/xlink}href')
            title = elem.get('{http://www.w3.org/1999/xlink}title')
            self.xmlMap[title] = href
            
                
            url2 = ''
            if href is not None:
                
                if href.startswith('/thredds'):
                    #print base + '/' + href
                    url2 = 'http://www.smast.umassd.edu:8080' + href
                else:
                    url2 = base + '/' + href

                    item = None
                
                
                print url2 + ':::xx'
                #self.datac.append(url2)
                self.model.appendRow(QStandardItem(url2))
                self.fetchTHData2(url2, count + 1, item)

        return
        
        


    def getResource(self, endpoint = 'http://www.nodc.noaa.gov/geoportal/csw', bbox=None, keywords=None, maxrecords=1, service_type='opendap', verbose=None):
        if service_type == 'opendap':
            service_string='urn:x-esri:specification:ServiceType:OPeNDAP'
        if service_type == 'wms':
            service_string='urn:x-esri:specification:ServiceType:WMS'
        csw = CatalogueServiceWeb(endpoint,timeout=30)
        if keywords is not None:
            csw.getrecords(keywords=keywords, bbox=bbox, maxrecords=maxrecords)
        else :
            csw.getrecords(bbox=bbox, maxrecords=maxrecords)
        csw.records.keys()
        result = {}
        for i in csw.records.keys():
            records=csw.records[i]
            resource = {}
            for key,rec in csw.records.iteritems():
                url = next((d['url'] for d in rec.references if d['scheme'] == service_string), None)
                print rec.references[0]['url']
                if url is not None:
                    resource[rec.title] = url
            result[i] = resource
        if verbose is not None:
            print 'endpoint: ', endpoint, '\n' , 'bbox: ', bbox, '\n' , 'keywords: ', keywords, '\n', 'maxrecords: ', maxrecords , '\n', 'service_type: ' , service_type
        return result

    #endpoint = 'http://www.smast.umassd.edu:8080/thredds/catalog.xml'
    #bbox = [-71.5, 39.5, -63.0, 46]
    #keywords = ['temperature']
    #maxrecords = 20
    #service_type = 'opendap'
    #res = getResource(endpoint=endpoint, bbox=bbox, keywords=keywords, maxrecords=maxrecords)
    #print res.keys()[0]

    #csw = CatalogueServiceWeb(endpoint)




            
        
    def fetchGNData(self):
    
        xml = self.url_s + "/thredds.xml"
        
    def fetchGPData(self):
    
        xml = self.url_s + "/thredds.xml"     
        
    def onClose(self):
        print 'wizard finished'
        self.close()
         

