#!/usr/bin/env python
import sys

#Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from utils import Utils



from wifi_joy import startj
from drawer import *
from log import *
if Utils.haveGRASS_:
    from Gdata import Data
    from GrassShell import GrShell

#ui
from gen.ui_sashamainwindow import Ui_SashaMainWindow

#gui
from gui.preferenceswindow import PreferencesWindow


class SashaMainWindow(QMainWindow, Ui_SashaMainWindow):
    def __init__(self, arg):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.item = self.GetViewType(0)
        self.arg_ = arg
                
        self.Place.setEditable(1)
        self.Place.setAutoCompletion(1)
        self.placezone.setEditable(1)
        self.placezone.setAutoCompletion(1)   

        self.joy = logJ()
        self.log = logS()
        #self.hw = HWS()
        self.gpsx = GpsT()
        #self.gt = gt(self.setcmd)
        #
        #self.lineEdit2 = QLineEdit(self.tab_6)
        #self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        #self.compassLayout.addWidget(self.lineEdit2)
        compass_widget = DrawCompass(self)
        roll_widget = DrawRoll(self)
        self.rotationAngleSpinBox = QSpinBox()
        self.rotationAngleSpinBox.setRange(0, 359)
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix('\xB0')
        self.rotationAngleLabel = QLabel("&Heading:")
        self.rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)
        self.compassLayout.addWidget(compass_widget)
        self.HLayout = QHBoxLayout()
        self.HLayout.addWidget(self.rotationAngleLabel)
        self.HLayout.addWidget(self.rotationAngleSpinBox)
        self.compassLayout.addLayout(self.HLayout)
        self.rotationAngleSpinBox.valueChanged.connect(compass_widget.setRotationAngle)
        self.rotationAngleSpinBox.hide()
        self.rotationAngleLabel.hide()
        #
        self.rotationRollSpinBox = QSpinBox()
        self.rotationRollSpinBox.setRange(0, 359)
        self.rotationRollSpinBox.setWrapping(True)
        self.rotationRollSpinBox.setSuffix('\xB0')
        self.rotationRollLabel = QLabel("&Roll:")
        self.rotationRollLabel.setBuddy(self.rotationRollLabel)
        self.rollLayout.addWidget(roll_widget)
        self.HLayoutRoll = QHBoxLayout()
        self.HLayoutRoll.addWidget(self.rotationRollLabel)
        self.HLayoutRoll.addWidget(self.rotationRollSpinBox)
        self.rollLayout.addLayout(self.HLayoutRoll)
        self.rotationRollSpinBox.valueChanged.connect(roll_widget.setRotationAngle)
        self.rotationRollSpinBox.hide()
        self.rotationRollLabel.hide()
        self.mainTabWidget.setCurrentIndex(0)    


    def initWidgets(self):
        self.ZoomSpinBox.setValue(0)
        self.RangeSpinBox.setValue(100000)
        self.ZoomSlider.setValue(0)
        self.RangeSlider.setValue(100000)
        self.mainTabWidget.removeTab(3)
        self.prefsWindow_ = PreferencesWindow()
        
        if Utils.haveGRASS_ == 0:
            self.mainTabWidget.removeTab(1)
            self.actionGrass.setEnabled(False)
            self.actionData.setEnabled(False)
            self.actionGrass.setVisible(False)
            self.actionData.setVisible(False)
            self.actionGrassshell.setEnabled(False)
            self.actionGrassshell.setVisible(False)
        else:
            self.Gshell = GrShell()
            self.Data = Data() 
            self.slvallon = self.getCenter()[0]
            self.slvallat = self.getCenter()[1]
            self.connect(self.Lon, SIGNAL("textChanged(QString)"), 
                         self.Data.setLonValue)
            self.connect(self.Lat, SIGNAL("textChanged(QString)"), 
                         self.Data.setLatValue)
            self.connect(self.GrassRLayer, SIGNAL("currentIndexChanged(int)"), self.selectraster)
            self.connect(self.GrassVLayer, SIGNAL("currentIndexChanged(int)"), self.selectvector)
            self.connect(self.refreshlayerlist, SIGNAL("clicked()"), self.refreshlayer)
            self.connect(self.refreshlayerlist, SIGNAL("clicked()"), self.showrenderoptions)
            self.connect(self.addRlayer, SIGNAL("clicked()"), self.addraster)
            self.connect(self.removeRlayer, SIGNAL("clicked()"), self.removeraster)
            self.connect(self.addVlayer, SIGNAL("clicked()"), self.addvector)
            self.connect(self.removeVlayer, SIGNAL("clicked()"), self.removevector)
            self.connect(self.actionGrass, SIGNAL("triggered()"),
                         self.Grassunceckbuttons)
            # Grass Shell
            self.connect(self.actionGrassshell, SIGNAL("triggered()"), 
                         self.GrassShell)
            self.vectors = VectorList()
            self.rasters = RasterList()
            vect = len(self.vectors)
            rast = len(self.rasters)
            numrow = max(vect,rast)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setRowCount(numrow)
            self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
            for i in range(rast):
                item = QTableWidgetItem(self.rasters[i])
                item.setTextAlignment(Qt.AlignCenter)
                item.setCheckState(Qt.Unchecked)
                self.tableWidget.setItem(i, 0, item)
            for i in range(vect):
                item = QTableWidgetItem(self.vectors[i])
                item.setTextAlignment(Qt.AlignCenter)
                item.setCheckState(Qt.Unchecked)
                self.tableWidget.setItem(i, 1, item)
            self.gcmd.setEditable(1)
            self.gcmd.setAutoCompletion(1)
            commandlist = self.commandlist()
            self.gcmd.addItems(commandlist)
            self.gcmd.setEditable(1)
            self.gcmd.setAutoCompletion(1)
            self.gt = gt(self.setcmd)
           
                        

        
        self.Lon.setText("0")
        self.Lat.setText("0")
        
        #
        self.grassvectoroption.hide()
        # Hide/Show Slider
        self.actionHideSlider.setChecked(True)
        self.actionHideSpinbox.setChecked(True)
        self.actionHideStepTool.setChecked(True)
        self.actionHide_place_position.setChecked(True)
        self.RollSlider.hide()
        self.PitchSlider.hide()
        self.HandlingSlider.hide()
        self.ZoomSlider.hide()
        self.RangeSlider.hide()

        # Pan Toolbox
        self.north.setAutoRepeat(True)
        self.northeast.setAutoRepeat(True)
        self.south.setAutoRepeat(True)
        self.east.setAutoRepeat(True)
        self.west.setAutoRepeat(True)
        self.southwest.setAutoRepeat(True)
        self.northwest.setAutoRepeat(True)
        self.southeast.setAutoRepeat(True)
        


        # spyderlib
        if self.arg_ == '-d':
            from spyderlib.widgets import internalshell
            dock = QDockWidget("Python Shell")
            self.pythonshell = internalshell.InternalShell(dock, namespace=globals(),commands=[], multithreaded=False)
            dock.setWidget(self.pythonshell)
            self.addDockWidget(Qt.BottomDockWidgetArea, dock)

        #self.show()        
        
        
        

    def connectSignals(self):
        # Hide Panel
        self.connect(self.actionHideSlider, SIGNAL("triggered()"), self.hidetool)
        self.connectPanSignals()
        self.connectZoomRangeSignals()
        self.connectSpeedSignals()
        self.connectHeadSignals()
        self.connectRollSignals()
        self.connectPitchSignals()
        self.connectRangeSignals()
        self.connectZoomSignals()
        self.connectPlaceSignals()
        self.connectActionSignals()


        # Epsg search-tool
        #self.connect(self.actionEpsg, SIGNAL("triggered()"), self.SEpsg)
        
        # Geonames sqlite DB

        self.connect(self.Place, SIGNAL("currentIndexChanged(int)"),
                     self.itemlist)
        self.connect(self.placezone, SIGNAL("currentIndexChanged(int)"), 
                     self.setplacezonecoords)
        self.connect(self.refreshsqlite, SIGNAL("clicked()"), self.refreshsqlitedb)
        # Vector GeoTransform
        self.connect(self.actionVectorOp, SIGNAL("triggered()"), self.Geom) 
        # Exit QApp
        #self.connect(self.actionExit, SIGNAL("triggered()"), qApp, SLOT("quit()"))
        self.connect(self.actionExit, SIGNAL("triggered()"), self.quitAll)
        
        
        
        
        self.connect(self.update, SIGNAL("clicked()"),self.aggiorna)
        self.connect(self.getlisttoquery, SIGNAL("clicked()"),self.getrasterstate)
        self.connect(self.getlisttoquery, SIGNAL("clicked()"),self.getvectorstate)
        self.connect(self.gcmdexec, SIGNAL("clicked()"),self.commandlist)

        self.connect(self.gcmd, SIGNAL("currentIndexChanged(int)"), self.selectcmd)
        self.connect(self.gcmdexec, SIGNAL("clicked()"), self.startstopGt)
        self.connect(self.gcmdexec, SIGNAL("clicked()"), self.stopstartGt)

