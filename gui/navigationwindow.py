#!/usr/bin/env python
import os
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_navigationwindow import Ui_NavigationWindow

from drawer import *
from utils import Utils

from log import *

class NavigationWindow(QWidget, Ui_NavigationWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.log = None

        #self.scrollArea.setWidget(self.widget)
        
        self.scrollAreaWidgetContents_5.setLayout(self.verticalLayout_2)
 #       self.L1.addWidget(self.scrollArea)
#        self.setLayout(self.L1)
        self.Place.setEditable(1)
        self.Place.setAutoCompletion(1)
        self.placezone.setEditable(1)
        self.placezone.setAutoCompletion(1)

        compass_widget = DrawCompass(self)
        roll_widget = DrawRoll(self)
        
        self.head = 'Manual'
        self.item = self.GetViewType(0)
                
        self.Lon.setText("0")
        self.Lat.setText("0")
        
        self.RollSlider.hide()
        self.PitchSlider.hide()
        self.HandlingSlider.hide()
        self.ZoomSlider.hide()
        self.RangeSlider.hide()
        
        self.rotationAngleSpinBox = QSpinBox()
        self.rotationAngleSpinBox.setRange(0, 359)
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix('\xB0')
        self.rotationAngleLabel = QLabel("&Heading:")
        self.rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)
        self.compassArea.setWidget(compass_widget)

        self.HLayout = QHBoxLayout()
        self.HLayout.addWidget(self.rotationAngleLabel)
        self.HLayout.addWidget(self.rotationAngleSpinBox)
        self.compassLayout.addLayout(self.HLayout)
        self.rotationAngleSpinBox.valueChanged.connect(compass_widget.setRotationAngle)
        self.rotationAngleSpinBox.hide()
        self.rotationAngleLabel.hide()
        
        self.rotationRollSpinBox = QSpinBox()
        self.rotationRollSpinBox.setRange(0, 359)
        self.rotationRollSpinBox.setWrapping(True)
        self.rotationRollSpinBox.setSuffix('\xB0')
        self.rotationRollLabel = QLabel("&Roll:")
        self.rotationRollLabel.setBuddy(self.rotationRollLabel)
        self.rollArea.setWidget(roll_widget)
        self.HLayoutRoll = QHBoxLayout()
        self.HLayoutRoll.addWidget(self.rotationRollLabel)
        self.HLayoutRoll.addWidget(self.rotationRollSpinBox)
        self.rollLayout.addLayout(self.HLayoutRoll)
        self.rotationRollSpinBox.valueChanged.connect(roll_widget.setRotationAngle)
        self.rotationRollSpinBox.hide()
        self.rotationRollLabel.hide()
        self.ZoomSpinBox.setValue(0)
        self.RangeSpinBox.setValue(100000)
        self.ZoomSlider.setValue(0)
        self.RangeSlider.setValue(100000)

        # Pan Toolbox
        self.north.setAutoRepeat(True)
        self.northeast.setAutoRepeat(True)
        self.south.setAutoRepeat(True)
        self.east.setAutoRepeat(True)
        self.west.setAutoRepeat(True)
        self.southwest.setAutoRepeat(True)
        self.northwest.setAutoRepeat(True)
        self.southeast.setAutoRepeat(True)

        self.connectPanSignals()
        self.connectZoomSignals()
        self.connectRangeSignals()
        self.connectRollSignals()
        self.connectPitchSignals()
        
        self.connectHeadSignals()
        self.connectSpeedSignals()
        self.connectZoomRangeSignals()
        
        
        self.fxvallon = self.SetPosition()[0]
        self.fxvallat = self.SetPosition()[1]
        self.slstep = 1
        self.connectPositonActions()
        
        # Coordinate Display UTM
        self.connect(self.ellipse, SIGNAL("currentIndexChanged(int)"), self.ellipsesettings)
        # View Type
        self.connect(self.View, SIGNAL("currentIndexChanged(int)"), self.GetViewType)
        
        self.connect(self.Place, SIGNAL("currentIndexChanged(int)"),
                     self.itemlist)
        self.connect(self.placezone, SIGNAL("currentIndexChanged(int)"), 
                     self.setplacezonecoords)
        self.connect(self.refreshsqlite, SIGNAL("clicked()"), self.refreshsqlitedb)
        
        #FME:URGENT self.connect(self.update, SIGNAL("clicked()"),self.aggiorna)

        #self.slvallon = self.getCenter()[0]
        #self.slvallat = self.getCenter()[1]
