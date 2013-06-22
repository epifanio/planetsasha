# -*- coding: utf-8 -*-

#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from Savekml import KmlView
from model import PlaceModel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

from Utils import Utils

from drawer import *


class NavigationWindow(QtGui.QTabWidget):
    def __init__(self, parent = None):

        self.parent = parent
        QtGui.QWidget.__init__(self, parent)
        self.kmlview = KmlView()
        self.placemodel = PlaceModel()
        self.setupUi()
        self.retranslateUi()
        

        #spinbox
        self.ZoomSpinBox.setValue(0)
        self.RangeSpinBox.setValue(100000)
        
        #slider
        self.ZoomSlider.setValue(0)
        self.RangeSlider.setValue(100000)
     
                
        self.Head.setCurrentIndex(1)

        self.Lon.setText("0")
        self.Lat.setText("0")

        self.RollSlider.hide()
        self.PitchSlider.hide()
        self.HandlingSlider.hide()
        self.ZoomSlider.hide()
        self.RangeSlider.hide()

        self.north.setAutoRepeat(True)
        self.northeast.setAutoRepeat(True)
        self.south.setAutoRepeat(True)
        self.east.setAutoRepeat(True)
        self.west.setAutoRepeat(True)
        self.southwest.setAutoRepeat(True)
        self.northwest.setAutoRepeat(True)
        self.southeast.setAutoRepeat(True)        
        
        self.head = 'Manual'  #FIXME
        
        if Utils.haveGRASS == 0:
            self.actionGrass.setEnabled(False)
            self.actionGrass.setVisible(False)           
        
        self.item = self.GetViewType(0)
        self.ZoomSpinBox.setSuffix(' m')
        self.connectSignals()
        

    def connectSignals(self):

        self.connect(self.ZoomSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.setValueZoomSpinBox)
        self.connect(self.ZoomSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.ZoomSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.setValueZoomSlider)
        self.connect(self.ZoomSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.ZoomSlider, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.ZoomSpinBox, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsZoom, QtCore.SIGNAL("clicked()"),
                     self.Zoomceckbuttons)
        self.connect(self.hsZoom, QtCore.SIGNAL("clicked()"),
                     self.hideslideZoom)

        # Coordinate Display UTM
        self.connect(self.ellipse, QtCore.SIGNAL("currentIndexChanged(int)"),
                     self.ellipsesettings)
        # View Type
        self.connect(self.View, QtCore.SIGNAL("currentIndexChanged(int)"),
                     self.GetViewType)                     



        # Range
        self.connect(self.RangeSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.setValueRangeSpinBox)
        self.connect(self.RangeSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.RangeSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.setValueRangeSlider)
        self.connect(self.RangeSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.RangeSlider, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.RangeSpinBox, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsRange, QtCore.SIGNAL("clicked()"),
                     self.Rangececkbuttons)
        self.connect(self.hsRange, QtCore.SIGNAL("clicked()"),
                     self.hideslideRange)
        self.RangeSpinBox.setSuffix(' m')
        # Roll
        
        
        
        self.connect(self.RollSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.setValueRollSpinBox)
        self.connect(self.RollSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.RollSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.setValueRollSlider)
        self.connect(self.RollSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.RollSlider, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.RollSpinBox, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsRoll, QtCore.SIGNAL("clicked()"),
                     self.Rollceckbuttons)
        self.connect(self.hsRoll, QtCore.SIGNAL("clicked()"),
                     self.hideslideRoll)
        self.RollSpinBox.setSuffix('\xB0')
        # Pitch
        self.connect(self.PitchSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.setValuePitchSpinBox)
        self.connect(self.PitchSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.PitchSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.setValuePitchSlider)
        self.connect(self.PitchSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.PitchSlider, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.PitchSpinBox, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.hsPitch, QtCore.SIGNAL("clicked()"),
                     self.Pitchceckbuttons)
        self.connect(self.hsPitch, QtCore.SIGNAL("clicked()"),
                     self.hideslidePitch)
        self.PitchSpinBox.setSuffix('\xB0')
        # Head
        self.connect(self.HandlingSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.setValueHandlingSpinBox)
        self.connect(self.HandlingSlider, QtCore.SIGNAL("valueChanged(int)"), 
                     self.sendFunction)
        self.connect(self.HandlingSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.setValueHandlingSlider)
        self.connect(self.HandlingSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.sendFunction)
        self.connect(self.HandlingSlider, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.HandlingSpinBox, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.Head, QtCore.SIGNAL("currentIndexChanged(int)"),
                     self.GetHead)
        self.connect(self.hsHeading, QtCore.SIGNAL("clicked()"),
                     self.Headingceckbuttons)
        self.connect(self.hsHeading, QtCore.SIGNAL("clicked()"),
                     self.hideslideHead)
        self.HandlingSpinBox.setSuffix('\xB0')
        #self.connect(self.HandlingSlider, QtCore.SIGNAL("valueChanged(int)"), 
        #             self.setValueHandlingSpinBox)
        # Speed
        self.connect(self.SpeedSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.setValueSpeedSpinBox)
        self.connect(self.SpeedSpinBox, QtCore.SIGNAL("valueChanged()"), 
                     self.setValue)
        self.connect(self.SpeedMultipler, QtCore.SIGNAL("valueChanged(double)"), 
                     self.setValueSpeedMultipler)
        self.connect(self.SpeedMultipler, QtCore.SIGNAL("valueChanged()"), 
                     self.setValueM)
                     
                     
        self.connect(self.center, QtCore.SIGNAL("clicked()"),
                     self.ResetPosition)
        self.connect(self.north, QtCore.SIGNAL("clicked()"),
                     self.inclat)
        self.connect(self.northeast, QtCore.SIGNAL("clicked()"),
                     self.inclatlon)
        self.connect(self.south, QtCore.SIGNAL("clicked()"),
                     self.declat)
        self.connect(self.east, QtCore.SIGNAL("clicked()"),
                     self.inclon)
        self.connect(self.west, QtCore.SIGNAL("clicked()"),
                     self.declon)
        self.connect(self.southwest, QtCore.SIGNAL("clicked()"),
                     self.declatlon)
        self.connect(self.northwest, QtCore.SIGNAL("clicked()"),
                     self.inclatdeclon)
        self.connect(self.southeast, QtCore.SIGNAL("clicked()"),
                     self.declatinclon)


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
        # ACTIONS
        # GPS
        self.connect(self.actionGPS, SIGNAL("triggered()"), 
                     self.startstopgpsx)	
        self.connect(self.actionGPS, SIGNAL("triggered()"), 
                     self.GPSunceckbuttons)
        self.connect(self.actionGPS, SIGNAL("triggered()"), 
                     self.stopstartgpsx)
        #self.connect(self.actionNMEA, SIGNAL("triggered()"),
        #             self.GpsHandling)
        #self.connect(self.actionGPS, SIGNAL("triggered()"),
        #             self.GpsHandling)
        # LON LAT
        self.connect(self.actionLonLat, SIGNAL("triggered()"),
                     self.LonLatunceckbuttons)
        # GRASS
        #self.connect(self.actionGrass, SIGNAL("triggered()"),
        #             self.Grassunceckbuttons)



        # View Type
        self.connect(self.View, SIGNAL("currentIndexChanged(int)"),
                     self.GetViewType)

        self.connect(self.SendPosition, SIGNAL("clicked()"),
                     self.SetJoyCoords)
        self.connect(self.SendPosition, SIGNAL("clicked()"),
                     self.ResetPosition)
                     
        self.connect(self.RollSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeRoll)
        self.connect(self.PitchSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangePitch)
        self.connect(self.HandlingSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeHead)
        self.connect(self.ZoomSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeZoom)
        self.connect(self.RangeSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.kmlview.setChangeRange)
