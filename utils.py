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



class Utils(object):

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
        print "GRASS environment not found - set to disabled"
    
    prefs_ = None
    #Utils.setPreferences(prefs)
    
    def __init__(self, prefs):
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