#        self.connect(self.update, SIGNAL("clicked()"),self.aggiorna)
#        self.connect(self.getlisttoquery, SIGNAL("clicked()"),self.getrasterstate)
#        self.connect(self.getlisttoquery, SIGNAL("clicked()"),self.getvectorstate)
#        self.connect(self.gcmdexec, SIGNAL("clicked()"),self.commandlist)   

    def connectPlaceSignals(self):
        # Place Model (send position to save kml model)
        #xprint "here"
        self.connect(self.Lon, SIGNAL("textChanged(QString)"), 
                     self.placemodel.setLonValue)
        self.connect(self.Lat, SIGNAL("textChanged(QString)"), 
                     self.placemodel.setLatValue)
        self.connect(self.RollSpinBox, SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeRoll)
        self.connect(self.PitchSpinBox, SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangePitch)
        self.connect(self.HandlingSpinBox, SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeHead)
        self.connect(self.ZoomSpinBox, SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeZoom)
        self.connect(self.RangeSpinBox, SIGNAL("valueChanged(double)"), 
                     self.placemodel.setChangeRange)
        self.connect(self.actionModel, SIGNAL("triggered()"), 
                     self.modeldialog)

#FIXME
#        # Place Model (send position to save kml model)
#        self.connect(self.w.Lon, SIGNAL("textChanged(QString)"), 
#                     self.placemodel.setLonValue)
#        self.connect(self.w.Lat, SIGNAL("textChanged(QString)"), 
#                     self.placemodel.setLatValue)
#        self.connect(self.w.RollSpinBox, SIGNAL("valueChanged(double)"), 
#                     self.placemodel.setChangeRoll)
#        self.connect(self.w.PitchSpinBox, SIGNAL("valueChanged(double)"), 
#                     self.placemodel.setChangePitch)
#        self.connect(self.w.HandlingSpinBox, SIGNAL("valueChanged(double)"), 
#                     self.placemodel.setChangeHead)
#        self.connect(self.w.ZoomSpinBox, SIGNAL("valueChanged(double)"), 
#                     self.placemodel.setChangeZoom)
#        self.connect(self.w.RangeSpinBox, SIGNAL("valueChanged(double)"), 
#                     self.placemodel.setChangeRange)
#        self.connect(self.w.actionModel, SIGNAL("triggered()"), 
#                     self.modeldialog)                     

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
        # ACTIONS
        # GPS
    def connectActionSignals(self):
        self.connectGpsActions()
        self.connectLonLatActions()
        self.connectJoystickActions()
        self.connectBroadcastActions()
        self.connectHwActions()
        self.connectPositonActions()        
        
        # Coordinate Display UTM
        self.connect(self.ellipse, SIGNAL("currentIndexChanged(int)"), self.ellipsesettings)
        # View Type
        self.connect(self.View, SIGNAL("currentIndexChanged(int)"), self.GetViewType)

                        

    def connectGpsActions(self):    
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
        
    def connectLonLatActions(self):        
        # LON LAT
        self.connect(self.actionLonLat, SIGNAL("triggered()"),
                     self.LonLatunceckbuttons)
        # GRASS
        #self.connect(self.actionGrass, SIGNAL("triggered()"),
        #             self.Grassunceckbuttons)
        
    def connectJoystickActions(self):         
        # Joistick
        self.connect(self.actionJoystick, SIGNAL("triggered()"),
                     self.Joyunceckbuttons)
        self.connect(self.actionJoystick, SIGNAL("triggered()"), 
                     self.startstopjoy)	
        self.connect(self.actionJoystick, SIGNAL("triggered()"), 
                     self.stopstartjoy)
                     
    def connectBroadcastActions(self):
        # Broadcast
        self.connect(self.actionBroadcast, SIGNAL("triggered()"), 
                     self.Serialunceckbuttons)
        #FIXME                     