#        self.connect(self.Lon, SIGNAL("textChanged(QString)"), 
#                     self.datawin.setLonValue)
#        self.connect(self.Lat, SIGNAL("textChanged(QString)"), 
#                     self.datawin.setLatValue)


        
#        self.connect(self.actionGrass, SIGNAL("triggered()"),
#                     self.Grassunceckbuttons)
#        # Grass Shell
#        self.connect(self.actionGrassshell, SIGNAL("triggered()"), 
#                     self.GrassShell)

    def toogleBroadCast(self, checked):

        if checked:
            self.log = logS()
            self.log.start()
            self.log.LonUpdated.connect(self.Lon.setText)
            self.log.LatUpdated.connect(self.Lat.setText)
            self.log.RollUpdated.connect(self.RollSpinBox.setValue)
            self.log.PitchUpdated.connect(self.PitchSpinBox.setValue)
            self.log.GainUpdated.connect(self.HandlingSpinBox.setValue)
            self.log.AltUpdated2.connect(self.Alt.setText)
            self.log.AltUpdated.connect(self.ZoomSpinBox.setValue)
            self.log.LookAtLonUpdated.connect(self.lookatLon.setText)
            self.log.LookAtLatUpdated.connect(self.lookatLat.setText)
            self.log.LookAtAltitudeUpdated.connect(self.lookatAlt.setText)
            self.log.LookAtRangeUpdated.connect(self.RangeSpinBox.setValue)
            print 'starting bcast'
            self.log.toggle()
        else :
            print 'stoppoing bcast'
            self.log.stop()
            self.log = None
            
    def itemlist(self,index):
        Zone = self.Place.itemText(index)
        database_name = parseOutputconf()['spatialitedb']
        db_connection = None
        try :
            db_connection = sqlite3.connect(database_name)
        except :
            self.worningmessage('spatialitedb not found')
        if db_connection is not None:
            db_connection = sqlite3.connect(database_name)
            db_cursor = db_connection.cursor()
            try :
                listatabelle = db_cursor.execute("SELECT name,latitude,longitude FROM %s ;" % (Zone))
                tabelle = listatabelle.fetchall()
                tablelist = []
                allist = []
                for i in tabelle:
                    tablelist.append(i[0])
                    allist.append(i[0]+' '+str(i[1])+' '+str(i[2]))
                allist.sort()
                tablelist.sort()
                self.placezone.clear()
                self.placezone.addItems(allist)
                db_connection.commit()
            except :
                print 'reload sqlite' #xprint
    
    def refreshsqlitedb(self):
        #xprint 'refresh sqlite'
        tables = self.gettablelist()
        if tables is not None :
            self.Place.clear()
            self.Place.addItems(tables)
    
            
    def setplacezonecoords(self,index):
        Placename = self.placezone.itemText(index)
        st = unicode(Placename)
        st = st.split(' ')
        try :
            lat = st[-2]
            lon = st[-1]
            self.Lon.setText(lon)
            self.Lat.setText(lat)
        except :
            pass
    def SetLonLat(self):
        host = self.setparamconnection()[0]
        nav = self.setparamconnection()[1]
        heads = head
        if head == str('Manual'):
            heads = self.HandlingSlider.value()
        if self.actionLonLat.isChecked():
            if self.NorthEast.isChecked():
                (z, e, n) = LLtoUTM(ell, float(self.Lat.text()), float(self.Lon.text()))
                self.Nord.setText(str(n))
                self.East.setText(str(e))
                self.utmcode.setText(str(z))
        if Utils.haveGRASS_ != 0:
            if self.actionGrass.isChecked():
                if self.NorthEast.isChecked():
                    xy = getlonlat(self.fxvallon,self.fxvallat)
                    #xprint xy
        ossimxml =  Utils.makeActionTemplate(self.item, unicode(self.Lon.text()), unicode(self.Lat.text()), 
                                         self.ZoomSlider.value(), heads, self.PitchSlider.value(), 
                                         self.RollSlider.value(), self.RangeSlider.value())
        ossim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ossim.connect((host, int(nav)))  
        try:
            ossim.send(ossimxml)
            ossim.close()
        except:
            if not self.actionBroadcast.isChecked():
                self.CeckViewTypeState()
                
    def aggiorna(self):
        newlon = str(self.Lon.text())
        newlat = str(self.Lat.text())
        #'''
        try :
            if self.ViewType == 'LookAt':
                newlon = str(self.lookatLon.text())
                newlat = str(self.lookatLat.text())
                #xprint 'query mode set to LookAt'
        except :
            print 'query mode set to eye' #xprint
        #'''
        self.longitude.setText(newlon)
        self.latitude.setText(newlat)
        
    def connectPositonActions(self):
        # Send Position
        self.connect(self.SendPosition, SIGNAL("clicked()"),
                     self.SetLonLat)
        ##TBD self.connect(self.SendPosition, SIGNAL("clicked()"),
                     ##self.SetJoyCoords)
        self.connect(self.SendPosition, SIGNAL("clicked()"),
                     self.ResetPosition)
        """
        #TBD
        self.connect(self.RollSpinBox, SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeRoll)
        self.connect(self.PitchSpinBox, SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangePitch)
        self.connect(self.HandlingSpinBox, SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeHead)
        self.connect(self.ZoomSpinBox, SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeZoom)
        self.connect(self.RangeSpinBox, SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeRange)
        self.connect(self.actionSavekml, SIGNAL("triggered()"), 
                     self.kmldialog)
        """                                     
                                        
    def connectPanSignals(self):
        self.connect(self.center, SIGNAL("clicked()"),
                     self.ResetPosition)
        self.connect(self.north, SIGNAL("clicked()"),
                     self.inclat)
        self.connect(self.northeast, SIGNAL("clicked()"),
                     self.inclatlon)
        self.connect(self.south, SIGNAL("clicked()"),
                     self.declat)
        self.connect(self.east, SIGNAL("clicked()"),
                     self.inclon)
        self.connect(self.west, SIGNAL("clicked()"),
                     self.declon)
        self.connect(self.southwest, SIGNAL("clicked()"),
                     self.declatlon)
        self.connect(self.northwest, SIGNAL("clicked()"),
                     self.inclatdeclon)
        self.connect(self.southeast, SIGNAL("clicked()"),
                     self.declatinclon)

    def connectZoomSignals(self):
        # Zoom
        self.connect(self.ZoomSlider, SIGNAL("valueChanged(int)"), 
                     self.setValueZoomSpinBox)
        self.connect(self.ZoomSlider, SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.ZoomSpinBox, SIGNAL("valueChanged(double)"), 
                     self.setValueZoomSlider)
        self.connect(self.ZoomSpinBox, SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.ZoomSlider, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.ZoomSpinBox, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsZoom, SIGNAL("clicked()"),
                     self.Zoomceckbuttons)
        self.connect(self.hsZoom, SIGNAL("clicked()"),
                     self.hideslideZoom)
        self.ZoomSpinBox.setSuffix(' m')

    def connectRangeSignals(self):
        # Range
        self.connect(self.RangeSlider, SIGNAL("valueChanged(int)"), 
                     self.setValueRangeSpinBox)
        self.connect(self.RangeSlider, SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.RangeSpinBox, SIGNAL("valueChanged(double)"), 
                     self.setValueRangeSlider)
        self.connect(self.RangeSpinBox, SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.RangeSlider, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.RangeSpinBox, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsRange, SIGNAL("clicked()"),
                     self.Rangececkbuttons)
        self.connect(self.hsRange, SIGNAL("clicked()"),
                     self.hideslideRange)
        self.RangeSpinBox.setSuffix(' m')

    def connectRollSignals(self):        
        # Roll
        self.connect(self.RollSlider, SIGNAL("valueChanged(int)"), 
                     self.setValueRollSpinBox)
        self.connect(self.RollSlider, SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.RollSpinBox, SIGNAL("valueChanged(double)"), 
                     self.setValueRollSlider)
        self.connect(self.RollSpinBox, SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.RollSlider, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.RollSpinBox, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsRoll, SIGNAL("clicked()"),
                     self.Rollceckbuttons)
        self.connect(self.hsRoll, SIGNAL("clicked()"),
                     self.hideslideRoll)
        self.RollSpinBox.setSuffix('\xB0')
        
    def connectPitchSignals(self):        
        # Pitch
        self.connect(self.PitchSlider, SIGNAL("valueChanged(int)"), 
                     self.setValuePitchSpinBox)
        self.connect(self.PitchSlider, SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.PitchSpinBox, SIGNAL("valueChanged(double)"), 
                     self.setValuePitchSlider)
        self.connect(self.PitchSpinBox, SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.PitchSlider, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.PitchSpinBox, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsPitch, SIGNAL("clicked()"),
                     self.Pitchceckbuttons)
        self.connect(self.hsPitch, SIGNAL("clicked()"),
                     self.hideslidePitch)
        self.PitchSpinBox.setSuffix('\xB0')

        
    def connectHeadSignals(self):        
        # Head
        self.connect(self.HandlingSlider, SIGNAL("valueChanged(int)"), 
                     self.setValueHandlingSpinBox)
        self.connect(self.HandlingSlider, SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.HandlingSpinBox, SIGNAL("valueChanged(double)"), 
                     self.setValueHandlingSlider)
        self.connect(self.HandlingSpinBox, SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.HandlingSlider, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.HandlingSpinBox, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.Head, SIGNAL("currentIndexChanged(int)"),
                     self.GetHead)
        self.connect(self.hsHeading, SIGNAL("clicked()"),
                     self.Headingceckbuttons)
        self.connect(self.hsHeading, SIGNAL("clicked()"),
                     self.hideslideHead)
        self.HandlingSpinBox.setSuffix('\xB0')
        #self.connect(self.HandlingSlider, SIGNAL("valueChanged(int)"), 
        #             self.setValueHandlingSpinBox)

    def connectSpeedSignals(self):        
        # Speed
        self.connect(self.SpeedSpinBox, SIGNAL("valueChanged(double)"), 
                     self.setValueSpeedSpinBox)
        self.connect(self.SpeedSpinBox, SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.SpeedMultipler, SIGNAL("valueChanged(double)"), 
                     self.setValueSpeedMultipler)
        self.connect(self.SpeedMultipler, SIGNAL("valueChanged()"), 
                     self.setValueM)
        #self.SpeedSpinBox.setSuffix(' m')

    def connectZoomRangeSignals(self):        
        # Zoom/Range Step-Nultipler
        self.connect(self.ZoomStepSpinBox, SIGNAL("valueChanged()"), 
                     self.setValueZM)
        self.connect(self.RangeStepSpinBox, SIGNAL("valueChanged()"),
                     self.setValueRM)
        self.connect(self.ZoomMultipler, SIGNAL("valueChanged(double)"), 
                     self.setValueZoomMultipler)
        self.connect(self.ZoomMultipler, SIGNAL("valueChanged()"), 
                     self.setValueZ)
        self.connect(self.RangeMultipler, SIGNAL("valueChanged()"), 
                     self.setValueR)
                     


