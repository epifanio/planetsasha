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


class MapWindow(QWidget, Ui_MapWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setLayout(self.verticalLayout)
        self.cmbDataset.currentIndexChanged.connect(self.viewnc)

    def viewnc(self):

        #url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc'
        url = str(self.cmbDataset.currentText())
        nc = netCDF4.Dataset(url)
        # read node locations
        lat = nc.variables['lat'][:]
        lon = nc.variables['lon'][:]
        # read connectivity array
        nv = nc.variables['nv'][:].T - 1
        tri = Tri.Triangulation(lon,lat, triangles=nv)
        h = nc.variables['h'][ :]
        
        # Now try plotting speed and vectors with Basemap using a PolyCollection
        m = Basemap(projection='merc', llcrnrlat=lat.min(), urcrnrlat=lat.max(), 
            llcrnrlon=lon.min(), urcrnrlon=lon.max(), lat_ts=lat.mean(), resolution=None)

        xnode, ynode = m(lon, lat) # convert to map coordinates with basemap

        # create another TRI object with projected coordinates
        tri = Tri.Triangulation(xnode, ynode, triangles=nv)

        # turn the triangles into a PolyCollection
        verts = concatenate((tri.x[tri.triangles][..., None],
              tri.y[tri.triangles][..., None]), axis=2)
        collection = PolyCollection(verts)
        collection.set_edgecolor('none')

        
        fig=figure(figsize=(12,12))
        ax=fig.add_subplot(111)
        m.drawmapboundary(fill_color='0.3')
        #m.drawcoastlines()
        #m.fillcontinents()
        # add the speed as colored triangles 
        ax.add_collection(collection) # add polygons to axes on basemap instance
        title('FVCOM Bathymetry')