#        self.connect(self.actionBroadcast, SIGNAL("triggered()"), 
#                     self.startstoplog)
#        self.connect(self.actionBroadcast, SIGNAL("triggered()"), 
#                     self.stopstartlog)

    def connectHwActions(self):        
        # HW
        self.connect(self.actionHW, SIGNAL("triggered()"),
                     self.Serialunceckbuttons2)
        self.connect(self.actionHW, SIGNAL("triggered()"), 
                     self.stopstartHW)
        self.connect(self.actionHW, SIGNAL("triggered()"),
                     self.startstopHW)
        self.connect(self.actionDB_setting, SIGNAL("triggered()"),
                     self.pgsetting)
        self.connect(self.actionPref, SIGNAL("triggered()"), self.showPreferences)

        self.connect(self.actionDataexp, SIGNAL("triggered()"),
                     self.processdata)
        self.connect(self.actionData, SIGNAL("triggered()"),
                     self.processdata)
        self.connect(self.renderoptions, SIGNAL("clicked()"), self.getRenderOptions)
        self.connect(self.renderoptions, SIGNAL("clicked()"), self.showrenderoptions)
        

    def connectPositonActions(self):
        # Send Position
        self.connect(self.SendPosition, SIGNAL("clicked()"),
                     self.SetLonLat)
        self.connect(self.SendPosition, SIGNAL("clicked()"),
                     self.SetJoyCoords)
        self.connect(self.SendPosition, SIGNAL("clicked()"),
                     self.ResetPosition)
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

    def showPreferences(self):
        self.prefsWindow_.show()
        

    def processdata(self):
        self.Data.show()
    
    
    def dataprocess(self):
        self.DataW.show()
        #self.compass.show()
    
    
    def GrassShell(self):
        if Utils.haveGRASS_ != 0:
            self.Gshell.show()
    
        
    def kmldialog(self):
        self.kmlview.show()
     
    def SEpsg(self):
        #self.searchepsg = SearchEpsg()
        self.epsgWindow.show()
    
    
    def Geom(self):
        self.vectoroperation.show()
            
    def pgsetting(self):
        self.pgconn = PgConn()
        self.pgconn.show()

    def worningmessage(self,text):
        self.worn = WarnMsgWindow()
        self.worn.label.setText(text)
        self.worn.show()
                                     