# Set Values Slider/SpinBox  
  
    def setValueZoomSpinBox(self, z):
        self.ZoomValue = float(z)
        self.ZoomSpinBox.setRange(-10000, 27536977)
        zstep = float(self.ZoomStepSpinBox.value())
        zmult = float(self.ZoomMultipler.value())
        zstep = zstep * (10 ** zmult)
        self.ZoomSpinBox.setSingleStep(zstep)
        self.ZoomSpinBox.setValue(self.ZoomValue)
    
    
    def setValueZoomSlider(self, z):
        self.ZoomValue = int(z)
        self.ZoomSlider.setMinimum(-10000)
        self.ZoomSlider.setMaximum(27536977)
        self.ZoomSlider.setValue(self.ZoomValue)
    
    
    def setValueRangeSpinBox(self, r):
        self.RangeValue = float(r)
        self.RangeSpinBox.setRange(-10000, 27536977)
        rstep = float(self.RangeStepSpinBox.value())
        rmult = float(self.RangeMultipler.value())
        rstep = rstep * (10 ** rmult)
        self.RangeSpinBox.setSingleStep(rstep)
        self.RangeSpinBox.setValue(self.RangeValue)
    
    
    def setValueRangeSlider(self, r):
        self.RangeValue = int(r)
        self.RangeSlider.setMinimum(-10000)
        self.RangeSlider.setMaximum(27536977)
        self.RangeSlider.setValue(self.RangeValue)
    
    
    def setValueRollSpinBox(self, rl):
        self.RollValue = float(rl)
        self.RollSpinBox.setRange(-90, 90)
        self.RollSpinBox.setSingleStep(1)
        self.RollSpinBox.setValue(self.RollValue)
        self.rotationRollSpinBox.setRange(-360, 360)
        self.rotationRollSpinBox.setSingleStep(1)
        self.rotationRollSpinBox.setValue(self.RollValue)
    
    
    def setValueRollSlider(self, rl):
        self.RollValue = int(rl)
        self.RollSlider.setMinimum(-90)
        self.RollSlider.setMaximum(90)
        self.RollSlider.setValue(self.RollValue)
    
    
    def setValuePitchSpinBox(self, p):
        self.PitchValue = float(p)
        self.PitchSpinBox.setRange(-90, 90)
        self.PitchSpinBox.setSingleStep(1)
        self.PitchSpinBox.setValue(self.PitchValue)
    
    
    def setValuePitchSlider(self, p):
        self.PitchValue = int(p)
        self.PitchSlider.setMinimum(-90)
        self.PitchSlider.setMaximum(90)
        self.PitchSlider.setValue(self.PitchValue)
    
    
    def setValueHandlingSpinBox(self, h):
        self.HandlingValue = float(h)
        self.HandlingSpinBox.setRange(-360, 360)
        self.HandlingSpinBox.setSingleStep(1)
        self.HandlingSpinBox.setValue(self.HandlingValue)
        self.rotationAngleSpinBox.setRange(-360, 360)
        self.rotationAngleSpinBox.setSingleStep(1)
        self.rotationAngleSpinBox.setValue(self.HandlingValue)
        
    
    
    def setValueHandlingSlider(self, h):
        self.HandlingValue = int(h)
        self.HandlingSlider.setMinimum(-360)
        self.HandlingSlider.setMaximum(360)
        self.HandlingSlider.setValue(self.HandlingValue)
    
    
    def setValueSpeedSpinBox(self, s):
        self.SpeedValue = float(s)
        self.SpeedSpinBox.setRange(0.01, 1)
        self.SpeedSpinBox.setSingleStep(0.01)
        self.SpeedSpinBox.setValue(self.SpeedValue)
    
    
    def setValueSpeedMultipler(self, s):
        self.SpeedM = float(s)
        self.SpeedMultipler.setRange(1, 10)
        self.SpeedMultipler.setSingleStep(1)
        self.SpeedMultipler.setValue(self.SpeedM)
    
    
    def setValueZoomMSpinBox(self, s):
        self.ZoomValue = float(s)
        self.ZoomSpinBox.setRange(0.01, 1)
        self.ZoomSpinBox.setSingleStep(0.01)
        self.ZoomSpinBox.setValue(self.ZoomValue)
    
    
    def setValueZoomMultipler(self, s):
        self.ZoomStepValue = float(s)
        self.ZoomMultipler.setRange(1, 10)
        self.ZoomMultipler.setSingleStep(1)
        self.ZoomMultipler.setValue(self.ZoomStepValue)
    
    def getViewVal(self):
        #lon,lat,zoom,heads,pitch,roll,range = 0,0,0,0,0,0,0
        pitch = self.PitchSlider.value()
        roll = self.RollSlider.value()
        rng = self.RangeSlider.value()
        zoom = self.ZoomSlider.value()
        heads = self.head
        lon = self.Lon.text()
        lat = self.Lat.text()
        if heads == str('Manual'):
            heads = self.HandlingSlider.value()
        if Utils.preferences().getSettings('actionLonLat'): #self.actionLonLat.isChecked():
            lat = self.fxvallat
            lon = self.fxvallon
            if self.northeast.isChecked():
                (z, e, n) = LLtoUTM(ell, lat, lon)
                self.Nord.setText(str(n))
                self.east.setText(str(e))
                self.utmcode.setText(str(z))
        """
        TBMV: to grass and gps window
        if Utils.haveGRASS_ != 0:
            if Utils.preferences().getSettings('actionGrass'): #self.actionGrass.isChecked():
                lon = self.slvallon
                lat = self.slvallat
                if self.northeast.isChecked():
                    xy = getlonlat(lon,lat)
                    self.Nord.setText(xy[1])
                    self.east.setText(xy[0])
        if Utils.preferences().getSettings('actionGPS'): #self.actionGPS.isChecked():
            lon = self.GPSlon.text()
            lat = self.GPSlat.text()
        """    
        pos = [lon,lat,zoom,heads,pitch,roll,rng]
        return pos
            
    def Jcoords(self):
        newlon = str(self.Lon.text())
        newlat = str(self.Lat.text())
        return newlon, newlat

    def sendFunction(self):
        if Utils.preferences().getSettings('actionLonLat'):
            pos = self.getViewVal()
            #xprint pos
            ossimxml =  Utils.makeActionTemplate(self.item, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6])
            self.fireAction(ossimxml)
            self.Lat.setText(unicode(pos[1]))
            self.Lon.setText(unicode(pos[0]))
            #print 'sendFunction commented'
    

    def ResetPosition(self):
        #xprint 'reset position'
        head = self.head
        if head == str('Manual'):
            self.heads = self.HandlingSlider.value()
        if Utils.preferences().getSettings('actionLonLat'):
            self.fxvallon = self.SetPosition()[0]
            self.fxvallat = self.SetPosition()[1]
            if self.northeast.isChecked():
                (z, e, n) = LLtoUTM(ell, self.fxvallat, self.fxvallon)
                self.Nord.setText(str(n))
                self.east.setText(str(e))
                self.utmcode.setText(str(z))
            ossimxml =  Utils.makeActionTemplate(self.item, unicode(self.fxvallon), unicode(self.fxvallat), 
                                             self.ZoomSlider.value(), 0, 0, 
                                             0, self.RangeSlider.value())
            self.Lat.setText(unicode(self.fxvallat))
            self.Lon.setText(unicode(self.fxvallon))
            self.fireAction(ossimxml)
        if Utils.haveGRASS_ != 0:
            if self.actionGrass.isChecked():
                self.slvallon = self.getCenter()[0]
                self.slvallat = self.getCenter()[1]
                #xprint self.slvallon, self.slvallat
                if self.northeast.isChecked():
                    xy = getlonlat(self.slvallon,self.slvallat)
                    self.Nord.setText(xy[1])
                    self.east.setText(xy[0])
            ossimxml =  Utils.makeActionTemplate(self.item, unicode(self.slvallon), unicode(self.slvallat), 
                                             self.ZoomSlider.value(), 0, 0, 
                                             0, self.RangeSlider.value())
            self.Lat.setText(unicode(self.slvallat))
            self.Lon.setText(unicode(self.slvallon))
            self.fireAction(ossimxml)
        if Utils.preferences().getSettings('actionGPS'):
            #self.CrossClassLon = float(self.CrossClassLon)
            #self.CrossClassLat = float(self.CrossClassLat)
            coordsfile = apppath+'/lonlatfile'
            f = open(coordsfile, "r")
            lonlat = f.readline()
            lonlat = lonlat.split(' ')
            lon = lonlat[0]
            lat = lonlat[1]
            ossimxml =  Utils.makeActionTemplate(self.item, lon, lat, self.ZoomSlider.value(), self.heads, 
                                             self.PitchSlider.value(), self.RollSlider.value(),
                                             self.RangeSlider.value())
            self.Lat.setText(unicode(self.CrossClassLat))
            self.Lon.setText(unicode(self.CrossClassLon))
            self.fireAction(ossimxml)
            
    

    def getCenter(self):
        #FIXME 
        lat = 0.0
        lon = 0.0
        return lon, lat
        
    def pan(self, action):
        step = float(self.SpeedSpinBox.value())
        mult = float(self.SpeedMultipler.value())
        step = step * (10 ** -mult)

        if Utils.preferences().getSettings('actionLonLat'):
            if action == 'inclat' :
                self.fxvallat += step
            if action == 'inclon' :
                self.fxvallon += step
            if action == 'declat' :
                self.fxvallat -= step
            if action == 'declon' :
                self.fxvallon -= step
            if action == 'inclatlon' :
                self.fxvallat += step
                self.fxvallon += step
            if action == 'declatlon' :
                self.fxvallat -= step
                self.fxvallon -= step
            if action == 'inclatdeclon' :
                self.fxvallat += step
                self.fxvallon -= step
            if action == 'declatinclon' :
                self.fxvallat -= step 
                self.fxvallon += step
        if Utils.haveGRASS_ != 0:
            if self.actionGrass.isChecked():
                if action == 'inclat' :
                    self.slvallat += step
                if action == 'inclon' :
                    self.slvallon += step
                if action == 'declat' :
                    self.slvallat -= step
                if action == 'declon' :
                    self.slvallon -= step
                if action == 'inclatlon' :
                    self.slvallat += step
                    self.slvallon += step
                if action == 'declatlon' :
                    self.slvallat -= step
                    self.slvallon -= step
                if action == 'inclatdeclon' :
                    self.slvallat += step
                    self.slvallon -= step
                if action == 'declatinclon' :
                    self.slvallat -= step 
                    self.slvallon += step
        pos = self.getViewVal()
        ossimxml =  Utils.makeActionTemplate(self.item, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6])
        self.fireAction(ossimxml)
        self.Lat.setText(unicode(pos[1]))
        self.Lon.setText(unicode(pos[0]))


    def CeckViewTypeState(self):
        if not Utils.preferences().getSettings('actionLonLat'): #self.actionLonLat.isChecked():
            if Utils.haveGRASS_ !=0:
                if not Utils.preferences().getSettings('actionGrass'): #self.actionGrass.isChecked():
                    #self.worningmessage('check a view type')
                    x = 1
                    #FIXME
                    
    def fireAction(self, xml):
        result = Utils.fireAction(xml)
        if result < 0:
                if not Utils.preferences().getSettings('actionBroadcast'):#self.actionBroadcast.isChecked(): FIXME
                    self.CeckViewTypeState()
             
        
    def inclat(self):
        self.pan('inclat')

    def inclon(self):
        self.pan('inclon')

    def declat(self):
        self.pan('declat')

    def declon(self):
        self.pan('declon')

    def inclatlon(self):
        self.pan('inclatlon')

    def declatlon(self):
        self.pan('declatlon')

    def inclatdeclon(self):
        self.pan('inclatdeclon')

    def declatinclon(self):
        self.pan('declatinclon')
    