# Place Model (send position to save kml model)
        self.connect(self.Lon, QtCore.SIGNAL("textChanged(QString)"), 
                     self.placemodel.setLonValue)
        self.connect(self.Lat, QtCore.SIGNAL("textChanged(QString)"), 
                     self.placemodel.setLatValue)
        self.connect(self.RollSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeRoll)
        self.connect(self.PitchSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangePitch)
        self.connect(self.HandlingSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeHead)
        self.connect(self.ZoomSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeZoom)
        self.connect(self.RangeSpinBox, QtCore.SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeRange)       
                     

    
# Set ellipsoid (for UTM display)
    
    def ellipsesettings(self,index):
        global ell
        ell = self.w.ellipse.itemText(index)
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
    

       
                           

    def SetJoyCoords(self):
        if self.actionJoystick.isChecked():
            a = self.Lon.text()
            b = self.Lat.text()
            aa = float(a) + 1
            bb = float(b) + 1
            self.Lon.setText(str(aa))
            self.Lat.setText(str(bb))
            self.Lon.setText(str(a))
            self.Lat.setText(str(b))

    
    def LonLatunceckbuttons(self):
        if self.actionGPS.isChecked():
            self.gpsx.stop()
            self.actionGPS.setChecked(False)
        if Utils.haveGRASS != 0:
            self.actionGrass.setChecked(False)
        if self.actionJoystick.isChecked():
            self.joy.stop()
            self.actionJoystick.setChecked(False)
        if self.actionHW.isChecked():
            self.hw.stop()
            self.actionHW.setChecked(False)
    
    
    def Grassunceckbuttons(self):
        if self.actionGPS.isChecked():
            self.gpsx.stop()
            self.actionGPS.setChecked(False)
        self.actionLonLat.setChecked(False)
        if self.actionJoystick.isChecked():
            self.joy.stop()
            self.actionJoystick.setChecked(False)
        if self.actionHW.isChecked():
            self.hw.stop()
            self.actionHW.setChecked(False)
    

    

        

    

    def GPSunceckbuttons(self):
        self.actionLonLat.setChecked(False)
        if Utils.haveGRASS != 0:
            self.actionGrass.setChecked(False)
        if self.actionJoystick.isChecked():
            self.joy.stop()
            self.actionJoystick.setChecked(False)
        if self.actionHW.isChecked():
            self.hw.stop()
            self.actionHW.setChecked(False)
        #if self.actionSerial.isChecked():


    def startstopgpsx(self):
        if self.actionGPS.isChecked():
            self.gpsx = GpsT()
            self.gpsx.start()
            self.gpsx.GPSlatitude.connect(self.GPSlat.setText)
            self.gpsx.GPSlongitude.connect(self.GPSlon.setText)
            self.gpsx.GPStime.connect(self.GPSTime.setText)
            self.gpsx.GPSutctime.connect(self.GPSUtctime.setText)
            self.gpsx.GPSaltitude.connect(self.GPSAltitude.setText)
            self.gpsx.GPSspeed.connect(self.GPSSpeed.setText)
            self.gpsx.GPStrack.connect(self.GPSTrack.setText)
            self.gpsx.GPSclimb.connect(self.GPSClimb.setText)
            self.gpsx.GPSeph.connect(self.GPSEph.setText)
            self.gpsx.GPSept.connect(self.GPSEpt.setText)
            self.gpsx.GPSepv.connect(self.GPSEpv.setText)
            self.gpsx.GPSepd.connect(self.GPSEpd.setText)
            self.gpsx.GPSepc.connect(self.GPSEpc.setText)
            self.gpsx.GPSeps.connect(self.GPSEps.setText)
            self.gpsx.GPSpdop.connect(self.GPSPdop.setText)
            self.gpsx.GPShdop.connect(self.GPSHdop.setText)
            self.gpsx.GPSvdop.connect(self.GPSVdop.setText)
            self.gpsx.GPStdop.connect(self.GPSTdop.setText)
            self.gpsx.GPSgdop.connect(self.GPSGdop.setText)
            self.gpsx.GPSsat.connect(self.Satellite.setText)
            print self.GPSlat.text()
            #print 'qualcosa'
            #if head == str('Manual'):
            #    heads = self.HandlingSlider.value()
            #if head == str('Auto'):
            #    heads = self.GPSTrack
            #print heads
            head = 'Manual'
            self.gpsx.toggle()
        else :
            self.gpsx.stop()
    
    
    def stopstartgpsx(self):
        if not self.actionGPS.isChecked():
            self.gpsx = GpsT()
            #self.gpsx.wait()
            self.gpsx.stop()
            self.gpsx.toggle()
                         

    def pan(self, action):

        step = float(self.SpeedSpinBox.value())
        mult = float(self.SpeedMultipler.value())
        step = step * (10 ** -mult)
        if self.actionLonLat.isChecked():
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
        if Utils.haveGRASS != 0:
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
        pos = self.getViewVal() #FIXME
        ossimxml = Utils.makeactiontemplate(self.item, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6]) #FIXME
        Utils.MakeConection(ossimxml) #FIXME
        self.Lat.setText(unicode(pos[1]))
        self.Lon.setText(unicode(pos[0]))

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
                     
                                          
                     
    def setValueHandlingSpinBox(self, h):
        self.HandlingValue = float(h)
        self.HandlingSpinBox.setRange(-360, 360)
        self.HandlingSpinBox.setSingleStep(1)
        self.HandlingSpinBox.setValue(self.HandlingValue)
        self.rotationAngleSpinBox.setRange(-360, 360)
        self.rotationAngleSpinBox.setSingleStep(1)
        self.rotationAngleSpinBox.setValue(self.HandlingValue)


    def setValueRollSpinBox(self, rl):
        self.RollValue = float(rl)
        self.RollSpinBox.setRange(-90, 90)
        self.RollSpinBox.setSingleStep(1)
        self.RollSpinBox.setValue(self.RollValue)
        self.rotationRollSpinBox.setRange(-360, 360)
        self.rotationRollSpinBox.setSingleStep(1)
        self.rotationRollSpinBox.setValue(self.RollValue)
            
    def hideslideZoom(self):
        if self.hsZoom.isChecked():
            self.RangeSlider.hide()
            self.ZoomSlider.show()
        else :
            self.RangeSlider.hide()
            self.ZoomSlider.hide()
    

    def sendFunction(self):
        pos = self.getViewVal()
        #print pos
        ossimxml = Utils.makeactiontemplate(self.item, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6])
        Utils.MakeConection(ossimxml)
        self.Lat.setText(unicode(pos[1]))
        self.Lon.setText(unicode(pos[0]))
        print 'sendFunction'                   


    def Zoomceckbuttons(self):
        self.hsRange.setChecked(False)
        
    def Rangececkbuttons(self):
        self.hsZoom.setChecked(False)   
