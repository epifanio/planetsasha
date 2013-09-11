#!/usr/bin/env python
import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_mapwindow import Ui_MapWindow


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


from PyQt4.QtCore import QSize
from PyQt4.QtGui import QSizePolicy

from pylab import *
from matplotlib.collections import PolyCollection
import matplotlib.tri as Tri
#from mpl_toolkits.basemap import Basemap
import netCDF4
import matplotlib

import datetime as dt
import numpy

import matplotlib.pyplot as plt

import resources_rc

import matplotlib.image as mpimg
import numpy as np
import sys
import ogr
import string
pyossim_path = os.getenv('PYOSSIM_DIR')
print pyossim_path
sys.path.append(pyossim_path + '/lib/')
from pyossim import *

import scipy
import numpy as np
import Image

from netCDF4 import Dataset

class MapWindow(QWidget, Ui_MapWindow):
    def __init__(self, model = None):

        QWidget.__init__(self)

        self.setupUi(self)
        
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

        #self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.canvas)
        
        self.url = '/home/rashad/Downloads/sci_20100602-20100605.nc'
        #self.testnc = netCDF4.Dataset(self.url)    
        #print var (for var in self.testnc.variables)
        
        self.movie = QMovie(":/icons/icons/loading.gif");
        self.lbLoading.setMovie(self.movie)
        
        self.animate(False)
        
                
        self.figure.clf()
        self.canvas.draw()
        
        
        #self.loadDataset()
        ##self.loadModel()
        
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
        ##print ww.collections[0]
        ##print len(ww.collections)
        k = 0
        
        self.ds = None
        self.ds, self.lyr = self.init_vector()
        self.init_kml()
        for col in ww.collections:
            p = col.get_paths()[0]
            
            if len(p.vertices) > 0:
                #print len(p)
                v = p.vertices
                x = v[:,0]
                y = v[:,1]
                self.add_data(x,y)
                #print "collection: " + str(k)
                #print str(x) + " " + str(y)
                k = k+1
                #break
        
        ds = None
        """
        self.nvvar = ''
        self.hvar = ''
        self.interp_method = 'nearest'
        # refresh canvas
        self.canvas.draw()
        
        ##self.loadModel()
    def init_kml(self, kmlname):
        kmlstr = " <?xml version=\"1.0\" encoding=\"UTF-8\"?><kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>%s</name><open>0</open><description>%s</description>" % (kmlname, kmldescr)
        """
    <Style id="Mystyle">
        <LabelStyle>
            <color>87000000</color>
            <colorMode>normal</colorMode>
            <scale>1</scale>
        </LabelStyle>
        <IconStyle>
            <Icon>
            <href>http://maps.google.com/mapfiles/kml/pal3/icon19.png</href>
            </Icon>
        </IconStyle>
        
        <LineStyle>
            <color>753200ae</color>
            <colorMode>normal</colorMode>
            <tessellate>1</tessellate>
            <width>2</width>
        </LineStyle>
        <PolyStyle>
            <color>87450ab1</color>
            <colorMode>normal</colorMode>
        </PolyStyle>
    </Style>
        """ 
        """   
      <Folder>
        <name>ocean_model</name>
        <visibility>0</visibility>
        <description>empty</description>
        <LookAt>
          <longitude>-122.084120030116</longitude>
          <latitude>37.42174011925477</latitude>
          <altitude>0</altitude>
          <heading>-34.82469740081282</heading>
          <tilt>53.454348562403</tilt>
          <range>276.7870053764046</range>
        </LookAt>
        <Placemark>
          <name>Building 40</name>
          <visibility>0</visibility>
          <styleUrl>#Mystyle</styleUrl>
        
          <Polygon>
            <extrude>1</extrude>
            <altitudeMode>relativeToGround</altitudeMode>
            <outerBoundaryIs>
              <LinearRing>
                <coordinates> -122.0848938459612,37.42257124044786,17
                  -122.0849580979198,37.42211922626856,17
                  -122.0847469573047,37.42207183952619,17
                  -122.0845725380962,37.42209006729676,17
                  -122.0845954886723,37.42215932700895,17
                  -122.0838521118269,37.42227278564371,17
                  -122.083792243335,37.42203539112084,17
                  -122.0835076656616,37.42209006957106,17
                  -122.0834709464152,37.42200987395161,17
                  -122.0831221085748,37.4221046494946,17
                  -122.0829247374572,37.42226503990386,17
                  -122.0829339169385,37.42231242843094,17
                  -122.0833837359737,37.42225046087618,17
                  -122.0833607854248,37.42234159228745,17
                  -122.0834204551642,37.42237075460644,17
                  -122.083659133885,37.42251292011001,17
                  -122.0839758438952,37.42265873093781,17
                  -122.0842374743331,37.42265143972521,17
                  -122.0845036949503,37.4226514386435,17
                  -122.0848020460801,37.42261133916315,17
                  -122.0847882750515,37.42256395055121,17
                  -122.0848938459612,37.42257124044786,17 </coordinates>
              </LinearRing>
            </outerBoundaryIs>
          </Polygon>
        </Placemark>
      </Folder>
        """
#</Document>
#</kml>


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
            
    def init_vector(self):

        driverName = "ESRI Shapefile"
        drv = ogr.GetDriverByName( driverName )
        if drv is None:
            print "%s driver not available.\n" % driverName
            sys.exit( 1 )

        os.system("rm -f point_outss.shp")
        ds = drv.CreateDataSource( "point_outss.shp" )
        if ds is None:
            print "Creation of output file failed.\n"
            sys.exit( 1 )

        lyr = ds.CreateLayer( "point_out", None, ogr.wkbLineString )
        if lyr is None:
            print "Layer creation failed.\n"
            sys.exit( 1 )

        field_defn = ogr.FieldDefn( "Name", ogr.OFTString )
        field_defn.SetWidth( 32 )

        if lyr.CreateField ( field_defn ) != 0:
            print "Creating Name field failed.\n"
            sys.exit( 1 )

        return ds, lyr


    def add_data(self,x,y):
        feat = ogr.Feature( self.lyr.GetLayerDefn())
        feat.SetField( "id", "1" )
        print str(len(x)) + " " + str(len(y))
        path = ogr.Geometry(ogr.wkbLineString)
        #print dir(path)
        for i in xrange(len(x)):
            path.AddPoint(x[i],y[i],0.0)
        feat.SetGeometry(path)
        if self.lyr.CreateFeature(feat) != 0:
            print "Failed to create feature in shapefile.\n"
            sys.exit( 1 )        
        
        """
            pt = ogr.Geometry(ogr.wkbPoint)
            pt.SetPoint_2D(0, x, y)

            feat.SetGeometry(pt)

            if self.lyr.CreateFeature(feat) != 0:
                print "Failed to create feature in shapefile.\n"
                sys.exit( 1 )
        """
        feat.Destroy()


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
        if self.cmbDataset.currentIndex() == 0:
            dsource = 'fvcom/hindcasts/30yr_gom3'

        url = self.url_base + dsource
        
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc'
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_GOM2_FORECAST.nc'

        url = '/home/rashad/Downloads/NECOFS_FVCOM_OCEAN_FORECAST.nc'
        
        self.progressBar.setValue(19)
        
        self.nc = netCDF4.Dataset(self.url)
        
        self.progressBar.setValue(27)
        
        latvar = 'lat'
        lonvar = 'lon'
        latcvar = 'latc'
        loncvar = 'lonc'
        timevar = 'time'
        self.nvvar = 'nv'
        self.hvar = 'h'        
        # read node locations
        self.lat = self.nc.variables[latvar][:]
        self.lon = self.nc.variables[lonvar][:]
        
        #print self.lat
        
        # read element centroid locations
        self.latc = self.nc.variables[latcvar][:]
        self.lonc = self.nc.variables[loncvar][:]

        self.time_var = self.nc.variables[timevar]
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
        
        self.figure.savefig('image.png', bbox_inches=0)
        
        self.progressBar.setValue(100)
        
        self.animate(False)
        
    def onPlotCurrent(self):
        
        
        self.figure.clf()
        self.canvas.draw()

        self.loadModel()
        
        self.progressBar.setValue(51)
        
        
        print 'Plotting till date: ' + self.dtFrom.date().toString()
        # get velocity nearest to current time
        dtnow = dt.datetime.utcnow() + dt.timedelta(hours=0)
        
        day = self.dtFrom.date().day()
        month = self.dtFrom.date().month()
        year = self.dtFrom.date().year()
        hour = dtnow.time().hour
        minute = dtnow.time().minute
        second = dtnow.time().second
        msecond = dtnow.time().microsecond
        
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
        print istart
               
        self.progressBar.setValue(63)
        
        # Now try plotting speed and vectors with Basemap using a PolyCollection
        m = Basemap(projection='merc',  llcrnrlat=self.lat.min(), urcrnrlat=self.lat.max(), 
                                        llcrnrlon=self.lon.min(), urcrnrlon=self.lon.max(), 
                                        lat_ts=self.lat.mean(), resolution=None)

        # project from lon,lat to mercator
        xnode, ynode = m(self.lon, self.lat) 
        xc, yc = m(self.lonc, self.latc) 

        nv = self.nc.variables['nv'][:].T - 1
        # create a TRI object with projected coordinates
        tri = Tri.Triangulation(xnode, ynode, triangles=nv)

        self.progressBar.setValue(77)
        
        
        # make a PolyCollection using triangles
        verts = concatenate((tri.x[tri.triangles][..., None],
              tri.y[tri.triangles][..., None]), axis=2)
        collection = PolyCollection(verts)
        collection.set_edgecolor('none')

        self.progressBar.setValue(81)

        timestamp=startdt.strftime('%Y-%m-%d %H:%M:%S')


        # set the magnitude of the polycollection to the speed
        collection.set_array(mag)
        collection.norm.vmin=0
        collection.norm.vmax=0.5


        ax2=self.figure.add_subplot(111)
        m.drawmapboundary(fill_color='0.3')
        
        
        self.progressBar.setValue(89)
        
        #m.drawcoastlines()
        #m.fillcontinents()
        # add the speed as colored triangles 
        ax2.add_collection(collection) # add polygons to axes on basemap instance
        # add the vectors
        #Q = m.quiver(xc,yc,u,v,scale=30)
        Q = m.quiver(xc, yc, u, v, scale=100);
        
        self.progressBar.setValue(94)
        # add a key for the vectors
        qk = plt.quiverkey(Q,0.1,0.1,0.20,'0.2 m/s',labelpos='W')
        title('FVCOM Surface Current speed at %s UTC' % timestamp)
  
        # refresh canvas
        self.progressBar.setValue(97)
        
        self.canvas.draw()
        
        self.progressBar.setValue(100)
        
        self.animate(False)
        