# Set Cross Widget Values
    
    def setValue(self, v):
        self.Value = v
    
    
    def setValueM(self, v):
        self.Value = v
    
    
    def setValueZ(self, v):
        self.Value = v
    
    
    def setValueR(self, v):
        self.Value = v
    
    
    def setValueRM(self, v):
        self.Value = v
    
    
    def setValueZM(self, v):
        self.Value = v
    
    
# Set ellipsoid (for UTM display)
    
    def ellipsesettings(self,index):
        global ell
        ell = self.ellipse.itemText(index)
        if ell == 'Airy':
            ell = 1
        if ell == 'Australian National':
            ell = 2
        if ell == 'Bessel 1841':
            ell = 3
        if ell == 'Bessel 1841 (Nambia)':
            ell = 4
        if ell == 'Clarke 1866':
            ell = 5
        if ell == 'Clarke 1880':
            ell = 6
        if ell == 'Everest':
            ell = 7
        if ell == 'Fischer 1960 (Mercury)':
            ell = 8
        if ell == 'Fischer 1968':
            ell = 9
        if ell == 'GRS 1967':
            ell = 10
        if ell == 'GRS 1980':
            ell = 11
        if ell == 'Helmert 1906':
            ell = 12
        if ell == 'Hough':
            ell = 13
        if ell == 'International':
            ell = 14
        if ell == 'Krassovsky':
            ell = 15
        if ell == 'Modified Airy':
            ell = 16
        if ell == 'Modified Everest':
            ell = 17
        if ell == 'Modified Fischer 1960':
            ell = 18
        if ell == 'South American 1969':
            ell = 19
        if ell == 'WGS 60':
            ell = 20
        if ell == 'WGS 66':
            ell = 21
        if ell == 'WGS-72':
            ell = 22
        if ell == 'WGS-84':
            ell = 23
        return ell
    

    
    def SetPosition(self):
        #global centro
        lon = 0
        lat = 0
        if not self.Lat.text() == "" and not self.Lon.text() == "":
            lon = str(self.Lon.text())
            lat = str(self.Lat.text())
        centro = (float(lon),float(lat))
        return centro
    
    
    def PrintPosition(self, lon, lat, zoom, roll, pitch, heading, rng):
        testo = '''Longitude : %s
        Latitude : %s 
        Altitude : %s
        Heading : %s
        Roll : %s
        Pitch : %s
        Range : %s
        ''' % (lon, lat, zoom, roll, pitch, heading, rng)