#    def showPreference(self):
#        self.preferencesetting = PreferencesWindow()
#        
        
    def selectcmd(self,index):
        #global setcmd
        self.setcmd = self.w.gcmd.itemText(index)
        return self.setcmd

    def addraster(self):
        while 1:
            try:
                #host = str(parseOutputconf()['host'])
                #dport = parseOutputconf()['dport']
                #pport = parseOutputconf()['pport']
                #print host, dport, pport
                host = str(parseOutputconf()['host']).split()
                print host
                for i in host :
                    print i
                    try:
                        run_command('r.planet.py', flags = 'a', map = inputR, host = str(i), dport = str(parseOutputconf()['dport']), pport = str(parseOutputconf()['pport']))
                    except IOError:
                        time.sleep(0.1)
                break
            except IOError:
                time.sleep(0.1)
        print 'add', inputR
    
        
    def removeraster(self):
        while 1:
            try:
                run_command('r.planet.py', flags = 'r', map = inputR, host = str(parseOutputconf()['host']), dport = parseOutputconf()['dport'], pport = parseOutputconf()['pport'])
                break
            except IOError:
                time.sleep(0.1)
        print 'removed', inputR
    
        
    def addvector(self):
        database_name = parseOutputconf()['spatialitedb']
        print database_name
        while 1:
            try:
                print inputV
                mapset = getEnv()['MAPSET']
                #instruction = "v.planet.py -a map='%s'@'%s' brush=111,111,111 pen=111,111,111 size=1,1 fill=0 "  % (inputV, mapset)
                #print instruction
                #os.system(instruction)
                #PointSize = str(parseOutputconf()['PointSize'])
                #LineWidth = str(parseOutputconf()['LineWidth'])
                #PenColor = str(parseOutputconf()['PenColor'])
                #BrushColor = str(parseOutputconf()['BrushColor'])
                Thickness = parseOutputconf()['Thickness']
                Fill = parseOutputconf()['Fill']
                PointSize = self.w.PointSize.text()
                LineWidth = self.w.LineWidth.value()
                PenColor = self.w.PenColor.text()
                BrushColor = self.w.BrushColor.text()
                
                run_command('v.planet.py', flags = 'a', map = str(inputV)+'@'+str(mapset), host = str(parseOutputconf()['host']), dport = parseOutputconf()['dport'], pport = parseOutputconf()['pport'], brush = BrushColor, pen = PenColor, size = PointSize, fill = Fill)
                break
            except IOError:
                time.sleep(0.2)
        print 'add', inputV
    
        
    def removevector(self):
        while 1:
            try:
                #mapsets = read_command('g.mapsets', flags ='l')
                #mapsets.replace('\n','').split()
                #for i in mapsets :
                #    print inputV+str(i)
                #    run_command('v.planet.py', flags = 'r', map = inputV+'@'+str(i), dport = 8000, pport = 7000)
                mapset = getEnv()['MAPSET']
                run_command('v.planet.py', flags = 'r', map = str(inputV)+'@'+str(mapset), host = str(parseOutputconf()['host']), dport = parseOutputconf()['dport'], pport = parseOutputconf()['pport'])
                time.sleep(0.1)
                break
            except IOError:
                time.sleep(0.1)
        print 'removed', inputV

    def selectraster(self,index):
        global inputR
        inputR = self.w.GrassRLayer.itemText(index)
        return inputR
        
    def selectvector(self,index):
        global inputV
        inputV = self.w.GrassVLayer.itemText(index)
        return inputV
    def refreshlayer(self):
        vector = VectorList()
        raster = RasterList()
        self.GrassRLayer.clear()
        self.GrassVLayer.clear()
        self.GrassRLayer.addItems(raster)
        self.GrassVLayer.addItems(vector)
        
    def showrenderoptions(self):
        if self.renderoptions.isChecked():
            self.grassvectoroption.show()
        else :
            self.grassvectoroption.hide()

    def getRenderOptions(self):
        PointSize = self.w.PointSize.text()
        LineWidth = self.w.LineWidth.value()
        PenColor = self.w.PenColor.text()
        BrushColor = self.w.BrushColor.text()
        #Tikchness = self.w.Tikchness.text()
        print PointSize, LineWidth, PenColor, BrushColor
       

    def commandlist(self):
        grassCmd = []
        grassCmd = GetGRASSCmds()
        #grassCmd.append(grassCmds)
        #grassCmds = self.GetGRASSCmds(bin = False)
        #grassCmd.append(grassCmds)
        return grassCmd
                
