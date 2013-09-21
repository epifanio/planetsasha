#!/usr/bin/env python
import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_mapwindow import Ui_MapWindow
from gui.kmlwindow import KmlWindow

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


from PyQt4.QtCore import QSize
from PyQt4.QtGui import QSizePolicy

from pylab import *
from matplotlib.collections import PolyCollection , PatchCollection
import matplotlib.tri as Tri
from mpl_toolkits.basemap import Basemap
import netCDF4
import matplotlib

import datetime as dt
import numpy

import matplotlib.pyplot as plt
from tcp4ossim import addfile , delfile
import resources_rc

import matplotlib.image as mpimg
import numpy as np
import sys
import ogr
import codecs
import string
pyossim_path = os.getenv('PYOSSIM_DIR')
print pyossim_path
sys.path.append(pyossim_path + '/lib/')
from pyossim import *

import scipy
import numpy as np
import Image
from simplekml import Kml, Color

import sqlite3
import random
import time

from gui.kmldialog import KmlSettings

from g2k import GrassToKml

from netCDF4 import Dataset
from matplotlib.patches import PathPatch


class DataTransferThread(QThread):
    def __init__(self, flist):
        QThread.__init__(self)
        self.flist = flist
        #self.index = 0
        #print self.flist
        self.stopTransfer = False
       
        
    def run(self):
        while index < len(self.flist):
            time.sleep(6)
            datafile = self.flist[self.index]
            print datafile
            addfile(datafile,'localhost',8000) 
            #print self.index
            index = index + 1
        return
    
    def __del__(self):
        self.wait()

    def terminate(self):
        self.stopTransfer = True
    
