#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_mapwindow import Ui_MapWindow
import os

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


from PyQt4.QtCore import QSize
from PyQt4.QtGui import QSizePolicy

from pylab import *
from matplotlib.collections import PolyCollection
import matplotlib.tri as Tri
from mpl_toolkits.basemap import Basemap
import netCDF4
import matplotlib

import datetime as dt
import numpy

import matplotlib.pyplot as plt

import resources_rc

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

        self.btDepth.clicked.connect(self.onPlotDepth)
        self.btCurrent.clicked.connect(self.onPlotCurrent)

        self.verticalLayout.addWidget(self.canvas)
        
        self.movie = QMovie(":/icons/icons/loading.gif");
        self.lbLoading.setMovie(self.movie)
        
        self.animate(False)
        

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
            self.progressBar.setValue(51)
            return
        dsource = str(self.cmbDataset.currentText())
        if self.cmbDataset.currentIndex() == 0:
            dsource = 'fvcom/hindcasts/30yr_gom3'

        url = self.url_base + dsource
        #print url
        
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc'
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_GOM2_FORECAST.nc'
        
        self.progressBar.setValue(19)
        
        self.nc = netCDF4.Dataset(url)
        
        self.progressBar.setValue(27)
        # read node locations
        self.lat = self.nc.variables['lat'][:]
        self.lon = self.nc.variables['lon'][:]
        
        # read element centroid locations
        self.latc = self.nc.variables['latc'][:]
        self.lonc = self.nc.variables['lonc'][:]

        self.time_var = self.nc.variables['time']
    
    def onPlotDepth(self):
        
        self.figure.clf()
        self.canvas.draw()
        
        
        self.animate(True)
        self.loadModel()
        
        self.progressBar.setValue(51)
        # read connectivity array
        nv = self.nc.variables['nv'][:].T - 1        
        # create a triangulation object, specifying the triangle connectivity array
        tri = Tri.Triangulation(self.lon, self.lat, triangles=nv)

        self.progressBar.setValue(65)
        
        # plot depth using tricontourf
        h = self.nc.variables['h'][:]
        ax1=self.figure.add_subplot(111,aspect=1.0/cos(self.latc.mean() * pi / 180.0))
        
        self.progressBar.setValue(71)
        tricontourf(tri,-h,levels=range(-300,10,10))
        self.progressBar.setValue(84)
        colorbar()
        self.progressBar.setValue(92)
        # refresh canvas
        self.canvas.draw()
        self.progressBar.setValue(100)
        
        self.animate(False)
        
    def onPlotCurrent(self):
        
        
        self.figure.clf()
        self.canvas.draw()

        self.loadModel()
        
        self.progressBar.setValue(51)
        
        # get velocity nearest to current time
        start = dt.datetime.utcnow()+ dt.timedelta(hours=0)
        istart = netCDF4.date2index(start,self.time_var,select='nearest')
        layer = 0 # surface layer
        u = self.nc.variables['u'][istart, layer, :]
        v = self.nc.variables['v'][istart, layer, :]
        mag = numpy.sqrt((u*u)+(v*v)) 
               
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

        timestamp=start.strftime('%Y-%m-%d %H:%M:%S')


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
        
              
    def viewnc(self):

        print matplotlib.__version__
        
        url = "http://www.smast.umassd.edu:8080/thredds/dodsC/fvcom/hindcasts/30yr_gom3"
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc'
        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_GOM2_FORECAST.nc'
        nc = netCDF4.Dataset(url)
        # read node locations
        lat = nc.variables['lat'][:]
        lon = nc.variables['lon'][:]
       
        # read element centroid locations
        latc = nc.variables['latc'][:]
        lonc = nc.variables['lonc'][:]
#        # read connectivity array
        nv = nc.variables['nv'][:].T - 1
        time_var = nc.variables['time']
#        
#        print nv
#        print lat
#        print lon
        # create a triangulation object, specifying the triangle connectivity array
        tri = Tri.Triangulation(lon,lat, triangles=nv)        
#        
#        
#        # plot depth using tricontourf
#        h = nc.variables['h'][:]
#        fig=figure(figsize=(12,12))
#        ax=fig.add_subplot(111,aspect=1.0/cos(latc.mean() * pi / 180.0))
#        tricontourf(tri,-h,levels=range(-300,10,10))
#        colorbar()
#
