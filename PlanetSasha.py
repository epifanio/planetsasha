#!/usr/bin/env python

import sys
import os
import subprocess
import string
import socket
import tempfile
import pygame
import time
from pysqlite2 import dbapi2 as sqlite3

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#from guix import GuiWidget



#from msgworntcp import worntcp

try:
    ossimlib=os.environ['PYOSSIM_DIR']
except KeyError:
    print 'PyOSSIM python bindings not found. contact PlanetSasha developers'
    print 'https://github.com/epifanio/planetsasha'
    print 'Good Bye :('
    sys.exit(1)



#from episg import *

#import gps


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

apppath = os.path.abspath(os.path.dirname(sys.argv[0]))

splash = '%s/spla.png' % (apppath)
configfile = '%s/conf/conf.xml' % (apppath)


# clon = 0
# clat = 0
# item = 'LookAt'
head = '0'
ell = 23

##try :
##    from Gdata import Data
##    from GrassShell import GrShell
##    from grass.script.core import *
##    from psinit import *
##    GRASS = 1
##except:
##    GRASS = 0
##    print "GRASS environment not found - set to disabled"

#core
from preferences import Preferences
from utils import Utils
#gui
from gui.sashamainwindow import SashaMainWindow

#from gui.warnmsgwindow import WarnMsgWindow
#from gui.kmlwindow import KmlWindow
#from gui.modelwindow import PlaceModel
#from gui.vectoropswindow import VectorOpsWindow

#from gui.epsgwindow import EpsgWindow
#from LatLongUTMconversion import LLtoUTM
from tcp4ossim import addfile

from owslib.csw import CatalogueServiceWeb
from g2k import GrassToKml

class PlanetSasha(SashaMainWindow):
##    _instance = None
##    def __new__(cls, *args, **kwargs):
##        if not cls._instance:
##            cls._instance = super(PlanetSasha, cls).__new__(
##                                cls, *args, **kwargs)
##        return cls._instance
        
    def __init__(self, arg):
    
        prefs = Preferences() #FIXME should go inside Utils ctor
        Utils(prefs)    
    
        SashaMainWindow.__init__(self, arg)

        """
        extrudetype = "Attribute"
        inputvector = "/home/rashad/fromgdal.shp"
        ExportVector = "/home/rashad/fromsaha.kml"
        VectorLabelColorName  = ""
        iconpath= ""
        tessellate = 0
        extrude = 0
        lwidth = 2
        VectorLineColorName = "linecolor"
        colormode = "normal"
        VectorPolygonColorName = "polycolor"
        AttributeList = "name"
        AltitudeMode = "clampToGround"
        print extrudetype,'polygon', inputvector, ExportVector, 2, \
              'name', 0, 'some desription here', VectorLabelColorName, \
              'labelscale', iconpath, tessellate, extrude, \
              lwidth, VectorLineColorName, colormode, \
              VectorPolygonColorName, AttributeList, 0, 0, 0, 0, 0, \
              AltitudeMode, 0, 0, \
              255, 255, \
              255
        GrassToKml(extrudetype,'polygon', inputvector, ExportVector, 1, 
                   'name', 0, 'some desription here', VectorLabelColorName, 
                   'labelscale', iconpath, tessellate, extrude, 
                   lwidth, VectorLineColorName, colormode, 
                   VectorPolygonColorName, AttributeList, 0, 0, 0, 0, 0, 
                   AltitudeMode, 0, 0,      255, 255,255, True)        

        sys.exit(1)
        """
        #self.initWidgets()

        #addfile('/home/rashad/aa.kml','localhost',8000)
        #sys.exit(1)
        
        self.Value=0
        self.ValueJ=0

        self.queryvalue = 0
        
        endpoint = 'http://www.smast.umassd.edu:8080/'
        bbox = [-71.5, 39.5, -63.0, 46]
        keywords = ['temperature']
        maxrecords = 20
        service_type = 'opendap'
        #res = self.getResource(endpoint=endpoint, bbox=bbox, keywords=keywords, maxrecords=maxrecords)
        #print res.keys()[0]
        #self.connectSignals()
           



# Quit Application
        
    def quitAll(self):
        qApp.quit()
    

        
# Set Configuration
              

    

    def setgrassparam(self):
        try :
            PointSize = str(parseOutputconf()['PointSize'])
            LineWidth = str(parseOutputconf()['LineWidth'])
            PenColor = str(parseOutputconf()['PenColor'])
            BrushColor = str(parseOutputconf()['BrushColor'])
            Thickness = parseOutputconf()['Thickness']
            Fill = parseOutputconf()['Fill']
            print PointSize, LineWidth, PenColor, BrushColor, Thickness, Fill
            return PointSize, LineWidth, PenColor, BrushColor, Thickness, Fill
        except :
            print 'Use preference Panel to set preference'
            self.worningmessage('Use the preference setting to set TCP preference')

    
