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