class MapWindow(QWidget, Ui_MapWindow):
    def __init__(self, model = None):

        QWidget.__init__(self)

        self.setupUi(self)
        
        ##self.simkml = Kml(open=1)
        
        
        self.model = model
        self.url_base = "http://www.smast.umassd.edu:8080/thredds/dodsC/"
        self.nc = None
        
        self.setLayout(self.verticalLayout)
        
        self.figure = plt.figure()
        
        self.canvas = FigureCanvas(self.figure)
        
        self.allVarsModel = QStandardItemModel(self)
        #self.cmbVars.setModel(self.allVarsModel)

        self.cmbDataset.currentIndexChanged.connect(self.loadDataset)
        self.btDepth.clicked.connect(self.onPlotDepth)
        self.btCurrent.clicked.connect(self.onPlotCurrent)
        self.btKmlProps.clicked.connect(self.onKmlProps)
        self.btAnimate.clicked.connect(self.onAnimate)
        #self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.canvas)

        #print var (for var in self.testnc.variables)
        
        self.movie = QMovie(":/icons/icons/loading.gif");
        self.lbLoading.setMovie(self.movie)
        
        self.animate(False)
        self.fflist  = []
        self.url = "/home/rashad/Downloads/sci_20100602-20100605.nc" #set in loadmodel for now
        self.OUT_PATH = "" 

        self._tessellate = 0
        self._extrudetype = "Attribute"
        self._extrude = 0
        self._lwidth = 1
        self._altitudeMode = "clampToGround"
        self._offset = 0        
        
        self.latvar = 'lat'
        self.lonvar = 'lon'
        self.latcvar = 'latc'
        self.loncvar = 'lonc'
        self.timevar = 'time'
        self.nvvar = 'nv'
        self.hvar = 'h'
        self.interp_method = 'nearest'
        
        #delfile('/home/rashad/aa.kml','localhost',8000)
        
                
        self.figure.clf()
        self.canvas.draw()
        
        
        #self.loadDataset()
        self.loadModel()
        
        """"

        # read connectivity array
        nv = self.nc.variables['nv'][:].T - 1        
        # create a triangulation object, specifying the triangle connectivity array
        tri = Tri.Triangulation(self.lon, self.lat, triangles=nv)

        # plot depth using tricontourf
        h = self.nc.variables['h'][:]
        
        #print h
        ax1=self.figure.add_subplot(111,aspect=1.0/cos(self.latc.mean() * pi / 180.0))
        ww =tricontourf(tri,-h,levels=range(-300,10,10))
        i = 0
        #print ww.collections[0]
        #print len(ww.collections)
        k = 0

        #print self.outkml
        #sys.exit(1)
#        self.lyr.SyncToDisk()
        ds = None
        """

        self.curfile = ""
        #self.mdi = None #FIXME
        #self.kmlstr = ''
        # refresh canvas
        self.canvas.draw()
        
                
    def onAnimate(self):

      
        #self.fflist =  [ "/home/rashad/aa.shp", "/home/rashad/bb.shp", "/home/rashad/cc.shp", "/home/rashad/dd.shp"]
        self.kmllist = []
        for shpfile in self.fflist:
            inputvector = shpfile + ".shp"
            ExportVector = shpfile + ".kml"
            VectorLabelColorName  = ""
            iconpath= ""
            VectorLineColorName = "linecolor"
            colormode = "normal"
            VectorPolygonColorName = "polycolor"
            AttributeList = "name"
            self._offset = 0 ##disabled now
            self.curfile = ExportVector
            self.kmllist.append(ExportVector)


            """
            print self._extrudetype,'polygon', inputvector, ExportVector, 2, \
                  'name', 0, 'some desription here', VectorLabelColorName, \
                  'labelscale', iconpath, self._tessellate, self._extrude, \
                  self._lwidth, VectorLineColorName, colormode, \
                  VectorPolygonColorName, AttributeList, 0, 0, 0, 0, 0, \
                  self._altitudeMode, self._offset, 0, 255, 255, 255
                  
            """
            """
            GrassToKml(self._extrudetype,'polygon', inputvector, ExportVector, 1, 
                       'name', 0, 'some desription here', VectorLabelColorName, 
                       'labelscale', iconpath, self._tessellate, self._extrude, 
                       self._lwidth, VectorLineColorName, colormode, 
                       VectorPolygonColorName, AttributeList, 0, 0, 0, 0, 0, 
                       self._altitudeMode, self._offset, 0, 255, 255,255, True)
            """
        self.transferthread = DataTransferThread(self.kmllist)
        self.transferthread.start()

            

    def init_vector(self, fnamebase):

        driverName = "ESRI ShapeFile"
        fname = fnamebase + ".shp"
        drv = ogr.GetDriverByName( driverName )
        if drv is None:
            print "%s driver not available.\n" % driverName
            sys.exit( 1 )

        os.system("rm -f " + fname)
        ds = drv.CreateDataSource( fname )
        if ds is None:
            print "Creation of output file failed.\n"
            sys.exit( 1 )

        lyr = ds.CreateLayer( "fvcom_current", None, ogr.wkbPolygon )
        if lyr is None:
            print "Layer creation failed.\n"
            sys.exit( 1 )

        field_defn1 = ogr.FieldDefn( "idd", ogr.OFTString )
        field_defn2 = ogr.FieldDefn( "name", ogr.OFTString )
        field_defn3 = ogr.FieldDefn( "color", ogr.OFTString )
        field_defn1.SetWidth( 32 )
        field_defn2.SetWidth( 32 )
        field_defn3.SetWidth( 32 )
        if lyr.CreateField ( field_defn1 ) != 0:
            print "Creating field1 failed.\n"        

        if lyr.CreateField ( field_defn2 ) != 0:
            print "Creating field1 failed.\n"
    
        if lyr.CreateField ( field_defn3 ) != 0:
            print "Creating field2 failed.\n"
      
        return ds, lyr


    def add_data(self,x,y):
        feat = ogr.Feature( self.lyr.GetLayerDefn())
        feat.SetField( "idd", "1" )
        #print str(len(x)) + " " + str(len(y))
        path = ogr.Geometry(ogr.Polygon)
        #print dir(path)
        for i in xrange(len(x)):
            #print x[i]
            path.AddPoint(x[i],y[i],0.0)
        feat.SetGeometry(path)
        if self.lyr.CreateFeature(feat) != 0:
            print "Failed to create feature in shapefile.\n"
            sys.exit( 1 )
        else:
            print 'creaating feature' + str(feat.GetFID());

        feat.Destroy()
        
    def onKmlProps(self):
        #show kml dialog  
        dlg = KmlSettings()
        if dlg.exec_():
            self._tessellate = dlg.getSettings("tessellate")
            self._extrudetype = dlg.getSettings("extrudetype")
            self._extrude = dlg.getSettings("extrude")
            self._lwidth = dlg.getSettings("lwidth")
            self._altitudeMode = dlg.getSettings("altitudemode")
            self._offset = dlg.getSettings("offset")   
           
    def init_kml(self, kmlname):
        kmlstr = " <?xml version=\"1.0\" encoding=\"UTF-8\"?><kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>%s</name><open>0</open><description>%s</description>" % (kmlname, kmldescr)
        return kmlstr 
        
           
    def loadDataset(self):
    
        
        dsource = str(self.cmbDataset.currentText())
        
        self.cmbLat.clear()
        self.cmbLon.clear()
        #self.cmbVars.clear()
        
        self.cmbLat.addItem('--select-lat-var--')
        self.cmbLon.addItem('--select-lon-var--')

        self.cmbVars.addItem('--select-other-var--')        
        
        if self.cmbDataset.currentIndex() == 0:
            return
        self.url = dsource
        
        #self.url = '/home/rashad/Downloads/NECOFS_FVCOM_OCEAN_FORECAST.nc'
        self.nc = netCDF4.Dataset(self.url)
        
        allvars = self.nc.variables.keys()
        for var in allvars:
            self.cmbLat.addItem(var)
            self.cmbLon.addItem(var)
            #item = QStandardItem()
            #item.setText('xxxxxxxxxxx')
            #item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
            #item.setData(Qt.Checked, Qt.CheckStateRole)
            #self.allVarsModel.appendRow(item)
            self.cmbVars.addItem(var)
        #print allvars
            



    def animate(self, start = True):
    
        if start is True:
            self.lbLoading.show()
            self.lbLoading.setMovie(self.movie)
            self.movie.start()
        else:
            self.lbLoading.hide()
            self.movie.stop()

    def loadModel(self):
        
       
        self.progressBar.setValue(7)
        
        if not self.nc is None:
            print 'Model loaded already. Skipping loadModel()...'
            return
        dsource = str(self.cmbDataset.currentText())
        if self.cmbDataset.currentIndex() != 0:
            dsource = 'fvcom/hindcasts/30yr_gom3'
            self.url = self.url_base + dsource
        
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc'
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_GOM2_FORECAST.nc'

        #self.url = '/home/rashad/Downloads/NECOFS_FVCOM_OCEAN_FORECAST.nc'
        
        self.progressBar.setValue(19)
        
        self.nc = netCDF4.Dataset(self.url)
        
        self.progressBar.setValue(27)
        
    
        # read node locations
        self.lat = self.nc.variables[self.latvar][:]
        self.lon = self.nc.variables[self.lonvar][:]
        
        #print self.lat
        
        # read element centroid locations
        ##print self.nc.variables.keys()
        
        self.latc = self.nc.variables[self.latcvar][:]
        self.lonc = self.nc.variables[self.loncvar][:]

        self.time_var = self.nc.variables[self.timevar]
        #d= dir(self.time_var)
        #print dir(self.time_var)
        
        ###print self.time_var[:]
        
        #print self.time_var.dimensions
        #print self.time_var.ndim
        
        #print self.time_var.shape
        #print d
        
        #print dir(self.dtFrom.date())
        #print self.dtFrom.time().toString()
 
    def onPlotDepth(self):
        collections =  self.plotDepth() 
        fnamebase = '/home/rashad/ee'
        self.fflist.clear()

        ds, lyr = self.init_vector(fnamebase)
        fid = 0
        
        self.fflist.append(fnamebase)
        for col in collections:
            p = col.get_paths()[0]
            feat = ogr.Feature( lyr.GetLayerDefn())
            feat.SetField( "idd", "idd1" )
            name = "polygon#" + str(fid)
            feat.SetField( "name", name )
            feat.SetField( "color", "ccc" )
            fid = fid + 1  
            extring = ogr.Geometry(ogr.wkbLinearRing)
                        
            if len(p.vertices) > 0:
                for vert in p.vertices:
                    x = vert[0]
                    y = vert[1]
                    z = 0 #vert[2]
                    extring.AddPoint(x, y,z)
                extring.CloseRings()
                
                polygon = ogr.Geometry(ogr.wkbPolygon)
                polygon.AddGeometry(extring)
                feat.SetGeometry(polygon)
                if lyr.CreateFeature(feat) != 0:
                    print "Failed to create feature in shapefile.\n"
                    sys.exit( 1 )
                ##else:
                ##    print 'creaating feature' + str(feat.GetFID());

                feat.Destroy()
                lyr.SyncToDisk()          
        
        

    def createkml(self,collections, fname):
        self.lk_heading = -34.82469740081282
        self.lk_tilt = 53.454348562403
        self.lk_range =   276.7870053764046    
        kmls1 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>newkml</name><open>0</open><description>laeltets</description><Style id=\"Mystyle\"><LabelStyle><color>ff81ff75</color><colorMode>normal</colorMode><scale>1</scale></LabelStyle><IconStyle><Icon><href>/code/planetsasha/icons/blue_circle.png</href></Icon></IconStyle><LineStyle><color>ff3776ff</color><colorMode>normal</colorMode><tessellate>0</tessellate><width>0</width></LineStyle><PolyStyle><color>ff9646ff</color><colorMode>normal</colorMode></PolyStyle></Style>"
        
        self.lk_lat = 0
        self.lk_lon = 0
        for col in collections:
            p = col.get_paths()[0]        
            if len(p.vertices) > 0:
                self.lk_lat = p.vertices[0][0]
                self.lk_lon = p.vertices[0][1]
                break
         
        #print self.lk_lat
        #sys.exit(1)


        #self.init_kml()
        self.kmlstr2 = "\n<Folder>\
        <name>ocean_model</name>\
        <visibility>0</visibility>\
        <description>empty</description>\
        <LookAt>\
       <longitude>%s</longitude><latitude>%s</latitude>\
       <altitude>0</altitude><heading>%s</heading><tilt>%s</tilt><range>%s</range> \
            </LookAt>\
        \n<Placemark>\
          <name>Building 40</name>\
          <visibility>0</visibility>\
          <styleUrl>#Mystyle</styleUrl>" %( str(self.lk_lat), str(self.lk_lon), str(self.lk_heading), str(self.lk_tilt), str(self.lk_range))
         
            ##for vert in p.vertices:
                
            ##self.outkml = self.kmlstr1 + self.kmlstr2 + self.kmlstr3 + self.kmlstr4
            ##print self.outkml
        
                    
        for col in collections:
            p = col.get_paths()[0]
            
            self.kmlstr3 = "\n<Polygon><extrude>1</extrude><altitudeMode>relativeToGround</altitudeMode><outerBoundaryIs><LinearRing><coordinates>"

            if len(p.vertices) > 0:
                #print len(p)
                vert = p.vertices
                #print len(vert)
                for v in vert:
                
                    x = str(v[0])
                    y = str(v[1])
                    self.kmlstr3 = self.kmlstr3 + x+ "," + y + ",17 \n" 
                self.kmlstr5 = "</coordinates></LinearRing></outerBoundaryIs></Polygon>"
                
                    #print x + " " + y
                #e() 
                #self.add_data(x,y)
                #print "collection: " + str(k)
                #print str(x) + " " + str(y)
                #k = k+1
                #break
        #print self.lyr.GetFeatureCount()
        kmltail = "</Placemark></Folder></Document></kml>"
        outkml = kmls1 + self.kmlstr2 + self.kmlstr3 + self.kmlstr5 +  kmltail
        f=codecs.open(fname, 'w', 'UTF8' )
        f.write(outkml)
        f.close()
        addfile(fname,'localhost',8000) 
                  
    def plotDepth(self):
        
        self.figure.clf()
        self.canvas.draw()
        
        
        
        self.animate(True)
        self.loadModel()
        
        self.progressBar.setValue(51)
        
        # read connectivity array
        nv = self.nc.variables[self.nvvar][:].T - 1        
        # create a triangulation object, specifying the triangle connectivity array
        tri = Tri.Triangulation(self.lon, self.lat, triangles=nv)
        
        ##print self.lon

        self.progressBar.setValue(65)
        
        # plot depth using tricontourf
        h = self.nc.variables[self.hvar][:]
        
        #print h
         
        ax1=self.figure.add_subplot(111,aspect=1.0/cos(self.latc.mean() * pi / 180.0))
        
        self.progressBar.setValue(71)
        ww=tricontourf(tri,-h,levels=range(-300,10,10))
        self.progressBar.setValue(84)
        colorbar()
        self.progressBar.setValue(92)
        # refresh canvas
        self.canvas.draw()
        
        self.progressBar.setValue(100)
        
        self.animate(False)
        return ww.collections

    def onPlotCurrent(self):
        
        self.fflist.clear()
        self.figure.clf()
        self.canvas.draw()

        self.loadModel()
   
        
        self.progressBar.setValue(51)
        frmDate = self.dtFrom.dateTime()

        """
        #collections = []
        filenamebase = "/home/rashad/fromgdal"
        fname = filenamebase + ".kml"
        
        dbfilename = filenamebase + ".db"
        conn = sqlite3.connect(dbfilename)
        cur = conn.cursor()
        sql = "create table if not exists polystyle (id varchar(30), color varchar(35))"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        
        self.conn = sqlite3.connect(dbfilename)
        self.dbcur = self.conn.cursor()

        
        coll = self.plotCurrent(frmDate,filenamebase)
        self.conn.commit()
        self.dbcur.close()
        self.conn.close()
        """
        
        #collections.append(coll)       
        
        #fname = '/home/rashad/cc.kml'
        #self.createkml(collections, fname)
        self.fflist = []
        while frmDate.date().toString() != self.dtTo.dateTime().date().toString():
            frmDate = frmDate.addDays(1)
            #print frmDate.date().toString()
            
            fname =  self.OUT_PATH + str(frmDate.date().day()) + str(frmDate.date().month()) + str(frmDate.date().year()) + ".kml"
            fnamebase = self.OUT_PATH + str(frmDate.date().day()) + str(frmDate.date().month()) + str(frmDate.date().year())
            #print fname
            outfile = self.plotCurrent(frmDate, fnamebase)
            self.fflist.append(outfile) 
