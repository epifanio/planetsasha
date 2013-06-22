
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
#from pantoolbox import PanToolBox
#from hptoolbox import HeadingToolBox, RollToolBox
from navigationwindow import NavigationWindow
from querywindow import QueryWindow

from gpswindow import GpsWindow
import resources_rc
from Utils import Utils
from Savekml import KmlView

class SashaMainWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi()
        
#        self.pantoolbox.setNWindow(self.nWindow_)
        self.connectSignals()
        
        
    def hideTool(self):
        if self.actionHideSlider.isChecked():
            self.tabWidget.show()
        else :
            self.tabWidget.hide()  


    def updateRollSpinBox(self, value):
        self.rolltoolbox.rotationRollSpinBox.setRange(-360, 360)
        self.rolltoolbox.rotationRollSpinBox.setSingleStep(1)
        self.rolltoolbox.rotationRollSpinBox.setValue(value)

    def connectSignals(self):
        self.connect(self.actionHideSlider, QtCore.SIGNAL("triggered()"), self.hideTool)
        # Joistick
        self.connect(self.nWindow_.actionJoystick, QtCore.SIGNAL("triggered()"),
                     self.Joyunceckbuttons)
        self.connect(self.nWindow_.actionJoystick, QtCore.SIGNAL("triggered()"), 
                     self.startstopjoy)	
        self.connect(self.nWindow_.actionJoystick, QtCore.SIGNAL("triggered()"), 
                     self.stopstartjoy)
        # Broadcast
        self.connect(self.nWindow_.actionBroadcast, QtCore.SIGNAL("triggered()"), 
                     self.Serialunceckbuttons)
        self.connect(self.nWindow_.actionBroadcast, QtCore.SIGNAL("triggered()"), 
                     self.startstoplog)
        self.connect(self.nWindow_.actionBroadcast, QtCore.SIGNAL("triggered()"), 
                     self.stopstartlog)
        # HW
        self.connect(self.nWindow_.actionHW, QtCore.SIGNAL("triggered()"),
                     self.Serialunceckbuttons2)
        self.connect(self.nWindow_.actionHW, QtCore.SIGNAL("triggered()"), 
                     self.stopstartHW)
        self.connect(self.nWindow_.actionHW, QtCore.SIGNAL("triggered()"),
                     self.startstopHW)
                     
        self.connect(self.actionDB_setting, QtCore.SIGNAL("triggered()"),
                     self.pgsetting)
        self.connect(self.actionPref, QtCore.SIGNAL("triggered()"), self.preference)
        self.connect(self.actionDataexp, QtCore.SIGNAL("triggered()"),
                     self.processdata)
        self.connect(self.actionData_2, QtCore.SIGNAL("triggered()"),
                     self.processdata)


            

        
        self.connect(self.actionModel, QtCore.SIGNAL("triggered()"), 
                     self.modeldialog)
        self.connect(self.actionSavekml, QtCore.SIGNAL("triggered()"), 
                     self.kmldialog)                     


    def preference(self):
        self.preferencesetting = PreferenceSetting()
        self.preferencesetting.show()
    
    
    def worningmessage(self,text):
        self.worn = worn()
        self.worn.label.setText(text)
        self.worn.show()


    def processdata(self):
        self.Data.show()
    
    
    def dataprocess(self):
        self.DataW.show()
        #self.compass.show()
    
    
    def GrassShell(self):
        if GRASS != 0:
            self.Gshell.show()
    
        
    def kmldialog(self):
        self.nWindow_.kmlview.show()
    
    
    def modeldialog(self):
        self.placemodel.show()
    
     
    def SEpsg(self):
        self.searchepsg = SearchEpsg()
        self.searchepsg.show()
    
    
    def Geom(self):
        self.vectoroperation.show()
    
    
