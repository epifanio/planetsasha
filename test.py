import sys
import time
from owslib.csw import CatalogueServiceWeb

import xml.etree.ElementTree as et
import urllib2

from pylab import *
from matplotlib.collections import PolyCollection
from matplotlib.collections import TriMesh

import matplotlib.tri as Tri
from mpl_toolkits.basemap import Basemap
import datetime as dt
import netCDF4
import matplotlib

from matplotlib import pyplot, mpl

def plot1():



    # Make a figure and axes with dimensions as desired.
    fig = pyplot.figure(figsize=(8,3))
    ax1 = fig.add_axes([0.05, 0.80, 0.9, 0.15])


    # Set the colormap and norm to correspond to the data for which
    # the colorbar will be used.
    cmap = mpl.cm.cool
    norm = mpl.colors.Normalize(vmin=5, vmax=10)

    # ColorbarBase derives from ScalarMappable and puts a colorbar
    # in a specified axes, so it has everything needed for a
    # standalone colorbar.  There are many more kwargs, but the
    # following gives a basic continuous colorbar with ticks
    # and labels.
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,
                                       norm=norm,
                                       orientation='horizontal')
    cb1.set_label('Some Units')


    
    pyplot.show()

def plot():
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
    # read connectivity array
    nv = nc.variables['nv'][:].T - 1
    time_var = nc.variables['time']
    
    nv
    # create a triangulation object, specifying the triangle connectivity array
    tri = Tri.Triangulation(lon,lat, triangles=nv)

    # plot depth using tricontourf
    h = nc.variables['h'][:]
    fig=figure(figsize=(12,12))
    ax=fig.add_subplot(111,aspect=1.0/cos(latc.mean() * pi / 180.0))
    tricontourf(tri,-h,levels=range(-300,10,10))
    colorbar()

    pyplot.show()

plot()

def fetchTHData2(url, count = 0, item = None):


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
        #print href
        
        url2 = ''
        if href is not None:

                url2 = base + '/' + href
                print url2 + '::yy'
                #item = None
                fetchTHData2(url2, count + 1, item)    
        
    for elem in root.findall('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalogRef'):
        href = elem.get('{http://www.w3.org/1999/xlink}href')
        title = elem.get('{http://www.w3.org/1999/xlink}title')
        
            
        url2 = ''
        if href is not None:
            
            if href.startswith('/thredds'):
                #print base + '/' + href
                url2 = 'http://www.smast.umassd.edu:8080' + href
            else:
                url2 = base + '/' + href

                item = None
            
            
            print url2 + ':::xx'
                
            fetchTHData2(url2, count + 1, item)

    return
    
import urlparse
url = 'http://www.smast.umassd.edu:8080///'
url = urlparse.urljoin(url, '///thredds')
print url
#fetchTHData2('http://www.smast.umassd.edu:8080/thredds/catalog.xml')

def getResource(endpoint = 'http://www.nodc.noaa.gov/geoportal/csw', bbox=None, keywords=None, maxrecords=1, service_type='opendap', verbose=None):
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

endpoint = 'http://www.smast.umassd.edu:8080/thredds/catalog.xml'
bbox = [-71.5, 39.5, -63.0, 46]
keywords = ['temperature']
maxrecords = 20
service_type = 'opendap'
#res = getResource(endpoint=endpoint, bbox=bbox, keywords=keywords, maxrecords=maxrecords)
#print res.keys()[0]

#csw = CatalogueServiceWeb(endpoint)

 
