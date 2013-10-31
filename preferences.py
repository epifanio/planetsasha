#!/usr/bin/env python

import sys
import os
import subprocess
import string
import socket
import tempfile
import pygame
import time
from configure import parseOutputconf

class Preferences(object):
    def __init__(self):
        self.aLonLat = False
        self.aGPS = False
        self.aBroadcast = False
        
        
    def pgsetting(self):
        #self.pgconn = PgConn()
        #self.pgconn.show()
        x=1

    def setSettings(self, key, value):
    
        if key == 'actionLonLat':
            self.aLonLat = value
            self.aGPS = not value
            self.aBcast = not value 
                       
        elif key == 'actionGPS':
            self.aGPS = value
            self.aBcast = not value
            self.aLonLat = not value
            
        elif key == 'actionBroadcast':
            self.aBcast = value
            self.aLonLat = not value
            self.aGPS = not value                  
        else:
            print 'implement the setting: ' + key
                
                                           
    def getSettings(self, key):
        if key == 'actionLonLat':
            return self.aLonLat
        elif key == 'actionGPS':
            return self.aGPS
        elif key == 'actionBroadcast':
            return self.aBcast                     
        else:
            print 'implement the setting: ' + key
                
        #print 'None' 
        return None                        
    def paramConnection(self, t):
        
        try :
            if t not in ('H','P','D'):
                print "Unknown type:" + t + " Use H/P/D for host/password/data"
            if t == 'H':
                host = str(parseOutputconf()['host'])
                return host
            elif t == 'P':    
                port = parseOutputconf()['pport']
                return int(port)
            elif t == 'D':
                data = parseOutputconf()['dport']
                return data
                
        except :
            print 'Use preference Panel to set preference'
            self.worningmessage('Use the preference setting to set TCP preference')        
