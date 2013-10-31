from PyQt4.QtCore import *
from PyQt4.QtGui import *
from configure import parseOutputconf
import socket
#from tcp4ossim import parseSignal # , parsesignalLookAt
import pygame
import os
import time
from datetime import datetime
from utils import Utils
import gps

class HWS(QThread):
    ValUpdated = pyqtSignal(str)
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.alive = 0
        self.running = 0

    def run(self):
        #HOST = str(parseOutputconf()['host'])
        #PORT = 19000
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.bind((HOST, PORT))
        #s.listen(1)
        #conn, addr = s.accept()
        #print 'Connected by', addr
        while self.alive:
            while self.running:
                #data = conn.recv(1048)
                #try :
                #    parsed = parseSignal(data)
                #    self.ValUpdated.emit(str(parsed['lon']))
                #except :
                #    print 'parsing error'
                now = datetime.now()
                self.ValUpdated.emit(str(now))
                time.sleep(0.5)

    def toggle(self):
        if self.running:
            self.running = 0
        else :
            self.running = 1

    def stop(self):
        print 'you have to sleep'
        self.alive = 0
        self.running = 0
        self.wait()


class logS(QThread):
    LonUpdated = pyqtSignal(str)
    LatUpdated = pyqtSignal(str)
    RollUpdated = pyqtSignal(float)
    PitchUpdated = pyqtSignal(float)
    GainUpdated = pyqtSignal(float)
    AltUpdated2 = pyqtSignal(str)
    AltUpdated = pyqtSignal(float)
    LookAtLonUpdated = pyqtSignal(str)
    LookAtLatUpdated = pyqtSignal(str)
    LookAtAltitudeUpdated = pyqtSignal(str)
    LookAtRangeUpdated = pyqtSignal(float)
    #GainUpdated = pyqtSignal(float)
    
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.alive = 1
        self.running = 0
    
    
    def run(self):
        HOST = str(parseOutputconf()['host']) # 'localhost'
        print HOST
        PORT = 8000 #str(parseOutputconf()['port'])
        print PORT
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        print 'Connected to Planet - ' + HOST + '@'  + str(PORT)

       
        #print self.alive
        #print self.running
        while self.alive:
            while self.running:
                data = conn.recv(1048)
                #print data
                #print 'hhhmm'
                #print type(data)
                #time.sleep(1)
                try :
                    #time.sleep(5)
                    parsed = Utils.readPlanetMessage(data)
                    self.LonUpdated.emit(str(parsed['lontitude']))
                    self.LatUpdated.emit(str(parsed['latitude']))
                    self.RollUpdated.emit(float(parsed['roll']))
                    self.PitchUpdated.emit(float(parsed['pitch']))
                    self.GainUpdated.emit(float(parsed['gain']))
                    self.AltUpdated2.emit(str(parsed['msl']))
                    self.AltUpdated.emit(float(parsed['msl']))
                    self.LookAtLonUpdated.emit(str(parsed['lk_lon']))
                    self.LookAtLatUpdated.emit(str(parsed['lk_lat']))
                    self.LookAtAltitudeUpdated.emit(str(parsed['lk_alt']))
                    self.LookAtRangeUpdated.emit(float(parsed['lk_rng']))
                    
                #navlogger('localhost', 9000)
                    #self.msleep(500)
                except:
                    print 'parsing error'
                    #self.stop()
                    
    

    def setValueLookAtLon(self, valueLookAtLon):
        self.valueLookAtLon = valueLookAtLon

    def setValueLookAtLat(self, valueLookAtLat):
        self.valueLookAtLat = valueLookAtLat

    def setValueLookAtAlt(self, valueLookAtAlt):
        self.valueLookAtAlt = valueLookAtAlt

    def setValueLookAtRange(self, valueLookAtRange):
        self.valueLookAtRange = valueLookAtRange
   
    
    def setValueLon(self, valueLon):
        self.valueLon = valueLon
    
    
    def setValueLat(self, valueLat):
        self.valueLat = valueLat
    
    
    def setValueRoll(self, valueRoll):
        self.valueRoll = valueRoll
    
    
    def setValuePitch(self, valuePitch):
        self.valuePitch = valuePitch
    
    
    def setValueGain(self, valueGain):
        self.valueGain = valueGain
    
    
    def setValueAlt(self, valueAlt):
        self.valueAlt = valueAlt

    def setValueRange(self, valueRange):
        self.valueRange = valueRange
    
    
    def toggle(self):
        if self.running:
            self.running = 0
        else :
            self.running = 1
    
    
    def stop(self):
        self.alive = 0
        self.running = 0
        self.wait()
        


"""
class logJ1(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.valuelonJ = ""
        self.valuelatJ = ""
        self.alive = 1
        self.running = 0


    def run(self):
        while self.alive:
            while self.running:
                try :
                    startj(float(self.jlon), float(self.jlat))
                except :
                    print 'exit from Joy mode'


    def toggle(self,x,y):
        self.jlon = x
        self.jlat = y
        #pygame.init()
        if self.running:
            self.running = 0
        else :
            self.running = 1


    def stop(self):
        pygame.quit()
        self.alive = 0
        self.running = 0
        self.wait()


    def setValueLonJ(self, valuelonJ):
        self.valuelonJ = valuelonJ


    def setValueLatJ(self, valuelatJ):
        self.valuelatJ = valuelatJ


    def aggiorna(self):
        newvaluelon = str(self.valuelonJ)
        newvaluelat = str(self.valuelatJ)
        position = (newvaluelon,newvaluelat)
        print position
        return position
"""