# Hide/Show widget
    
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
    
            


    
    def hideslideRange(self):
        if self.hsRange.isChecked():
            self.ZoomSlider.hide()
            self.RangeSlider.show()
        else :
            self.RangeSlider.hide()
            self.ZoomSlider.hide()
            


    
# Set Heading Mode    
    
    def GetHead(self,index):
        #global head
        head = self.Head.itemText(index)
        print head
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
        print "pitch slider"
        self.PitchValue = int(p)
        self.PitchSlider.setMinimum(-90)
        self.PitchSlider.setMaximum(90)
        self.PitchSlider.setValue(self.PitchValue)

    def setValueHandlingSlider(self, h):
        self.HandlingValue = int(h)
        self.HandlingSlider.setMinimum(-360)
        self.HandlingSlider.setMaximum(360)
        self.HandlingSlider.setValue(self.HandlingValue)
    
    
    def setValueSpeedSpinBox(self, s):
        print "setValueSpeedSpinBox"
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
            
    def GetViewType(self,index):
        ViewT = self.View.itemText(index)
        zoomV = self.ZoomSlider.value()
        rangeV = self.RangeSlider.value()
        self.ViewType = ViewT
        if ViewT == 'Camera':
            print 'Camera'
            self.RangeSlider.setValue(0)
            self.RangeSpinBox.setValue(0)
            self.ZoomSpinBox.setValue(rangeV)
            self.ZoomSlider.setValue(rangeV)
        if ViewT == 'LookAt':
            print 'LookAt'
            self.ZoomSpinBox.setValue(0)
            self.ZoomSlider.setValue(0)
            self.RangeSlider.setValue(zoomV)
            self.RangeSpinBox.setValue(zoomV)
        return ViewT

    def getViewVal(self):
        #lon,lat,zoom,heads,pitch,roll,range = 0,0,0,0,0,0,0
        pitch = self.PitchSlider.value()
        roll = self.RollSlider.value()
        range = self.RangeSlider.value()
        zoom = self.ZoomSlider.value()
        heads = self.head
        lon = self.Lon.text()
        lat = self.Lat.text()
        if heads == str('Manual'):
            heads = self.HandlingSlider.value()
        if self.actionLonLat.isChecked():
            lat = self.fxvallat
            lon = self.fxvallon
            if self.NorthEast.isChecked():
                (z, e, n) = LLtoUTM(ell, lat, lon)
                self.Nord.setText(str(n))
                self.East.setText(str(e))
                self.utmcode.setText(str(z))

        pos = [lon,lat,zoom,heads,pitch,roll,range]
        return pos


    def ResetPosition(self):
        print 'reset position'
        head = self.head
        if head == str('Manual'):
            self.heads = self.HandlingSlider.value()
        if self.actionLonLat.isChecked():
            self.fxvallon = self.SetPosition()[0]
            self.fxvallat = self.SetPosition()[1]
            if self.NorthEast.isChecked():
                (z, e, n) = LLtoUTM(ell, self.fxvallat, self.fxvallon)
                self.Nord.setText(str(n))
                self.East.setText(str(e))
                self.utmcode.setText(str(z))
            ossimxml = Utils.makeactiontemplate(self.item, unicode(self.fxvallon), unicode(self.fxvallat), 
                                             self.ZoomSlider.value(), 0, 0, 
                                             0, self.RangeSlider.value())
            self.Lat.setText(unicode(self.fxvallat))
            self.Lon.setText(unicode(self.fxvallon))
            self.MakeConection(ossimxml)
        if Utils.haveGRASS != 0:
            if self.actionGrass.isChecked():
                self.slvallon = setcenter()[0]
                self.slvallat = setcenter()[1]
                print self.slvallon, self.slvallat
                if self.NorthEast.isChecked():
                    xy = getlonlat(self.slvallon,self.slvallat)
                    self.Nord.setText(xy[1])
                    self.East.setText(xy[0])
            ossimxml = Utils.makeactiontemplate(self.item, unicode(self.slvallon), unicode(self.slvallat), 
                                             self.ZoomSlider.value(), 0, 0, 
                                             0, self.RangeSlider.value())
            self.Lat.setText(unicode(self.slvallat))
            self.Lon.setText(unicode(self.slvallon))
            Utils.MakeConection(ossimxml)
        if self.actionGPS.isChecked():
            #self.CrossClassLon = float(self.CrossClassLon)
            #self.CrossClassLat = float(self.CrossClassLat)
            coordsfile = apppath+'/lonlatfile'
            f = open(coordsfile, "r")
            lonlat = f.readline()
            lonlat = lonlat.split(' ')
            lon = lonlat[0]
            lat = lonlat[1]
            ossimxml = Utils.makeactiontemplate(self.item, lon, lat, self.ZoomSlider.value(), self.heads, 
                                             self.PitchSlider.value(), self.RollSlider.value(),
                                             self.RangeSlider.value())
            self.Lat.setText(unicode(self.CrossClassLat))
            self.Lon.setText(unicode(self.CrossClassLon))
            Utils.MakeConection(ossimxml)
            

    def createRollWidget(self):
        self.dockWidget_3 = QtGui.QDockWidget(self)   
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        roll_widget = DrawRoll(self.dockWidget_3)
        self.rotationRollSpinBox = QSpinBox()
        self.rotationRollSpinBox.setRange(0, 359)
        self.rotationRollSpinBox.setWrapping(True)
        self.rotationRollSpinBox.setSuffix('\xB0')
        self.rotationRollLabel = QLabel("&Roll:")
        self.rotationRollLabel.setBuddy(self.rotationRollLabel)
        self.verticalLayout_18.addWidget(roll_widget)
        self.HLayoutRoll = QHBoxLayout()
        self.HLayoutRoll.addWidget(self.rotationRollLabel)
        self.HLayoutRoll.addWidget(self.rotationRollSpinBox)
        self.verticalLayout_18.addLayout(self.HLayoutRoll)
        self.rotationRollSpinBox.valueChanged.connect(roll_widget.setRotationAngle)
        self.rotationRollSpinBox.hide()
        self.rotationRollLabel.hide()
        self.verticalLayout_3.addLayout(self.verticalLayout_18)
        self.dockWidget_3.setWidget(self.dockWidgetContents)
        return self.dockWidget_3                                                          

    def createHeadingWidget(self):   
        self.dockWidget_2 = QtGui.QDockWidget(self)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))

        compass_widget = DrawCompass(self.dockWidget_2)
        #roll_widget = DrawRoll(self)
        self.rotationAngleSpinBox = QSpinBox()
        self.rotationAngleSpinBox.setRange(0, 359)
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix('\xB0')
        self.rotationAngleLabel = QLabel("&Heading:")
        self.rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)
        self.verticalLayout_8.addWidget(compass_widget)
        self.HLayout = QHBoxLayout()
        self.HLayout.addWidget(self.rotationAngleLabel)
        self.HLayout.addWidget(self.rotationAngleSpinBox)
        self.verticalLayout_8.addLayout(self.HLayout)
        self.rotationAngleSpinBox.valueChanged.connect(compass_widget.setRotationAngle)
        self.rotationAngleSpinBox.hide()
        self.rotationAngleLabel.hide()        
        self.verticalLayout_21.addLayout(self.verticalLayout_8)
        self.dockWidget_2.setWidget(self.dockWidgetContents_3)
        return self.dockWidget_2
        
    def setupUi(self):        
        self.setObjectName(_fromUtf8("tab"))
        self.hLayout = QtGui.QHBoxLayout(self)
        
        self.dockLayout = QtGui.QVBoxLayout()
        self.panbox = self.createPanToolBox()
        self.headingWidget = self.createHeadingWidget()
        self.rollWidget = self.createRollWidget()
        self.dockLayout.addWidget(self.panbox)
        self.dockLayout.addWidget(self.headingWidget)
        self.dockLayout.addWidget(self.rollWidget)
        self.hLayout.addLayout(self.dockLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hLayout.addLayout(self.verticalLayout) # = QtGui.QHBoxLayout()
        #self.hLayout.addWidget(self.setupPanToolBox())
        #self.verticalLayout.addLayout(self.hLayout)
        
        
        self.scrollArea_4 = QtGui.QScrollArea(self)
        self.scrollArea_4.setStyleSheet(_fromUtf8(""))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))

        #scrollarea
        self.navScrollArea = QtGui.QWidget()
        self.navScrollArea.setGeometry(QtCore.QRect(0, 0, 541, 645))
        self.navScrollArea.setObjectName(_fromUtf8("navScrollArea"))
        
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.navScrollArea)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        
        self.line_8 = QtGui.QFrame(self.navScrollArea)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_5.addWidget(self.line_8)
        
        
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.navScrollArea)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        
        self.Lat = QtGui.QLineEdit(self.navScrollArea)
        self.Lat.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Lat.setAlignment(QtCore.Qt.AlignCenter)
        self.Lat.setObjectName(_fromUtf8("Lat"))
        self.horizontalLayout_6.addWidget(self.Lat)
        self.Lon = QtGui.QLineEdit(self.navScrollArea)
        self.Lon.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Lon.setAlignment(QtCore.Qt.AlignCenter)
        self.Lon.setObjectName(_fromUtf8("Lon"))
        self.horizontalLayout_6.addWidget(self.Lon)
        self.Alt = QtGui.QLineEdit(self.navScrollArea)
        self.Alt.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Alt.setObjectName(_fromUtf8("Alt"))
        self.horizontalLayout_6.addWidget(self.Alt)
        
        
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.line_5 = QtGui.QFrame(self.navScrollArea)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_5.addWidget(self.line_5)
        
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.navScrollArea)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        
        self.lookatLat = QtGui.QLineEdit(self.navScrollArea)
        self.lookatLat.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.lookatLat.setObjectName(_fromUtf8("lookatLat"))
        self.horizontalLayout_5.addWidget(self.lookatLat)
        self.lookatLon = QtGui.QLineEdit(self.navScrollArea)
        self.lookatLon.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.lookatLon.setObjectName(_fromUtf8("lookatLon"))
        self.horizontalLayout_5.addWidget(self.lookatLon)
        
        self.lookatAlt = QtGui.QLineEdit(self.navScrollArea)
        self.lookatAlt.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.lookatAlt.setObjectName(_fromUtf8("lookatAlt"))
        self.horizontalLayout_5.addWidget(self.lookatAlt)
        
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        
        self.line_9 = QtGui.QFrame(self.navScrollArea)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout_5.addWidget(self.line_9)
        
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        
        self.label_9 = QtGui.QLabel(self.navScrollArea)
        self.label_9.setMinimumSize(QtCore.QSize(50, 0))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_11.addWidget(self.label_9)
        
        self.NorthEast = QtGui.QCheckBox(self.navScrollArea)
        self.NorthEast.setText(_fromUtf8(""))
        self.NorthEast.setObjectName(_fromUtf8("NorthEast"))
        self.horizontalLayout_11.addWidget(self.NorthEast)
        
        
        self.Nord = QtGui.QLineEdit(self.navScrollArea)
        self.Nord.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.Nord.setAlignment(QtCore.Qt.AlignCenter)
        self.Nord.setObjectName(_fromUtf8("Nord"))
        self.horizontalLayout_11.addWidget(self.Nord)
        
        
        self.East = QtGui.QLineEdit(self.navScrollArea)
        self.East.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.East.setAlignment(QtCore.Qt.AlignCenter)
        self.East.setObjectName(_fromUtf8("East"))
        self.horizontalLayout_11.addWidget(self.East)
        
        self.label_11 = QtGui.QLabel(self.navScrollArea)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_11.addWidget(self.label_11)
        
        self.utmcode = QtGui.QLineEdit(self.navScrollArea)
        self.utmcode.setMinimumSize(QtCore.QSize(45, 0))
        self.utmcode.setMaximumSize(QtCore.QSize(45, 16777215))
        self.utmcode.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }"))
        self.utmcode.setText(_fromUtf8(""))
        self.utmcode.setAlignment(QtCore.Qt.AlignCenter)
        self.utmcode.setObjectName(_fromUtf8("utmcode"))
        self.horizontalLayout_11.addWidget(self.utmcode)
        
        self.ellipse = QtGui.QComboBox(self.navScrollArea)
        self.ellipse.setMaximumSize(QtCore.QSize(150, 26))
        self.ellipse.setStyleSheet(_fromUtf8(""))
        self.ellipse.setObjectName(_fromUtf8("ellipse"))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.ellipse.addItem(_fromUtf8(""))
        self.horizontalLayout_11.addWidget(self.ellipse)
        
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        
        
        

        self.line_10 = QtGui.QFrame(self.navScrollArea)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.verticalLayout_5.addWidget(self.line_10)
        
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        
        self.Place = QtGui.QComboBox(self.navScrollArea)
        self.Place.setStyleSheet(_fromUtf8(""))
        self.Place.setObjectName(_fromUtf8("Place"))
        self.Place.addItem(_fromUtf8(""))
        self.Place.setItemText(0, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.Place)
        
        self.line_17 = QtGui.QFrame(self.navScrollArea)
        self.line_17.setFrameShape(QtGui.QFrame.VLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.horizontalLayout_3.addWidget(self.line_17)
        
        self.actionJoystick = QtGui.QAction(self)
        self.actionJoystick.setCheckable(True)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/joystick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJoystick.setIcon(icon22)
        self.actionJoystick.setObjectName(_fromUtf8("actionJoystick"))
        
        self.actionHW = QtGui.QAction(self)
        self.actionHW.setCheckable(True)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/keyser-tux-wifi-logo-2300.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHW.setIcon(icon33)
        self.actionHW.setObjectName(_fromUtf8("actionHW"))
        self.actionBroadcast = QtGui.QAction(self)
        self.actionBroadcast.setCheckable(True)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Ubuntu_connessione_Internet_.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBroadcast.setIcon(icon34)
        self.actionBroadcast.setObjectName(_fromUtf8("actionBroadcast"))
                

        self.refreshsqlite = QtGui.QToolButton(self.navScrollArea)
        self.refreshsqlite.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.refreshsqlite.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/mActionDraw.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshsqlite.setIcon(icon1)
        self.refreshsqlite.setObjectName(_fromUtf8("refreshsqlite"))
        self.horizontalLayout_3.addWidget(self.refreshsqlite)
        self.line_18 = QtGui.QFrame(self.navScrollArea)
        self.line_18.setFrameShape(QtGui.QFrame.VLine)
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_18.setObjectName(_fromUtf8("line_18"))
        self.horizontalLayout_3.addWidget(self.line_18)
        self.placezone = QtGui.QComboBox(self.navScrollArea)
        self.placezone.setStyleSheet(_fromUtf8(""))
        self.placezone.setObjectName(_fromUtf8("placezone"))
        self.horizontalLayout_3.addWidget(self.placezone)
        self.SendPosition = QtGui.QPushButton(self.navScrollArea)
        self.SendPosition.setMaximumSize(QtCore.QSize(30, 16777215))
        self.SendPosition.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 44px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }"))
        self.SendPosition.setObjectName(_fromUtf8("SendPosition"))
        self.horizontalLayout_3.addWidget(self.SendPosition)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.line_19 = QtGui.QFrame(self.navScrollArea)
        self.line_19.setFrameShape(QtGui.QFrame.HLine)
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_19.setObjectName(_fromUtf8("line_19"))
        self.verticalLayout_5.addWidget(self.line_19)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(self.navScrollArea)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.SpeedSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpeedSpinBox.sizePolicy().hasHeightForWidth())
        self.SpeedSpinBox.setSizePolicy(sizePolicy)
        self.SpeedSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.SpeedSpinBox.setProperty(_fromUtf8("value"), 1.0)
        self.SpeedSpinBox.setObjectName(_fromUtf8("SpeedSpinBox"))
        self.horizontalLayout_7.addWidget(self.SpeedSpinBox)
        self.label_5 = QtGui.QLabel(self.navScrollArea)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.SpeedMultipler = QtGui.QSpinBox(self.navScrollArea)
        self.SpeedMultipler.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.SpeedMultipler.setObjectName(_fromUtf8("SpeedMultipler"))
        self.horizontalLayout_7.addWidget(self.SpeedMultipler)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.View = QtGui.QComboBox(self.navScrollArea)
        self.View.setStyleSheet(_fromUtf8(""))
        self.View.setObjectName(_fromUtf8("View"))
        self.View.addItem(_fromUtf8(""))
        self.View.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.View)
        self.Head = QtGui.QComboBox(self.navScrollArea)
        self.Head.setStyleSheet(_fromUtf8(""))
        self.Head.setModelColumn(0)
        self.Head.setObjectName(_fromUtf8("Head"))
        self.Head.addItem(_fromUtf8(""))
        self.Head.setItemText(0, _fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.Head.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.Head)
        self.line = QtGui.QFrame(self.navScrollArea)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_7.addWidget(self.line)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.line_20 = QtGui.QFrame(self.navScrollArea)
        self.line_20.setFrameShape(QtGui.QFrame.HLine)
        self.line_20.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_20.setObjectName(_fromUtf8("line_20"))
        self.verticalLayout_5.addWidget(self.line_20)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.hsHeading = QtGui.QToolButton(self.navScrollArea)
        self.hsHeading.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.hsHeading.setCheckable(True)
        self.hsHeading.setObjectName(_fromUtf8("hsHeading"))
        self.horizontalLayout_12.addWidget(self.hsHeading)
        self.HandlingSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea)
        self.HandlingSpinBox.setStyleSheet(_fromUtf8("border: 1px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background: rgb(231, 231, 231);"))
        self.HandlingSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HandlingSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.HandlingSpinBox.setMinimum(-360.0)
        self.HandlingSpinBox.setMaximum(360.0)
        self.HandlingSpinBox.setObjectName(_fromUtf8("HandlingSpinBox"))
        self.horizontalLayout_12.addWidget(self.HandlingSpinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.hsPitch = QtGui.QToolButton(self.navScrollArea)
        self.hsPitch.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.hsPitch.setCheckable(True)
        self.hsPitch.setObjectName(_fromUtf8("hsPitch"))
        self.horizontalLayout_12.addWidget(self.hsPitch)
        self.PitchSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea)
        self.PitchSpinBox.setStyleSheet(_fromUtf8("border: 1px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background: rgb(231, 231, 231);"))
        self.PitchSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PitchSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.PitchSpinBox.setMinimum(-90.0)
        self.PitchSpinBox.setMaximum(90.0)
        self.PitchSpinBox.setObjectName(_fromUtf8("PitchSpinBox"))
        self.horizontalLayout_12.addWidget(self.PitchSpinBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.hsRoll = QtGui.QToolButton(self.navScrollArea)
        self.hsRoll.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.hsRoll.setCheckable(True)
        self.hsRoll.setObjectName(_fromUtf8("hsRoll"))
        self.horizontalLayout_12.addWidget(self.hsRoll)
        self.RollSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea)
        self.RollSpinBox.setStyleSheet(_fromUtf8("border: 1px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background: rgb(231, 231, 231);"))
        self.RollSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RollSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.RollSpinBox.setAccelerated(False)
        self.RollSpinBox.setMinimum(-90.0)
        self.RollSpinBox.setMaximum(90.0)
        self.RollSpinBox.setObjectName(_fromUtf8("RollSpinBox"))
        self.horizontalLayout_12.addWidget(self.RollSpinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.HandlingSlider = QtGui.QSlider(self.navScrollArea)
        self.HandlingSlider.setMinimum(-360)
        self.HandlingSlider.setMaximum(360)
        self.HandlingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HandlingSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.HandlingSlider.setTickInterval(10)
        self.HandlingSlider.setObjectName(_fromUtf8("HandlingSlider"))
        self.horizontalLayout_4.addWidget(self.HandlingSlider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.PitchSlider = QtGui.QSlider(self.navScrollArea)
        self.PitchSlider.setMinimum(-90)
        self.PitchSlider.setMaximum(90)
        self.PitchSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PitchSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.PitchSlider.setObjectName(_fromUtf8("PitchSlider"))
        self.verticalLayout_5.addWidget(self.PitchSlider)
        self.RollSlider = QtGui.QSlider(self.navScrollArea)
        self.RollSlider.setMinimum(-90)
        self.RollSlider.setMaximum(90)
        self.RollSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RollSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.RollSlider.setTickInterval(10)
        self.RollSlider.setObjectName(_fromUtf8("RollSlider"))
        self.verticalLayout_5.addWidget(self.RollSlider)
        self.line_2 = QtGui.QFrame(self.navScrollArea)
        self.line_2.setStyleSheet(_fromUtf8(""))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.hsZoom = QtGui.QToolButton(self.navScrollArea)
        self.hsZoom.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.hsZoom.setCheckable(True)
        self.hsZoom.setObjectName(_fromUtf8("hsZoom"))
        self.horizontalLayout_8.addWidget(self.hsZoom)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        
        self.ZoomSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZoomSpinBox.sizePolicy().hasHeightForWidth())
        self.ZoomSpinBox.setSizePolicy(sizePolicy)
        self.ZoomSpinBox.setAutoFillBackground(True)
        self.ZoomSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.ZoomSpinBox.setWrapping(False)
        self.ZoomSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ZoomSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.ZoomSpinBox.setAccelerated(True)
        self.ZoomSpinBox.setMinimum(-10000.0)
        self.ZoomSpinBox.setMaximum(27536977.99)
        self.ZoomSpinBox.setObjectName(_fromUtf8("ZoomSpinBox"))
        self.horizontalLayout_8.addWidget(self.ZoomSpinBox)
        
        self.label_6 = QtGui.QLabel(self.navScrollArea)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        
        self.ZoomStepSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea)
        self.ZoomStepSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.ZoomStepSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.ZoomStepSpinBox.setMinimum(0.0)
        self.ZoomStepSpinBox.setMaximum(100000.0)
        self.ZoomStepSpinBox.setSingleStep(1.0)
        self.ZoomStepSpinBox.setProperty(_fromUtf8("value"), 100.0)
        self.ZoomStepSpinBox.setObjectName(_fromUtf8("ZoomStepSpinBox"))
        self.horizontalLayout_8.addWidget(self.ZoomStepSpinBox)
        
        self.label_7 = QtGui.QLabel(self.navScrollArea)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        
        self.ZoomMultipler = QtGui.QSpinBox(self.navScrollArea)
        self.ZoomMultipler.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.ZoomMultipler.setMinimum(0)
        self.ZoomMultipler.setObjectName(_fromUtf8("ZoomMultipler"))
        self.horizontalLayout_8.addWidget(self.ZoomMultipler)
        
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        
        self.ZoomSlider = QtGui.QSlider(self.navScrollArea)
        self.ZoomSlider.setMinimum(-10000)
        self.ZoomSlider.setMaximum(27536977)
        self.ZoomSlider.setProperty(_fromUtf8("value"), 5000)
        self.ZoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ZoomSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.ZoomSlider.setTickInterval(1000000)
        self.ZoomSlider.setObjectName(_fromUtf8("ZoomSlider"))
        self.verticalLayout_5.addWidget(self.ZoomSlider)
        
        self.line_3 = QtGui.QFrame(self.navScrollArea)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_5.addWidget(self.line_3)
        
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        
        self.hsRange = QtGui.QToolButton(self.navScrollArea)
        self.hsRange.setStyleSheet(_fromUtf8("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     font: bold; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 rgb(108, 183, 255) );\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.hsRange.setCheckable(True)
        self.hsRange.setObjectName(_fromUtf8("hsRange"))
        self.horizontalLayout_13.addWidget(self.hsRange)
        
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        
        self.RangeSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea) 
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RangeSpinBox.sizePolicy().hasHeightForWidth())
        self.RangeSpinBox.setSizePolicy(sizePolicy)
        self.RangeSpinBox.setAutoFillBackground(True)
        self.RangeSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.RangeSpinBox.setWrapping(True)
        self.RangeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.RangeSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.RangeSpinBox.setAccelerated(True)
        self.RangeSpinBox.setMinimum(-10000.0)
        self.RangeSpinBox.setMaximum(27536977.99)
        self.RangeSpinBox.setProperty(_fromUtf8("value"), 10000.0)
        self.RangeSpinBox.setObjectName(_fromUtf8("RangeSpinBox"))
        self.horizontalLayout_13.addWidget(self.RangeSpinBox)
        
        self.label = QtGui.QLabel(self.navScrollArea)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_13.addWidget(self.label)
        
        self.RangeStepSpinBox = QtGui.QDoubleSpinBox(self.navScrollArea)
        self.RangeStepSpinBox.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.RangeStepSpinBox.setMinimum(0.0)
        self.RangeStepSpinBox.setMaximum(100000.0)
        self.RangeStepSpinBox.setSingleStep(1.0)
        self.RangeStepSpinBox.setProperty(_fromUtf8("value"), 100.0)
        self.RangeStepSpinBox.setObjectName(_fromUtf8("RangeStepSpinBox"))
        self.horizontalLayout_13.addWidget(self.RangeStepSpinBox)
        
        self.label_8 = QtGui.QLabel(self.navScrollArea)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_13.addWidget(self.label_8)
        
        self.RangeMultipler = QtGui.QSpinBox(self.navScrollArea)
        self.RangeMultipler.setStyleSheet(_fromUtf8("background: rgb(231, 231, 231);"))
        self.RangeMultipler.setObjectName(_fromUtf8("RangeMultipler"))
        self.horizontalLayout_13.addWidget(self.RangeMultipler)
        
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        
        self.RangeSlider = QtGui.QSlider(self.navScrollArea)
        self.RangeSlider.setMinimum(-10000)
        self.RangeSlider.setMaximum(27536977)
        self.RangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RangeSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.RangeSlider.setTickInterval(1000000)
        self.RangeSlider.setObjectName(_fromUtf8("RangeSlider"))
        self.verticalLayout_5.addWidget(self.RangeSlider)
        
        self.line_4 = QtGui.QFrame(self.navScrollArea)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_5.addWidget(self.line_4)
        
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.scrollArea_4.setWidget(self.navScrollArea)
        self.verticalLayout.addWidget(self.scrollArea_4)
        
        
        self.actionLonLat = QtGui.QAction(self)
        self.actionLonLat.setCheckable(True)
        self.actionLonLat.setChecked(False)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/600px-Brosen_windrose.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)     
        self.actionLonLat.setIcon(icon19)
        self.actionLonLat.setObjectName(_fromUtf8("actionLonLat"))

        self.actionGPS = QtGui.QAction(self)
        self.actionGPS.setCheckable(True)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/satellite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGPS.setIcon(icon21)
        self.actionGPS.setObjectName(_fromUtf8("actionGPS"))
        self.actionGrass = QtGui.QAction(self)
        self.actionGrass.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/grass_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGrass.setIcon(icon7)
        self.actionGrass.setObjectName(_fromUtf8("actionGrass"))              

    def createPanToolBox(self):
        self.dockWidget = QtGui.QDockWidget(self)    
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem6)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.west = QtGui.QToolButton(self.dockWidgetContents_2)
        self.west.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_5.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.west.setIcon(icon9)
        self.west.setObjectName(_fromUtf8("west"))
        self.gridLayout.addWidget(self.west, 7, 1, 1, 1)
        self.east = QtGui.QToolButton(self.dockWidgetContents_2)
        self.east.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.east.setIcon(icon10)
        self.east.setObjectName(_fromUtf8("east"))
        self.gridLayout.addWidget(self.east, 7, 4, 1, 1)
        self.center = QtGui.QToolButton(self.dockWidgetContents_2)
        self.center.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.center.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.center.setIcon(icon11)
        self.center.setObjectName(_fromUtf8("center"))
        self.gridLayout.addWidget(self.center, 7, 3, 1, 1)
        self.southwest = QtGui.QToolButton(self.dockWidgetContents_2)
        self.southwest.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.southwest.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_8.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.southwest.setIcon(icon12)
        self.southwest.setObjectName(_fromUtf8("southwest"))
        self.gridLayout.addWidget(self.southwest, 9, 1, 1, 1)
        self.south = QtGui.QToolButton(self.dockWidgetContents_2)
        self.south.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_6.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.south.setIcon(icon13)
        self.south.setObjectName(_fromUtf8("south"))
        self.gridLayout.addWidget(self.south, 9, 3, 1, 1)
        self.southeast = QtGui.QToolButton(self.dockWidgetContents_2)
        self.southeast.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.southeast.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_10.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.southeast.setIcon(icon14)
        self.southeast.setObjectName(_fromUtf8("southeast"))
        self.gridLayout.addWidget(self.southeast, 9, 4, 1, 1)
        self.north = QtGui.QToolButton(self.dockWidgetContents_2)
        self.north.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.north.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.north.setIcon(icon15)
        self.north.setObjectName(_fromUtf8("north"))
        self.gridLayout.addWidget(self.north, 4, 3, 1, 1)
        self.northwest = QtGui.QToolButton(self.dockWidgetContents_2)
        self.northwest.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.northwest.setText(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_9.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.northwest.setIcon(icon16)
        self.northwest.setObjectName(_fromUtf8("northwest"))
        self.gridLayout.addWidget(self.northwest, 4, 1, 1, 1)
        self.northeast = QtGui.QToolButton(self.dockWidgetContents_2)
        self.northeast.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.northeast.setText(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/shapeimage_7.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.northeast.setIcon(icon17)
        self.northeast.setObjectName(_fromUtf8("northeast"))
        self.gridLayout.addWidget(self.northeast, 4, 4, 1, 1)
        self.zoomDell = QtGui.QToolButton(self.dockWidgetContents_2)
        self.zoomDell.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.zoomDell.setText(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomDell.setIcon(icon18)
        self.zoomDell.setObjectName(_fromUtf8("zoomDell"))
        self.gridLayout.addWidget(self.zoomDell, 10, 1, 1, 1)
        self.clview = QtGui.QToolButton(self.dockWidgetContents_2)
        self.clview.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.clview.setText(_fromUtf8(""))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/600px-Brosen_windrose.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clview.setIcon(icon19)
        self.clview.setObjectName(_fromUtf8("clview"))
        self.gridLayout.addWidget(self.clview, 10, 3, 1, 1)
        self.zoomAdd = QtGui.QToolButton(self.dockWidgetContents_2)
        self.zoomAdd.setStyleSheet(_fromUtf8(" QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }"))
        self.zoomAdd.setText(_fromUtf8(""))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomAdd.setIcon(icon20)
        self.zoomAdd.setObjectName(_fromUtf8("zoomAdd"))
        self.gridLayout.addWidget(self.zoomAdd, 10, 4, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem7)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        return self.dockWidget




    def retranslateUi(self):
        self.actionHW.setText(QtGui.QApplication.translate("OssimPlanetSasha", "HW", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHW.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Serial", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBroadcast.setText(QtGui.QApplication.translate("OssimPlanetSasha", "actionBroadcast", None, QtGui.QApplication.UnicodeUTF8))

        self.actionJoystick.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Joystick", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJoystick.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Joystick", None, QtGui.QApplication.UnicodeUTF8))    
        self.dockWidget_3.setWindowTitle(QtGui.QApplication.translate("OssimPlanetSasha", "Roll°", None, QtGui.QApplication.UnicodeUTF8))    
        self.dockWidget_2.setWindowTitle(QtGui.QApplication.translate("OssimPlanetSasha", "Heading°", None, QtGui.QApplication.UnicodeUTF8)) 
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("OssimPlanetSasha", "PanTool", None, QtGui.QApplication.UnicodeUTF8))
        self.west.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "West", None, QtGui.QApplication.UnicodeUTF8))
        self.west.setText(QtGui.QApplication.translate("OssimPlanetSasha", " W", None, QtGui.QApplication.UnicodeUTF8))
        self.east.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "East", None, QtGui.QApplication.UnicodeUTF8))
        self.east.setText(QtGui.QApplication.translate("OssimPlanetSasha", " E ", None, QtGui.QApplication.UnicodeUTF8))
        self.southwest.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "SouthWest", None, QtGui.QApplication.UnicodeUTF8))
        self.south.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "South", None, QtGui.QApplication.UnicodeUTF8))
        self.south.setText(QtGui.QApplication.translate("OssimPlanetSasha", " S ", None, QtGui.QApplication.UnicodeUTF8))
        self.southeast.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "SouthEast", None, QtGui.QApplication.UnicodeUTF8))
        self.north.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "North", None, QtGui.QApplication.UnicodeUTF8))
        self.northwest.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "NordWest", None, QtGui.QApplication.UnicodeUTF8)) 
        self.northeast.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "NordEast", None, QtGui.QApplication.UnicodeUTF8))                   
        self.label_3.setText(QtGui.QApplication.translate("NavigationWindow", "Eye", None, QtGui.QApplication.UnicodeUTF8))
        self.Lat.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Display Longitude value in decimal degrees", None, QtGui.QApplication.UnicodeUTF8))
        self.Lon.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Display Latitude value in decimal degrees", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("OssimPlanetSasha", "LookAt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("OssimPlanetSasha", "N/E", None, QtGui.QApplication.UnicodeUTF8))
        self.Nord.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "North - UTM coordinates - meters", None, QtGui.QApplication.UnicodeUTF8))
        self.East.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "East - UTM coordinates - meters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("OssimPlanetSasha", "UTM", None, QtGui.QApplication.UnicodeUTF8))
        self.utmcode.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "UTM zone", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Ellipsoid", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(0, QtGui.QApplication.translate("OssimPlanetSasha", "WGS-84", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(1, QtGui.QApplication.translate("OssimPlanetSasha", "Airy", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(2, QtGui.QApplication.translate("OssimPlanetSasha", "Australian National", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(3, QtGui.QApplication.translate("OssimPlanetSasha", "Bessel 1841", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(4, QtGui.QApplication.translate("OssimPlanetSasha", "Bessel 1841 (Nambia)", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(5, QtGui.QApplication.translate("OssimPlanetSasha", "Clarke 1866", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(6, QtGui.QApplication.translate("OssimPlanetSasha", "Clarke 1880", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(7, QtGui.QApplication.translate("OssimPlanetSasha", "Everest", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(8, QtGui.QApplication.translate("OssimPlanetSasha", "Fischer 1960 (Mercury)", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(9, QtGui.QApplication.translate("OssimPlanetSasha", "Fischer 1968", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(10, QtGui.QApplication.translate("OssimPlanetSasha", "GRS 1967", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(11, QtGui.QApplication.translate("OssimPlanetSasha", "GRS 1980", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(12, QtGui.QApplication.translate("OssimPlanetSasha", "Helmert 1906", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(13, QtGui.QApplication.translate("OssimPlanetSasha", "Hough", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(14, QtGui.QApplication.translate("OssimPlanetSasha", "International", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(15, QtGui.QApplication.translate("OssimPlanetSasha", "Krassovsky", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(16, QtGui.QApplication.translate("OssimPlanetSasha", "Modified Airy", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(17, QtGui.QApplication.translate("OssimPlanetSasha", "Modified Everest", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(18, QtGui.QApplication.translate("OssimPlanetSasha", "Modified Fischer 1960", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(19, QtGui.QApplication.translate("OssimPlanetSasha", "South American 1969", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(20, QtGui.QApplication.translate("OssimPlanetSasha", "WGS 60", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(21, QtGui.QApplication.translate("OssimPlanetSasha", "WGS 66", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(22, QtGui.QApplication.translate("OssimPlanetSasha", "WGS-72", None, QtGui.QApplication.UnicodeUTF8))
        self.ellipse.setItemText(23, QtGui.QApplication.translate("OssimPlanetSasha", "WGS-84", None, QtGui.QApplication.UnicodeUTF8))

        #actions from SashaMainWindow
        self.actionLonLat.setText(QtGui.QApplication.translate("OssimPlanetSasha", "LonLat", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLonLat.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "LonLat", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionGPS.setText(QtGui.QApplication.translate("OssimPlanetSasha", "GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGrass.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Grass", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGrass.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Grass", None, QtGui.QApplication.UnicodeUTF8))
                
        self.Place.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Geonames Zone", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshsqlite.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reload sqlite db</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.placezone.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Geonames Place", None, QtGui.QApplication.UnicodeUTF8))
        self.SendPosition.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Pan-Step : Deg", None, QtGui.QApplication.UnicodeUTF8))
        self.SpeedSpinBox.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Pan Step in decimal degrees", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("OssimPlanetSasha", "* 10^-", None, QtGui.QApplication.UnicodeUTF8))
        self.SpeedMultipler.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "PStep - 10^-x  multipler", None, QtGui.QApplication.UnicodeUTF8))
        self.View.setItemText(0, QtGui.QApplication.translate("OssimPlanetSasha", "LookAt", None, QtGui.QApplication.UnicodeUTF8))
        self.View.setItemText(1, QtGui.QApplication.translate("OssimPlanetSasha", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Heading mode", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(1, QtGui.QApplication.translate("OssimPlanetSasha", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(2, QtGui.QApplication.translate("OssimPlanetSasha", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(3, QtGui.QApplication.translate("OssimPlanetSasha", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(4, QtGui.QApplication.translate("OssimPlanetSasha", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(5, QtGui.QApplication.translate("OssimPlanetSasha", "SE", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(6, QtGui.QApplication.translate("OssimPlanetSasha", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(7, QtGui.QApplication.translate("OssimPlanetSasha", "SW", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(8, QtGui.QApplication.translate("OssimPlanetSasha", "W", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(9, QtGui.QApplication.translate("OssimPlanetSasha", "NW", None, QtGui.QApplication.UnicodeUTF8))
        self.Head.setItemText(10, QtGui.QApplication.translate("OssimPlanetSasha", "NE", None, QtGui.QApplication.UnicodeUTF8))
        self.hsHeading.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Heading ", None, QtGui.QApplication.UnicodeUTF8))
        self.hsPitch.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Pitch", None, QtGui.QApplication.UnicodeUTF8))
        self.hsRoll.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Roll ", None, QtGui.QApplication.UnicodeUTF8))
        self.hsZoom.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Zoom ", None, QtGui.QApplication.UnicodeUTF8))
        self.ZoomSpinBox.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Zoom (altitude) value in meters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Step : m", None, QtGui.QApplication.UnicodeUTF8))
        self.ZoomStepSpinBox.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Zoom Step in meters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("OssimPlanetSasha", "*10^", None, QtGui.QApplication.UnicodeUTF8))
        self.ZoomMultipler.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "ZStep - 10^x  multipler", None, QtGui.QApplication.UnicodeUTF8))
        self.hsRange.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Range ", None, QtGui.QApplication.UnicodeUTF8))
        self.RangeSpinBox.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Range (distance) in meters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Step : m", None, QtGui.QApplication.UnicodeUTF8))
        self.RangeStepSpinBox.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Zoom Step in meters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("OssimPlanetSasha", "*10^", None, QtGui.QApplication.UnicodeUTF8))
        