# Set Position Messages    

    




 
# Set GRASS Vector/Raster 
   

    
        





    
    #def addcmd(self):
    #    commandlist = self.commandlist()
    #    self.w.gcmd.addItems(commandlist)
    
    

    
        

# Show External Widgets
    

    
    

    
    

    
    
#    def worningmessagetcp(self):
#        self.worntcp = worntcp()
#        self.worntcp.show()
#    
    

    
# code not used :
    
    def modeldialog(self):
        self.placemodel.show()
        #lite
    
    
    def setparamconnection2(self):
        try:
            TCP = open(tcpparam, "r")
            K = TCP.read()
            Y = K.rsplit(',')
            host = str(Y[0])
            nav = str(Y[1])
            data = str(Y[2])
            return host, nav, data
        except :
            print 'Use preference Panel to set preference'
            self.worningmessage('Use the preference setting to set TCP preference')
    
    def GpsHandling(self):
        #print self.item,self.w.ZoomSlider.value(),head,self.w.PitchSlider.value(),
        #self.w.RollSlider.value(),self.w.RangeSlider.value()
        #self.gps = GpsClass(self.item,self.w.ZoomSlider.value(),head,
        #self.w.PitchSlider.value(),self.w.RollSlider.value(),self.w.RangeSlider.value())
        self.gps.show()
    
    
    def GetType(self,index):
        global Gtype
        Gtype = self.w.GrassType.itemText(index)
        if Gtype == 'region':
            while 1:
                try:
                    rg = list_strings('region')
                    break
                except IOError:
                    time.sleep(0.1)
            region = []
            for i in rg:
                rgname = i.split('@', 2)[0]
                region.append(rgname)
            region.sort()
            self.w.InputType.clear()
            self.w.InputType.addItems(region)
        if Gtype == 'vect':
            while 1:
                try:
                    vc = list_strings('vect')
                    break
                except IOError:
                    time.split(0.1)
            vector = []
            for i in vc:
                vecname = i.split('@', 2)[0]
                vector.append(vecname)
            vector.sort()
            self.w.InputType.clear()
            self.w.InputType.addItems(vector)
        if Gtype == 'rast':
            while 1:
                try:
                    rs = list_strings('rast')
                    break
                except IOError:
                    time.sleep(0.1)
            raster = []
            for i in rs:
                rasname = i.split('@', 2)[0]
                raster.append(rasname)
            raster.sort()
            self.w.InputType.clear()
            self.w.InputType.addItems(raster)
        #return GType
    
        
# Refresh SQLite
        
    def refreshsqlitedb(self):
        print 'refresh sqlite'
        tables = self.gettablelist()
        if tables is not None :
            self.w.Place.clear()
            self.w.Place.addItems(tables)
    
    
    def itemlist(self,index):
        Zone = self.w.Place.itemText(index)
        database_name = parseOutputconf()['spatialitedb']
        db_connection = None
        try :
            db_connection = sqlite3.connect(database_name)
        except :
            self.worningmessage('spatialitedb not found')
        if db_connection is not None:
            db_connection = sqlite3.connect(database_name)
            db_cursor = db_connection.cursor()
            try :
                listatabelle = db_cursor.execute("SELECT name,latitude,longitude FROM %s ;" % (Zone))
                tabelle = listatabelle.fetchall()
                tablelist = []
                allist = []
                for i in tabelle:
                    tablelist.append(i[0])
                    allist.append(i[0]+' '+str(i[1])+' '+str(i[2]))
                allist.sort()
                tablelist.sort()
                self.w.placezone.clear()
                self.w.placezone.addItems(allist)
                db_connection.commit()
            except :
                print 'reload sqlite'
    
        
    def setplacezonecoords(self,index):
        Placename = self.w.placezone.itemText(index)
        st = unicode(Placename)
        st = st.split(' ')
        try :
            lat = st[-2]
            lon = st[-1]
            self.w.Lon.setText(lon)
            self.w.Lat.setText(lat)
        except :
            pass
    
        
    def gettablelist(self):
        #database_name = sqlitedb
        database_name = parseOutputconf()['spatialitedb']
        print database_name
        db_connection = None
        try :
            db_connection = sqlite3.connect(database_name)
        except :
            self.worningmessage('spatialitedb not found')
        if db_connection is not None:
            db_cursor = db_connection.cursor()
            listatabelle = db_cursor.execute("SELECT name FROM sqlite_master where type = 'table';")
            tabelle = listatabelle.fetchall()
            tablelist = []
            for i in tabelle:
                tablelist.append(i[0])
            db_connection.commit()
            tablelist.sort()
            return tablelist
    
    



if __name__ == "__main__":
    import sys
    import time
    app = QApplication(sys.argv)
    ss = None
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    splash_pix = QPixmap(splash)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    #splash_pix_mask = QPixmap(splash_mask)
    #splash.setMask(splash_pix_mask.mask())
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(1)
    app.processEvents()
    p = PlanetSasha(arg1)
    p.showMaximized()
    splash.close()
    sys.exit(app.exec_())





