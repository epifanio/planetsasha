#!/usr/local/bin/python
 
import datetime as dt
import netCDF4
import datetime as dt
 
def fetchNC(url='http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_OCEAN_MASSBAY_FORECAST.nc'):
    start = dt.datetime.now()
    nc = netCDF4.Dataset(url)
    ncTime = dt.datetime.now()
    
    lat = nc.variables['lat'][:]
    latTime = dt.datetime.now()
    
    lon = nc.variables['lon'][:]
    lonTime = dt.datetime.now()
    lindex = 0
    bbox =  [-70.7, -70.6, 41.48, 41.55]
    
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
    
    
if __name__ == '__main__':
    fetchNC()