# code not used :
    
    def modeldialog(self):
        self.placemodel.show()
        #lite
    
    
    def setparamconnection2(self):
        try:
            TCP = open(tcpparam, "r")
            K = TCP.read()
            Y = K.rsplit(',')
            host = str(Y[0])
            nav = str(Y[1])
            data = str(Y[2])
            return host, nav, data
        except :
            print 'Use preference Panel to set preference'
            self.worningmessage('Use the preference setting to set TCP preference')
    
    def GpsHandling(self):
        #print self.item,self.ZoomSlider.value(),head,self.PitchSlider.value(),
        #self.RollSlider.value(),self.RangeSlider.value()
        #self.gps = GpsClass(self.item,self.ZoomSlider.value(),head,
        #self.PitchSlider.value(),self.RollSlider.value(),self.RangeSlider.value())
        self.gps.show()
        
    def startstopjoy(self):
        if self.actionJoystick.isChecked():
            self.joy = logJ()
            self.joy.start()
            #print 'i am self jcords', self.Jcoords()
            self.joy.toggle(self.Jcoords()[0],self.Jcoords()[1])
            self.connect(self.Lon, SIGNAL("textChanged(QString)"), self.joy.setValueLonJ)
            self.connect(self.Lat, SIGNAL("textChanged(QString)"), self.joy.setValueLatJ)
            self.SetJoyCoords()
            self.Lon.setText(self.Lon.text())
            self.Lat.setText(self.Lat.text())
            print self.Lon.text(), self.Lat.text()
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

    def Serialunceckbuttons(self):
        self.actionGPS.setChecked(False)
        self.actionLonLat.setChecked(False)
        if GRASS != 0:
            self.actionGrass.setChecked(False)
        #self.actionJoystick.setChecked(False)
        self.actionHW.setChecked(False)


    def Serialunceckbuttons2(self):
        self.actionGPS.setChecked(False)
        self.actionLonLat.setChecked(False)
        if GRASS != 0:
            self.actionGrass.setChecked(False)    

    def pgsetting(self):
        self.pgconn = PgConn()
        self.pgconn.show()
            
    def Joyunceckbuttons(self):
        self.actionGPS.setChecked(False)
        self.actionLonLat.setChecked(False)
        if GRASS != 0:
            self.actionGrass.setChecked(False)
        self.actionHW.setChecked(False)
                
    def setupUi(self):
        
        self.resize(764, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/epi.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        self.centralwidget = QtGui.QWidget(self)
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)

        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        self.nWindow_ = NavigationWindow(self)        
        self.tabWidget.addTab(self.nWindow_, _fromUtf8("Navigation")) 

        self.qWindow_ = QueryWindow()
        self.tabWidget.addTab(self.qWindow_, _fromUtf8("Query"))
        self.gWindow_ = GpsWindow()        
        self.tabWidget.addTab(self.gWindow_, _fromUtf8("GPS"))
        
        self.horizontalLayout.addWidget(self.tabWidget)
  
        self.dWindow = DataWindow(self)      
    
        self.tabWidget.addTab(self.dWindow, _fromUtf8("Data"))
        
        self.horizontalLayout.addWidget(self.tabWidget)
        
        self.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSasha = QtGui.QMenu(self.menubar)
        self.menuSasha.setObjectName(_fromUtf8("menuSasha"))
        self.menuView_2 = QtGui.QMenu(self.menuSasha)
        self.menuView_2.setObjectName(_fromUtf8("menuView_2"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuGPS = QtGui.QMenu(self.menuTools)
        self.menuGPS.setObjectName(_fromUtf8("menuGPS"))
        self.menuData = QtGui.QMenu(self.menuTools)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(self)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        #
        #self.pantoolbox = PanToolBox(self)
        #self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.pantoolbox)
#        self.headingtoolbox = HeadingToolBox(self.nWindow_)
#        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.headingtoolbox)
#        self.rolltoolbox = RollToolBox(self)
#        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.rolltoolbox)


        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/joystick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.actionExit = QtGui.QAction(self)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon23)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDB_setting = QtGui.QAction(self)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/db.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDB_setting.setIcon(icon24)
        self.actionDB_setting.setObjectName(_fromUtf8("actionDB_setting"))
        self.actionNMEA = QtGui.QAction(self)
        self.actionNMEA.setObjectName(_fromUtf8("actionNMEA"))
        self.actionData_2 = QtGui.QAction(self)
        self.actionData_2.setCheckable(False)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gui-mapzoom.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionData_2.setIcon(icon25)
        self.actionData_2.setObjectName(_fromUtf8("actionData_2"))
        self.actionSavekml = QtGui.QAction(self)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/saveinfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSavekml.setIcon(icon26)
        self.actionSavekml.setObjectName(_fromUtf8("actionSavekml"))
        self.actionEpsg = QtGui.QAction(self)
        self.actionEpsg.setObjectName(_fromUtf8("actionEpsg"))
        self.actionHidesliders = QtGui.QAction(self)
        self.actionHidesliders.setCheckable(True)
        self.actionHidesliders.setObjectName(_fromUtf8("actionHidesliders"))
        self.actionHideSpinbox = QtGui.QAction(self)
        self.actionHideSpinbox.setCheckable(True)
        self.actionHideSpinbox.setObjectName(_fromUtf8("actionHideSpinbox"))
        self.actionHide_place_position = QtGui.QAction(self)
        self.actionHide_place_position.setCheckable(True)
        self.actionHide_place_position.setObjectName(_fromUtf8("actionHide_place_position"))
        self.actionHideStepTool = QtGui.QAction(self)
        self.actionHideStepTool.setCheckable(True)
        self.actionHideStepTool.setObjectName(_fromUtf8("actionHideStepTool"))
        self.actionHideSlider = QtGui.QAction(self)
        self.actionHideSlider.setCheckable(True)
        self.actionHideSlider.setObjectName(_fromUtf8("actionHideSlider"))
        self.actionJoystick_2 = QtGui.QAction(self)
        self.actionJoystick_2.setIcon(icon22)
        self.actionJoystick_2.setObjectName(_fromUtf8("actionJoystick_2"))
        self.actionDataexp = QtGui.QAction(self)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ingranaggi.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDataexp.setIcon(icon27)
        self.actionDataexp.setObjectName(_fromUtf8("actionDataexp"))
        self.actionVrt = QtGui.QAction(self)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ingranaggio_icona.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVrt.setIcon(icon28)
        self.actionVrt.setObjectName(_fromUtf8("actionVrt"))
        self.actionGVrt = QtGui.QAction(self)
        self.actionGVrt.setIcon(icon28)
        self.actionGVrt.setObjectName(_fromUtf8("actionGVrt"))
        self.actionGrassshell = QtGui.QAction(self)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/512 Terminal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGrassshell.setIcon(icon29)
        self.actionGrassshell.setObjectName(_fromUtf8("actionGrassshell"))
        self.actionModel = QtGui.QAction(self)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cubo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionModel.setIcon(icon30)
        self.actionModel.setObjectName(_fromUtf8("actionModel"))
        self.actionPref = QtGui.QAction(self)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/tools.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPref.setIcon(icon31)
        self.actionPref.setShortcut(_fromUtf8(""))
        self.actionPref.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionPref.setObjectName(_fromUtf8("actionPref"))
        self.actionVectorOp = QtGui.QAction(self)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/SquadraCompasso.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVectorOp.setIcon(icon32)
        self.actionVectorOp.setObjectName(_fromUtf8("actionVectorOp"))

        self.actionCompass = QtGui.QAction(self)
        self.actionCompass.setObjectName(_fromUtf8("actionCompass"))
        self.actionPan_Tool = QtGui.QAction(self)
        self.actionPan_Tool.setObjectName(_fromUtf8("actionPan_Tool"))
        self.actionGt = QtGui.QAction(self)
        self.actionGt.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gui-help.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
        self.actionGt.setIcon(icon8)
        self.actionGt.setObjectName(_fromUtf8("actionGt"))
        self.menuView_2.addAction(self.actionHideSlider)
        self.menuView_2.addAction(self.actionCompass)
        self.menuView_2.addAction(self.actionPan_Tool)
        self.menuSasha.addAction(self.menuView_2.menuAction())
        self.menuSasha.addAction(self.actionPref)
        self.menuGPS.addAction(self.actionNMEA)
        self.menuData.addAction(self.actionDataexp)
        self.menuData.addAction(self.actionVrt)
        self.menuTools.addAction(self.menuData.menuAction())
        self.menuTools.addAction(self.menuGPS.menuAction())
        self.menuTools.addAction(self.actionEpsg)
        self.menubar.addAction(self.menuSasha.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        
        self.toolBar.addAction(self.nWindow_.actionLonLat) #FIXME
        self.toolBar.addAction(self.nWindow_.actionGrass)
        self.toolBar.addAction(self.nWindow_.actionGPS)
        
        self.toolBar.addAction(self.nWindow_.actionBroadcast)
        self.toolBar.addAction(self.nWindow_.actionJoystick)
        self.toolBar.addAction(self.nWindow_.actionHW)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionData_2)
        self.toolBar.addAction(self.actionGrassshell)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSavekml)
        self.toolBar.addAction(self.actionVectorOp)
        self.toolBar.addAction(self.actionModel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.tabWidget.setCurrentIndex(0)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        



    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("OssimPlanetSasha", "OssimPlanetSasha", None, QtGui.QApplication.UnicodeUTF8))
        
        self.menuSasha.setTitle(QtGui.QApplication.translate("OssimPlanetSasha", "Sasha", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView_2.setTitle(QtGui.QApplication.translate("OssimPlanetSasha", "view", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("OssimPlanetSasha", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGPS.setTitle(QtGui.QApplication.translate("OssimPlanetSasha", "GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("OssimPlanetSasha", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("OssimPlanetSasha", "toolBar", None, QtGui.QApplication.UnicodeUTF8))




        self.actionExit.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDB_setting.setText(QtGui.QApplication.translate("OssimPlanetSasha", "DB-setting", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNMEA.setText(QtGui.QApplication.translate("OssimPlanetSasha", "NMEA", None, QtGui.QApplication.UnicodeUTF8))
        self.actionData_2.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionData_2.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Data processing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavekml.setText(QtGui.QApplication.translate("OssimPlanetSasha", "savekml", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEpsg.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Epsg", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHidesliders.setText(QtGui.QApplication.translate("OssimPlanetSasha", "hideslider", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHideSpinbox.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Spinbox", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHide_place_position.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Place-Position", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHideStepTool.setText(QtGui.QApplication.translate("OssimPlanetSasha", "StepTool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHideSlider.setText(QtGui.QApplication.translate("OssimPlanetSasha", "tabPosition", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJoystick_2.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Joystick", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDataexp.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVrt.setText(QtGui.QApplication.translate("OssimPlanetSasha", "DataTools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGVrt.setText(QtGui.QApplication.translate("OssimPlanetSasha", "vrt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGrassshell.setText(QtGui.QApplication.translate("OssimPlanetSasha", "grassshell", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModel.setText(QtGui.QApplication.translate("OssimPlanetSasha", "model", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPref.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPref.setToolTip(QtGui.QApplication.translate("OssimPlanetSasha", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVectorOp.setText(QtGui.QApplication.translate("OssimPlanetSasha", "VectorOp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompass.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Compass", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPan_Tool.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Pan-Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGt.setText(QtGui.QApplication.translate("OssimPlanetSasha", "Gt", None, QtGui.QApplication.UnicodeUTF8))
       

    def initWidgets(self):
    

        
        self.queryvalue = 0     #FIXME
        

        
        self.tabWidget.removeTab(3)

        if Utils.haveGRASS == 0:
            self.tabWidget.removeTab(1)
           
            self.actionData_2.setEnabled(False)

            self.actionData_2.setVisible(False)
            self.actionGrassshell.setEnabled(False)
            self.actionGrassshell.setVisible(False)           

        # Hide/Show Slider
        self.actionHideSlider.setChecked(True)
        self.actionHideSpinbox.setChecked(True)
        self.actionHideStepTool.setChecked(True)
        self.actionHide_place_position.setChecked(True)

                
class DataWindow(QtGui.QWidget):

    def __init__(self, parent = None):
    
        QtGui.QWidget.__init__(self, parent)
        self.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.textHW = QtGui.QTextEdit(self)
        self.textHW.setObjectName(_fromUtf8("textHW"))
        self.verticalLayout_7.addWidget(self.textHW)



        
        
