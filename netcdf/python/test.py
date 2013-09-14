#!/usr/bin/env python
import sys
import os
#os.environ['PYOSSIM_DIR'] = '/usr/local/ossim/python/'
try:
    ossimlib=os.environ['PYOSSIM_DIR']
    
except KeyError:
    print 'PyOSSIM python bindings not installed or PYOSSIM_DIR not set.'
    print 'Contact PlanetSasha developers'
    print 'https://github.com/epifanio/planetsasha'
    print 'Good Bye :('
    sys.exit(1)


pyossim_path = os.getenv('PYOSSIM_DIR')
pyossim_path= '/usr/local/ossim/python/lib/'
sys.path.append(pyossim_path)
print pyossim_path
from pyossim import *
import netCDF4
from matplotlib.collections import PolyCollection
import matplotlib.tri as Tri
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

import matplotlib.image as mpimg
import numpy as np

def testossimncdf(argc,argv):
    img = mpimg.imread('/code/planetsasha/image.png')
    imgplot = plt.imshow(img)
    print imgplot


def testossimncdf2(argc,argv):

    url = '/home/rashad/Downloads/sci_20100602-20100605.nc'

    
    nc = netCDF4.Dataset(url)

    # read node locations
    lat = nc.variables['lat'][:]
    lon = nc.variables['lon'][:]
    
    #print lat
    
    # read element centroid locations
    latc = nc.variables['latc'][:]
    lonc = nc.variables['lonc'][:]

    time_var = nc.variables['time']
    #d= dir(time_var)
    #print dir(time_var)
    
    ###print time_var[:]
    
    #print time_var.dimensions
    #print time_var.ndim
    
    #print time_var.shape
    #print d
    
    #print dir(dtFrom.date())
    #print dtFrom.time().toString()

    # read connectivity array
    nv = nc.variables['nv'][:].T - 1        
    # create a triangulation object, specifying the triangle connectivity array
    tri = Tri.Triangulation(lon, lat, triangles=nv)
    
    # plot depth using tricontourf
    h = nc.variables['h'][:]
    
    print h
    
    ##registry = ossimImageHandlerRegistry.instance()

    #array = h

    memSource = ossimMemoryImageSource()
    stype = PYOSSIM_UINT16
    imdata = ossimImageData(memSource,stype,1)
    imdata.initialize()

    WriteArrayToImageData(imdata,h,0)
    outfile = "out_from_rw.jpg"
    WriteImageDataToFile(imdata,outfile)
    #raw_input()   

     
    ##ax1=figure.add_subplot(111,aspect=1.0/cos(latc.mean() * pi / 180.0))
    
    ##tricontourf(tri,-h,levels=range(-300,10,10))

    ##colorbar()

    # refresh canvas
    ##canvas.draw()


if __name__ == "__main__":
    init = ossimInit.instance()
    init.initialize()
    testossimncdf(len(sys.argv),sys.argv)

