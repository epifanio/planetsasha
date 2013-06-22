#!/usr/bin/env python

import sys
import os
import subprocess
import string
import socket
import tempfile
import pygame
import time

class Utils(object):
    haveGRASS = 0
    
    def checkGrass(self): #maybe there is a better way
        try :
            from Gdata import Data
            from GrassShell import GrShell
            from grass.script.core import core
#            from psinit import 
            haveGRASS = 1
        except:
            haveGRASS = 0
            print "GRASS environment not found - set to disabled"
            
    @staticmethod
    def makeactiontemplate(item, lon, lat, zoom, heads, pitch, roll, range):
        
        ossimxml = '<Set target=":navigator" vref="wgs84"><%s>\
        <longitude>%s</longitude><latitude>%s</latitude>\
        <altitude>%s</altitude><heading>%s</heading><pitch>%s</pitch>\
        <roll>%s</roll><altitudeMode>absolute</altitudeMode>\
        <range>%s</range></%s></Set>' % (item, lon, lat, zoom, heads, pitch, roll, range, item)
        return ossimxml
        
        
    @staticmethod
    def MakeConection(ossimxml):
        print "NOT IMPLEMENTED"
#FIXME##        host = self.setparamconnection()[0].split()
###        nav = self.setparamconnection()[1]
###        for i in host :
###            try:
###                ossim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
###                ossim.connect((i, int(nav)))
###                ossim.send(ossimxml)
###                ossim.close()
###            except:
###                if not self.w.actionBroadcast.isChecked():
###                    self.CeckViewTypeState()
###                #if not self.w.actionHW.isChecked():
###                #    self.CeckViewTypeState()                