# Set Heading Mode    
    
    def GetHead(self,index):
        #global head
        head = self.Head.itemText(index)
        #xprint head
        if head == 'N':
            self.head = '0'
        if head == 'NE':
            self.head = '45' 
        if head == 'E':
            self.head = '90'
        if head == 'SE':
            self.head = '135'
        if head == 'S':
            self.head = '180'
        if head == 'SW':
            self.head = '-135'
        if head == 'W':
            self.head = '-90'
        if head == 'NW':
            self.head = '-45'
        if head == 'Auto':
            self.head = 'angle'
        if head == 'Manual':
            self.head = 'Manual'
        return self.head
    
    
# Set View Type
    
    def GetViewType(self,index):
        ViewT = self.View.itemText(index)
        zoomV = self.ZoomSlider.value()
        rangeV = self.RangeSlider.value()
        self.ViewType = ViewT
        if ViewT == 'Camera':
            #xprint 'Camera'
            self.RangeSlider.setValue(0)
            self.RangeSpinBox.setValue(0)
            self.ZoomSpinBox.setValue(rangeV)
            self.ZoomSlider.setValue(rangeV)
        if ViewT == 'LookAt':
            #xprint 'LookAt'
            self.ZoomSpinBox.setValue(0)
            self.ZoomSlider.setValue(0)
            self.RangeSlider.setValue(zoomV)
            self.RangeSpinBox.setValue(zoomV)
        return ViewT


    def Headingceckbuttons(self):
        self.hsPitch.setChecked(False)
        self.hsRoll.setChecked(False)
    
    
    def Pitchceckbuttons(self):
        self.hsHeading.setChecked(False)
        self.hsRoll.setChecked(False)
    
    
    def Rollceckbuttons(self):
        self.hsHeading.setChecked(False)
        self.hsPitch.setChecked(False)
    
    
    def hideslideHead(self):
        if self.hsHeading.isChecked():
            self.PitchSlider.hide()
            self.RollSlider.hide()
            self.HandlingSlider.show()
        else :
            self.HandlingSlider.hide()
            self.PitchSlider.hide()
            self.RollSlider.hide()
    
    
    def hideslidePitch(self):
        if self.hsPitch.isChecked():
            self.HandlingSlider.hide()
            self.RollSlider.hide()
            self.PitchSlider.show()
        else :
            self.HandlingSlider.hide()
            self.PitchSlider.hide()
            self.RollSlider.hide()
    
    
    def hideslideRoll(self):
        if self.hsRoll.isChecked():
            self.HandlingSlider.hide()
            self.PitchSlider.hide()
            self.RollSlider.show()
        else :
            self.HandlingSlider.hide()
            self.PitchSlider.hide()
            self.RollSlider.hide()
    
            
    def Zoomceckbuttons(self):
        self.hsRange.setChecked(False)
    
    
    def Rangececkbuttons(self):
        self.hsZoom.setChecked(False)
    
        
    def hideslideZoom(self):
        if self.hsZoom.isChecked():
            self.RangeSlider.hide()
            self.ZoomSlider.show()
        else :
            self.RangeSlider.hide()
            self.ZoomSlider.hide()
    
    
    def hideslideRange(self):
        if self.hsRange.isChecked():
            self.ZoomSlider.hide()
            self.RangeSlider.show()
        else :
            self.RangeSlider.hide()
            self.ZoomSlider.hide()
    
    
