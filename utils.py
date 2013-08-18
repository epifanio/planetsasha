#!/usr/bin/env python

import sys
import os
import subprocess
import string
import socket
import tempfile
import pygame
import time
from preferences import Preferences
import socket
from lxml import etree


class Utils(object):
    haveGRASS_ = 0
    def checkGrass(self):
    
        try :
            #=from Gdata import Data #FIXME
            #from GrassShell import GrShell #FIXME
            #from grass.script.core import core #FIXME
            #from grass.lib import grass #FIXME
            from grass.pygrass.modules import grass
            #from psinit import  #FIXME
            haveGRASS_ = 1
            print "GRASS found!! - show grass info??"
        except:
            haveGRASS_ = 0
            print "GRASS environment not found - set to disabled2"
    
    prefs_ = None
    #Utils.setPreferences(prefs)
    
    def __init__(self, prefs):

	self.checkGrass()
        Utils.prefs_ =  Preferences()

#    @staticmethod    
#    def setPreferences(prefs):
#        prefs_ = prefs

    @staticmethod  
    def preferences():
        return Utils.prefs_
        

    @staticmethod
    def makeActionTemplate(item, lon, lat, zoom, heads, pitch, roll, range):
        
        ossimxml = '<Set target=":navigator" vref="wgs84"><%s>\
        <longitude>%s</longitude><latitude>%s</latitude>\
        <altitude>%s</altitude><heading>%s</heading><pitch>%s</pitch>\
        <roll>%s</roll><altitudeMode>absolute</altitudeMode>\
        <range>%s</range></%s></Set>' % (item, lon, lat, zoom, heads, pitch, roll, range, item)
        return ossimxml
        
        
    @staticmethod
    def fireAction(ossimxml):

        host = Utils.preferences().paramConnection('H').split()
        port = Utils.preferences().paramConnection('P')
        for i in host :
            try:
                ossim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ossim.connect((i, port))
                ossim.send(ossimxml)
                ossim.close()
                return 0
            except:
                return -1

    @staticmethod	
    def sendFile(output,host,dport):
        ossim_data_xml = "<Add target=':idolbridge'><Image groupType='groundTexture'><filename>%s</filename> <id>%s</id><name>%s</name></Image></Add>" % (output,output,output)
        ossimdata = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ossimdata.connect((host, int(dport)))
        ossimdata.send(ossim_data_xml)
        ossimdata.close()

    @staticmethod
    def zoomToLonLat(lon,lat,distance,host,pport):
        ossim_zoom_xml = '<Set target=":navigator" vref="wgs84"><Camera><longitude>%s</longitude><latitude>%s</latitude><altitude>%s</altitude><heading>0</heading><pitch>0</pitch><roll>0</roll><altitudeMode>absolute</altitudeMode><range>%s</range></Camera></Set>' % (lon, lat, distance, distance)
        ossimposition = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ossimposition.connect((host, int(pport)))  
        ossimposition.send(ossim_zoom_xml)
        ossimposition.close()
    
    @staticmethod
    def removeFile(output,host,dport):
        ossimdata = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ossimdata.connect((host, int(dport)))
        ossim_data_xml = "<Remove target=':idolbridge' id='%s' />" % (output)
        ossimdata.send(ossim_data_xml)
        ossimdata.close()

    @staticmethod	
    def zoomPlanetTo(output,lon,lat,distance,host,dport,pport):
        addfile(output,host,dport)
        zoomToLonLat(lon,lat,distance,host,pport)      



    @staticmethod
    def readPlanetMessage(msg):
	    try :
	    	root = ET.fromstring(msg)
	
		lk_lat = root.xpath("//LookAt/latitude/text()")
		lk_lon = root.xpath("//LookAt/longitude/text()")
		lookat_alt = root.xpath("//LookAt/altitude/text()")
		lk_rng = root.xpath("//LookAt/range/text()")
		lk_head = root.xpath("//LookAt/heading/text()")
		lk_amode = root.xpath("//LookAt/altitudeMode/text()")

		lontitude = root.xpath("//Camera/longitude/text()")
		latitude = root.xpath("//Camera/latitude/text()")
		roll = root.xpath("//Camera/roll/text()")
		pit = root.xpath("//Camera/pitch/text()")
		head = root.xpath("//Camera/heading/text()")
		altitude = root.xpath("//Camera/altitude/text()")
		nav = {}
		nav['lontitude'] , nav['latitude'] = float(lontitude[0]) , float(latitude[0])
		nav['roll'] , nav['pitch'] , nav['gain'] , nav['msl'] = float(roll[0]), float(pit[0]), float(head[0]), float(altitude[0])
		nav['lk_lon'] , nav['lk_lat'] = float(lk_lon[0]) , float(lk_lat[0])
		nav['lookat_alt'] , nav['lk_rng'] , nav['lk_head'] , nav['lk_amode'] = float(lookat_alt[0]), float(lk_rng[0]), float(lk_head[0]), str(lk_amode[0])
		return nav
	    except :
	    	print 'error in message from planet!'



    def navigationlogs(hname,pnum):
        haddr = hname
        port = pnum
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((haddr, Pnum))
        sock.listen(1)
        conn, addr = sock.accept()
        print 'Connected by', addr
        logmsg = conn.recv(1024)
        try :
            res = readPlanetMessage(logmsg)
            #print 
            if not logmsg:
                conn.close()
        except :
        	print 'error in msg'
        conn.close()