# Refresh SQLite
        
    def refreshsqlitedb(self):
        #xprint 'refresh sqlite'
        tables = self.gettablelist()
        if tables is not None :
            self.Place.clear()
            self.Place.addItems(tables)
    
    
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
    
        
    def gettablelist(self):
        #database_name = sqlitedb
        database_name = parseOutputconf()['spatialitedb']
        #xprint database_name
        db_connection = None
        try :
            db_connection = sqlite3.connect(database_name)
        except :
            self.worningmessage('spatialitedb not found')
        if db_connection is not None:
            db_cursor = db_connection.cursor()
            listatabelle = db_cursor.execute("SELECT name FROM sqlite_master where type = 'table';")
            tabelle = listatabelle.fetchall()
            tablelist = []
            for i in tabelle:
                tablelist.append(i[0])
            db_connection.commit()
            tablelist.sort()
            return tablelist
    
    def SEpsg(self):
        self.searchepsg = SearchEpsg()
        self.searchepsg.show()

# Quit Application
        
    def quitAll(self):
        print "Good Bye, PlanetSasha"
        qApp.quit()
    
    
    def Geom(self):
        self.vectoroperation.show()
    

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

    def getrasterstate(self):
        raster = RasterList()
        rast = len(raster)
        rastertoquery = []
        valori = []
        newlon = str(self.longitude.text())
        newlat = str(self.latitude.text())
        lonlat = str(newlon)+' '+str(newlat)
        f = tempfile.NamedTemporaryFile(delete=False)
        coordsfile = f.name
        f.write(lonlat)
        f.flush()
        f.close
        while 1:
            try:
                c = read_command('m.proj', input=coordsfile, flags='i')
                break
            except IOError:
                time.sleep(0.1) 
        os.unlink(f.name)
        lonlat = parse_key_val(c,'\t')
        lonlat = str(lonlat)
        lonlat = lonlat.replace('{','')
        lonlat = lonlat.replace('}','')
        lonlat = lonlat.replace("'",'')
        lonlat = lonlat.replace(':','')
        lonlat = lonlat.replace('|',' ')
        lonlat = lonlat.split(' ')
        lonlat = str(lonlat[0])+','+str(lonlat[1])
        htmlquery = []
        html = """<TABLE cellpadding="4" style="border: 1px solid \
        000000; border-collapse: collapse;" border="1"><TR><TD>Layer</TD>\
        <TD>Values</TD>"""
        htmlquery.append(html)
        for i in range(rast):
            cell = self.tableWidget.item(i, 0)
            if cell.checkState() == 2:
                while 1:
                    try:
                        s = read_command('r.what', input=cell.text(), east_north=lonlat) 
                        break
                    except IOError:
                        time.sleep(0.1)
                attr = str(s)
                attr = attr.replace("|",' ')
                attr = attr.replace('\n',' ')
                attr = attr.split(':')
                attr = str(attr)
                attr = attr.replace("'",'')
                attr = attr.replace('"','')
                attr = attr.replace('[','')
                attr = attr.replace(']','')
                results = str(cell.text())+'  : '+attr
                htmlvalue = '<TR><TD>%s</TD><TD>%s</TD>' % (cell.text() ,attr)
                htmlquery.append(htmlvalue)
                rastertoquery.append(results)
        htmlend = """</TR></TABLE>"""
        htmlquery.append(htmlend)
        rastertoquery = str(rastertoquery)
        rastertoquery = rastertoquery.replace("'",'')
        rastertoquery = rastertoquery.split(',')
        rastertoquery = str(rastertoquery)
        rastertoquery = rastertoquery.replace('[','')
        rastertoquery = rastertoquery.replace(']','')
        htmlquery = str(htmlquery)
        htmlquery = htmlquery.replace("', u'",'')
        htmlquery = htmlquery.replace("']",'')
        htmlquery = htmlquery.replace("['",'')
        htmlquery = htmlquery.replace("', '",'')
        self.QueryResultsRaster.setText(htmlquery)
        #xprint rastertoquery

    def getvectorstate(self):
        vector = VectorList()
        vect = len(vector)
        vectortoquery = []
        newlon = str(self.longitude.text())
        newlat = str(self.latitude.text())
        lonlat = str(newlon)+' '+str(newlat)
        f = tempfile.NamedTemporaryFile(delete=False)
        coordsfile = f.name
        f.write(lonlat)
        f.flush()
        f.close
        while 1:
            try:
                c = read_command('m.proj', input=coordsfile, flags='i') 
                break
            except IOError:
                time.sleep(0.1)
        os.unlink(f.name)
        lonlat = parse_key_val(c,'\t')
        lonlat = str(lonlat)
        lonlat = lonlat.replace('{','')
        lonlat = lonlat.replace('}','')
        lonlat = lonlat.replace("'",'')
        lonlat = lonlat.replace(':','')
        lonlat = lonlat.replace('|',' ')
        lonlat = lonlat.split(' ')
        lonlat = str(lonlat[0])+','+str(lonlat[1])
        htmlquery = []
        html = """<TABLE cellpadding="4" style="border: 1px solid \
        000000; border-collapse: collapse;" border="1"><TR>\
        <TD>Layer</TD><TD>Values</TD>"""
        htmlquery.append(html)
        for i in range(vect):
            cell = self.tableWidget.item(i, 1)
            if cell.checkState() == 2:
                while 1:
                    try:
                        s = read_command('v.what', map=cell.text(), east_north=lonlat)
                        break
                    except IOError:
                        time.sleep(0.1)
                attr = parse_key_val(s,':')
                attr = str(attr)
                attr = attr.replace('{','')
                attr = attr.replace('}','')
                attr = attr.replace("'",'')
                attr = attr.replace(': None','')
                htmlvalue = '<TR><TD>%s</TD><TD>%s</TD>' % (cell.text() ,attr)
                htmlquery.append(htmlvalue)
                #xprint attr
        htmlend = """</TR></TABLE>"""
        htmlquery.append(htmlend)
        htmlquery = str(htmlquery)
        htmlquery = htmlquery.replace("', u'",'')
        htmlquery = htmlquery.replace("']",'')
        htmlquery = htmlquery.replace("['",'')
        htmlquery = htmlquery.replace("', '",'')
        htmlquery = htmlquery.replace(",",'<BR>')
        self.QueryResultsVector.setText(str(htmlquery))
    