#FIXME should be moved to gps.py    
class GpsT(QThread):
    GPSlatitude = pyqtSignal(str)
    GPSlongitude = pyqtSignal(str)
    GPSsat = pyqtSignal(str)
    GPStime = pyqtSignal(str)
    GPSeph = pyqtSignal(str)
    GPSspeed = pyqtSignal(str)
    GPSaltitude = pyqtSignal(str)
    GPSepv = pyqtSignal(str)
    GPSept = pyqtSignal(str)
    GPSclimb = pyqtSignal(str)
    satellite = pyqtSignal(str)
    GPSutctime = pyqtSignal(str)
    GPStrack = pyqtSignal(str)
    GPSepd = pyqtSignal(str)
    GPSeps = pyqtSignal(str)
    GPSepc = pyqtSignal(str)
    GPSpdop = pyqtSignal(str)
    GPShdop = pyqtSignal(str)
    GPSvdop = pyqtSignal(str)
    GPStdop = pyqtSignal(str)
    GPSgdop = pyqtSignal(str)
    GPSsat = pyqtSignal(str)
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.alive = 1
        self.running = 0
        #xprint "vivo 1"
    
        
    def run(self):
        #xprint "vivo 2"
        #session = gps.gps()
        while self.alive:
            while self.running:
                os.system('clear')
                session.query('admosyq')
                satellitelist=[]
                html = """<TABLE cellpadding="4" style="border: 1px solid \
                #000000; border-collapse: collapse;" border="1"><TR><TD>PRN</TD>\
                <TD>E</TD><TD>Az</TD><TD>Ss</TD><TD>Used</TD></TR>"""
                satellitelist.append(html)
                for i in session.satellites:                    
                    table = """<TR><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD>\
                    <TD>%s</TD>""" % (i.PRN, i.elevation, i.azimuth, i.ss, i.used)
                    satellitelist.append(table)
                htmlend = """</TR></TABLE>"""
                satellitelist.append(htmlend)
                satstringa = str(satellitelist)
                satstringa = satstringa.replace(",","")
                satstringa = satstringa.replace("[","")
                satstringa = satstringa.replace("]","")
                satstringa = satstringa.replace("'","")
                GPSlatitudex = str(session.fix.latitude)
                self.GPSlatitude.emit(str(session.fix.latitude))
                self.GPSlongitude.emit(str(session.fix.longitude))
                self.GPStime.emit(str(session.utc))
                self.GPSutctime.emit(str(session.fix.time))
                self.GPSaltitude.emit(str(session.fix.altitude))
                self.GPSeph.emit(str(session.fix.eph))
                self.GPSepv.emit(str(session.fix.epv))
                self.GPSept.emit(str(session.fix.ept))
                self.GPSspeed.emit(str(session.fix.speed))
                self.GPSclimb.emit(str(session.fix.climb))
                self.GPStrack.emit(str(session.fix.track))
                self.GPSepd.emit(str(session.fix.epd))
                self.GPSeps.emit(str(session.fix.eps))
                self.GPSepc.emit(str(session.fix.epc))
                self.GPSpdop.emit(str(session.pdop))
                self.GPShdop.emit(str(session.hdop))
                self.GPSvdop.emit(str(session.vdop))
                self.GPStdop.emit(str(session.tdop))
                self.GPSgdop.emit(str(session.gdop))
                self.GPSsat.emit(str(satstringa))
                #print satstringa
                self.msleep(1000)
            #self.msleep(1000)
    
    
    def toggle(self):
        #xprint "vivo 3"
        global session
        session = gps.gps()
        if self.running:
            self.running = 0
        else :
            self.running = 1
    
    
    def stop(self):
        #xprint "vivo 4"
        self.alive = 0
        self.running = 0
        self.wait()
        


class gt(QThread):
    def __init__(self, command, parent = None):
        QThread.__init__(self, parent)
        self.alive = 1
        self.running = 0
        self.command = command


    def run(self):
        os.system(str(self.command))
        #os.system('g.region')


    def toggle(self):
        if self.running:
            self.running = 0
        else :
            self.running = 1


    def stop(self):
        self.alive = 0
        self.running = 0
        self.wait()


class logJ(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.valuelonJ = ""
        self.valuelatJ = ""
        self.alive = 1
        self.running = 0
    
    
    def run(self):
        while self.alive:
            while self.running:
                try :
                    startj(float(self.jlon), float(self.jlat))
                except :
                    msg = 'exit from Joy mode'
                    print msg
                    self.stop()
    
    
    def toggle(self,x,y):
        self.jlon = x
        self.jlat = y
        #pygame.init()
        if self.running:
            self.running = 0
        else :
            self.running = 1
    
    
    def stop(self):
        pygame.quit()
        self.alive = 0
        self.running = 0
        self.wait()
    
    
    def setValueLonJ(self, valuelonJ):
        self.valuelonJ = valuelonJ
    
    
    def setValueLatJ(self, valuelatJ):
        self.valuelatJ = valuelatJ
    
    
    def aggiorna(self):
        newvaluelon = str(self.valuelonJ)
        newvaluelat = str(self.valuelatJ)
        position = (newvaluelon,newvaluelat)
        print position
        return position
    

