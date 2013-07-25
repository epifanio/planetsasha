#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_mapwindow import Ui_MapWindow
import os

from pylab import *
from matplotlib.collections import PolyCollection
import matplotlib.tri as Tri
from mpl_toolkits.basemap import Basemap
import netCDF4
import matplotlib

class MapWindow(QWidget, Ui_MapWindow):
    def __init__(self, model = None):
        QWidget.__init__(self)
        self.setupUi(self)
        self.model = model        
        
        self.setLayout(self.verticalLayout)
        self.cmbDataset.currentIndexChanged.connect(self.viewnc)
        self.viewnc()

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