# Set Toolbar Action
    
    def GPSunceckbuttons(self):
        self.actionLonLat.setChecked(False)
        if Utils.haveGRASS_ != 0:
            self.actionGrass.setChecked(False)
        if self.actionJoystick.isChecked():
            self.joy.stop()
            self.actionJoystick.setChecked(False)
        if self.actionHW.isChecked():
            self.hw.stop()
            self.actionHW.setChecked(False)
        #if self.actionSerial.isChecked():
    
    
    def LonLatunceckbuttons(self):
        if self.actionGPS.isChecked():
            self.gpsx.stop()
            self.actionGPS.setChecked(False)
        if Utils.haveGRASS_ != 0:
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
    
    
    def Joyunceckbuttons(self):
        self.actionGPS.setChecked(False)
        self.actionLonLat.setChecked(False)
        if Utils.haveGRASS_ != 0:
            self.actionGrass.setChecked(False)
        self.actionHW.setChecked(False)
    
    
    def Serialunceckbuttons(self):
        self.actionGPS.setChecked(False)
        self.actionLonLat.setChecked(False)
        if Utils.haveGRASS_ != 0:
            self.actionGrass.setChecked(False)
        #self.actionJoystick.setChecked(False)
        self.actionHW.setChecked(False)


    def Serialunceckbuttons2(self):
        self.actionGPS.setChecked(False)
        self.actionLonLat.setChecked(False)
        if Utils.haveGRASS_ != 0:
            self.actionGrass.setChecked(False)

    def startstopjoy(self):
        if self.actionJoystick.isChecked():
            self.joy = logJ()
            self.joy.start()
            #xprint 'i am self jcords', self.Jcoords()
            self.joy.toggle(self.Jcoords()[0],self.Jcoords()[1])
            self.connect(self.Lon, SIGNAL("textChanged(QString)"), self.joy.setValueLonJ)
            self.connect(self.Lat, SIGNAL("textChanged(QString)"), self.joy.setValueLatJ)
            self.SetJoyCoords()
            self.Lon.setText(self.Lon.text())
            self.Lat.setText(self.Lat.text())
            #xprint self.Lon.text(), self.Lat.text()
        else :
            self.joy.stop()
            
    
    
    def stopstartjoy(self):
        if not self.actionJoystick.isChecked():
            self.joy = logJ()
            self.joy.stop()
            self.joy.toggle(0,0)
            
    


    def startstopHW(self):
        if self.actionHW.isChecked():
            self.hw = HWS()
            self.hw.start()
            self.hw.ValUpdated.connect(self.textHW.setText)
            self.hw.toggle()
        else :
            #self.hw = HWS()
            self.hw.stop()

    def stopstartHW(self):
        if not self.actionHW.isChecked():
            self.hw = HWS()
            self.hw.stop()
            self.hw.toggle()
    

    def startstoplog(self):
        if self.actionBroadcast.isChecked():
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
            
            self.log.toggle()
        else :
            self.log.stop()
    
    
    def stopstartlog(self):
        if not self.actionBroadcast.isChecked():
            self.log = logS()
            self.log.stop()
            self.log.toggle()
    
    
    
    def startstopGt(self):
        if self.gcmdexec.isChecked():
            self.gt = gt(self.setcmd)
            self.gt.start()
            self.gt.toggle()
        else :
            self.gt.stop()
            
    def stopstartGt(self):
        if not self.gcmdexec.isChecked():
            self.gt = gt(self.setcmd)
            self.gt.stop()
            self.gt.toggle()
    


    def startstopgpsx(self):
        if self.actionGPS.isChecked():
            #self.gpsx = GpsT()
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
            #xprint self.GPSlat.text()
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
    
    

    def modeldialog(self):
        self.placemodel.show()
    
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
    
    
    def hidetool(self):
        if self.actionHideSlider.isChecked():
            self.tabWidget.show()
        else :
            self.tabWidget.hide()    
    
            
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
        if Utils.haveGRASS_ != 0:
            if self.actionGrass.isChecked():
                lon = self.slvallon
                lat = self.slvallat
                if self.NorthEast.isChecked():
                    xy = getlonlat(lon,lat)
                    self.Nord.setText(xy[1])
                    self.East.setText(xy[0])
        if self.actionGPS.isChecked():
            lon = self.GPSlon.text()
            lat = self.GPSlat.text()
        pos = [lon,lat,zoom,heads,pitch,roll,range]
        return pos
            
    def Jcoords(self):
        newlon = str(self.Lon.text())
        newlat = str(self.Lat.text())
        return newlon, newlat

    def sendFunction(self):
        pos = self.getViewVal()
        #xprint pos
        ossimxml =  Utils.makeActionTemplate(self.item, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6])
        self.fireAction(ossimxml)
        self.Lat.setText(unicode(pos[1]))
        self.Lon.setText(unicode(pos[0]))
        #xprint 'sendFunction commented'
    

    def ResetPosition(self):
        #xprint 'reset position'
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
                if self.NorthEast.isChecked():
                    xy = getlonlat(self.slvallon,self.slvallat)
                    self.Nord.setText(xy[1])
                    self.East.setText(xy[0])
            ossimxml =  Utils.makeActionTemplate(self.item, unicode(self.slvallon), unicode(self.slvallat), 
                                             self.ZoomSlider.value(), 0, 0, 
                                             0, self.RangeSlider.value())
            self.Lat.setText(unicode(self.slvallat))
            self.Lon.setText(unicode(self.slvallon))
            self.fireAction(ossimxml)
        if self.actionGPS.isChecked():
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

    
    def fireAction(self, xml):
        result = Utils.fireAction(xml)
        if result < 0:
                if not self.actionBroadcast.isChecked():
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
        lon = float(self.Lon.text())
        lat = float(self.Lat.text())
        centro = (lon,lat)
        return centro
    
    
    def PrintPosition(self, lon, lat, zoom, roll, pitch, heading, range):
        testo = '''Longitude : %s
        Latitude : %s 
        Altitude : %s
        Heading : %s
        Roll : %s
        Pitch : %s
        Range : %s
        ''' % (lon, lat, zoom, roll, pitch, heading, range)


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
    
    
    def CeckViewTypeState(self):
        if not self.actionLonLat.isChecked():
            if Utils.haveGRASS_ !=0:
                if not self.actionGrass.isChecked():
                    self.worningmessage('check a view type')
        
                                                     
