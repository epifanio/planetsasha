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
        x = 1
    def pgsetting(self):
        #self.pgconn = PgConn()
        #self.pgconn.show()
        x=1
        
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