#            addfile(ff,'localhost',8000) 
 #           delfile(ff,'localhost',8000)
            
        print self.fflist
            #p = coll.get_paths()[0]            

            #fname = '/home/rashad/cc.kml'
            #self.createkml(collections, fname)
            #sys.exit(1)
            #"""

        
                
    def plotCurrent(self, dtfrom, fnamebase):
        
        
        #self.figure.clf()
        #self.canvas.draw()

        #self.loadModel()
        
        self.progressBar.setValue(51)
        frmDate = self.dtFrom.dateTime()


        #print 'Plotting till date: ' + dtfrom.date().toString()
        # get velocity nearest to current time
        ##dtnow = dt.datetime.utcnow() + dt.timedelta(hours=0)
        
        day = dtfrom.date().day()
        month = dtfrom.date().month()
        year = dtfrom.date().year()
        hour = dtfrom.time().hour()
        minute = dtfrom.time().minute()
        second = dtfrom.time().second()
        msecond = dtfrom.time().msec()
        
        #print dir(dtnow)
        #print dtnow.time()
        
        
        startdt = dt.datetime(year, month, day, hour, minute, second, msecond)
        #print startdt
        
        #print start
        istart = netCDF4.date2index(startdt,self.time_var,select=self.interp_method)
        layer = 0 # surface layer
        u = self.nc.variables['u'][istart, layer, :]
        v = self.nc.variables['v'][istart, layer, :]
        mag = numpy.sqrt((u*u)+(v*v)) 
        
        #print start
        #print istart
               
        self.progressBar.setValue(63)
        
        # Now try plotting speed and vectors with Basemap using a PolyCollection
        m = Basemap(projection='merc',  llcrnrlat=self.lat.min(), urcrnrlat=self.lat.max(), 
                                        llcrnrlon=self.lon.min(), urcrnrlon=self.lon.max(), 
                                        lat_ts=self.lat.mean(), resolution=None)

        # project from lon,lat to mercator
        xnode, ynode = m(self.lon, self.lat) 
        xc, yc = m(self.lonc, self.latc) 

        nv = self.nc.variables[self.nvvar][:].T - 1
        # create a TRI object with projected coordinates
        tri = Tri.Triangulation(xnode, ynode, triangles=nv)

        self.progressBar.setValue(77)
        sig_lay = self.nc.variables['siglay']
        zeta = self.nc.variables['zeta']
        
        # make a PolyCollection using triangles
        verts = concatenate((tri.x[tri.triangles][..., None],
              tri.y[tri.triangles][..., None]), axis=2)

        colorlut = []
        fid = 0
        for poly in verts:
            fid = fid + 1
       

        collection = PolyCollection(verts)
        collection.set_edgecolor('none')

        self.progressBar.setValue(81)

        timestamp=startdt.strftime('%Y-%m-%d %H:%M:%S')


        # set the magnitude of the polycollection to the speed
        collection.set_array(mag)

        
        #sys.exit(1)    
        collection.norm.vmin=0
        collection.norm.vmax=0.5


        #for path in collection.get_paths():

        cmap =collection.cmap
        featurecount = fid
        
        redArray =  matplotlib.colors.makeMappingArray(featurecount,cmap._segmentdata['red'], 1.0)            
        greenArray =  matplotlib.colors.makeMappingArray(featurecount,cmap._segmentdata['green'], 1.0)  
        blueArray =  matplotlib.colors.makeMappingArray(featurecount,cmap._segmentdata['blue'], 1.0)                
                        
        fid = 0    
        for path in collection.get_paths():
            tricolor = self.makehexcolor(redArray[fid], greenArray[fid], blueArray[fid])
            ##print tricolor
            name = "polygon#" + str(fid)
            colorlut.append(tricolor)
            #self.dbcur.execute("insert into polystyle values(?,?)",[name,str(tricolor) ])
            fid = fid + 1

        ds, lyr = self.init_vector(fnamebase)
        fid = 0
        for poly in verts:
            #print "polygon"
            linecoords = []
            feat = ogr.Feature( lyr.GetLayerDefn())
            feat.SetField( "idd", "idd1" )
            name = "polygon#" + str(fid)
            feat.SetField( "name", name )
            feat.SetField( "color", colorlut[fid] )
            fid = fid + 1
            path = ogr.Geometry(ogr.wkbPolygon)    
            extring = ogr.Geometry(ogr.wkbLinearRing)
            #path.getExteriorRing();
        
            for coord in poly:
                ##print coord
                cc = m(coord[0],coord[1],inverse=True)
                #print cc
                x = cc[0]
                y = cc[1]
                pt = fid
                tstamp = startdt.strftime('%Y-%m-%d %H:%M:%S')
                z = 0
                #z = sig_lay[pt:pt] * (zeta[pt:pt] - self.nc.variables[self.hvar][pt:pt])
                #print (zeta[tstamp,pt]) # - self.nc.variables[self.hvar][pt])
                #print zeta[:pt]
                #sys.exit(1)
                extring.AddPoint(x, y,z)
                
            extring.CloseRings()    
            polygon = ogr.Geometry(ogr.wkbPolygon)
            polygon.AddGeometry(extring)
            feat.SetGeometry(polygon)
            if lyr.CreateFeature(feat) != 0:
                print "Failed to create feature in shapefile.\n"
                sys.exit( 1 )
            ##else:
                ##print 'creaating feature' + str(feat.GetFID());

            feat.Destroy()
            lyr.SyncToDisk()          
        
        ax2=self.figure.add_subplot(111)
        coll = m.drawmapboundary(fill_color='0.3')
        
        
        self.progressBar.setValue(89)
        
        #m.drawcoastlines()
        #m.fillcontinents()
        # add the speed as colored triangles 
        ax2.add_collection(collection) # add polygons to axes on basemap instance
        # add the vectors
        #Q = m.quiver(xc,yc,u,v,scale=30)
        Q = m.quiver(xc, yc, u, v, scale=100);
        
        ##self.progressBar.setValue(94)
        # add a key for the vectors
        qk = plt.quiverkey(Q,0.1,0.1,0.20,'0.2 m/s',labelpos='W')
        title('FVCOM Surface Current speed at %s UTC' % timestamp)
  
        # refresh canvas
        self.progressBar.setValue(97)
        
        self.canvas.draw()
        
        self.progressBar.setValue(100)
        
        self.animate(False)

        print "returning..."
        outfile = fnamebase + ".shp"
        return outfile

    def makehexcolor(self, r, g, b):
        def _chkarg(a):
            if isinstance(a, int): # fit for range(0,255)
                if a < 0:
                    a = 0
                elif a > 255:
                    a = 255
            elif isinstance(a, float): # check for float and convert to range (0,255)
                if a < 0.0:
                    a = 0
                elif a > 1.0:
                    a = 255
                else:
                    a = int(round(a*255))
            else:
                raise ValueError('Arguments must be integers or floats.')
            return a
        r = _chkarg(r)
        g = _chkarg(g)
        b = _chkarg(b)
        return '{:02x}{:02x}{:02x}'.format(r,g,b)   
 
def e():
        sys.exit()
