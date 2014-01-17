import datetime as dt
import netCDF4
import datetime as dt


def fetchNC(url='http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc', bbox=None):
    start = dt.datetime.now()
    nc = netCDF4.Dataset(url)
    ncTime = dt.datetime.now()
    
    lat = nc.variables['lat'][:]
    latTime = dt.datetime.now()
    
    lon = nc.variables['lon'][:]
    lonTime = dt.datetime.now()
    lindex = 0
    
    if bbox is not None:   
        start = ( lon >= bbox[0] ) & ( lon <= bbox[2] )
        end =   ( lat >= bbox[1] ) & ( lat <= bbox[3] )    
    
    
        latc = nc.variables['latc'][lindex, start,end]
        latcTime = dt.datetime.now()

        lonc = nc.variables['lonc'][lindex, start,end]
        loncTime = dt.datetime.now()
    else:
        
        latc = nc.variables['latc'][:]
        latcTime = dt.datetime.now()

        lonc = nc.variables['lonc'][:]
        loncTime = dt.datetime.now()
                
    print 'nc fetched in : ', ncTime-start
    print 'lat fetched in : ', latTime-ncTime
    print 'latc fetched in : ', latcTime-latTime
    print 'lon fetched in : ', lonTime-latcTime
    print 'lonc fetched in : ', loncTime-lonTime
    print 'total time : ', loncTime-start
    

'''
fetchNC(bbox=None)

# print :
# nc fetched in :  0:00:00.803309
# lat fetched in :  0:00:01.369446
# latc fetched in :  0:00:02.894489
# lon fetched in :  -1 day, 23:59:58.178018  
# lonc fetched in :  0:00:03.631206
# total time :  0:00:06.876468
#  (i'm in different time zone than my VM settings .. i shoyld use UTC time)


bbox =  [-70.7, -70.6, 41.48, 41.55]
fetchNC(bbox=bbox)

# give error :
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-f7ac50f48e55> in <module>()
----> 1 fetchNC(bbox=bbox)

<ipython-input-6-819ac5d3be16> in fetchNC(url, bbox)
     16 
     17 
---> 18         latc = nc.variables['latc'][lindex, start,end]
     19         latcTime = dt.datetime.now()
     20 

/usr/local/lib/python2.7/dist-packages/netCDF4.so in netCDF4.Variable.__getitem__ (netCDF4.c:34013)()

/usr/local/lib/python2.7/dist-packages/netCDF4_utils.pyc in _StartCountStride(elem, shape, dimensions, grp, datashape)
    203     # make sure there are not too many dimensions in slice.
    204     if len(elem) > nDims:
--> 205         raise ValueError("slicing expression exceeds the number of dimensions of the variable")
    206 
    207     # Compute the dimensions of the start, count, stride and indices arrays.

ValueError: slicing expression exceeds the number of dimensions of the variable
'''

