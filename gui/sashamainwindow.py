#!/usr/bin/env python
import sys

#Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from utils import Utils



#from wifi_joy import startj

from log import *


#ui
from gen.ui_sashamainwindow import Ui_SashaMainWindow

#gui
from gui.navigationwindow import NavigationWindow

from gui.gpswindow import GpsWindow
from gui.mapwindow import MapWindow
from gui.preferenceswindow import PreferencesWindow

from gui.importwindow import ImportWindow
from gui.ossimwindow import OssimWindow

if Utils.haveGRASS_:
    from gui.datawindow import DataWindow
    from gui.grasswindow import GrassWindow
    from gui.layerlistwindow import LayerListWindow
    from gui.querywindow import QueryWindow  
##from psinit import * #FIXME

class SashaMainWindow(QMainWindow, Ui_SashaMainWindow):
    def __init__(self, arg):
        QMainWindow.__init__(self)
        
        
        self.setupUi(self)
        
        self.setCentralWidget(self.mdiArea)
        #self.setLayout(self.verticalLayout)

#        self.navwin =  NavigationWindow()
#        self.mdiArea.addSubWindow(self.navwin)
#        self.navwin.show()

        #self.prefsWindow_ = PreferencesWindow()
        
        self.actionT_LonLat.triggered.connect(self.showNavWindow)

        self.actionM_Navigation.triggered.connect(self.showNavWindow)
        self.actionM_Query.triggered.connect(self.showQueryWindow)
        self.actionM_GPS.triggered.connect(self.showGpsWindow)
        self.actionM_Data.triggered.connect(self.showDataWindow)
        self.actionM_Import.triggered.connect(self.showImportWindow)
        self.actionM_Preferences.triggered.connect(self.showPrefsWindow)
        self.actionM_Map.triggered.connect(self.showMapWindow)
        self.actionM_Ossim.triggered.connect(self.showOssimWindow)

        #self.connect(self.actionLonLat, SIGNAL("triggered()"),           self.LonLatunceckbuttons)                 


        self.joy = logJ()
        self.log = logS()
        #self.hw = HWS()
        self.gpsx = GpsT()
        #self.gt = gt(self.setcmd)
        #
        #self.lineEdit2 = QLineEdit(self.tab_6)
        #self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        #self.compassLayout.addWidget(self.lineEdit2)



        #

        #self.mainTabWidget.setCurrentIndex(0)    


    def showNavWindow(self):
        self.navwin =  NavigationWindow()
        self.mdiArea.addSubWindow(self.navwin)
        self.navwin.show()

    def showQueryWindow(self):
        self.querywin =  QueryWindow()
        self.mdiArea.addSubWindow(self.querywin)
        self.querywin.show()
        
    def showGpsWindow(self):
        self.gpswin =  GpsWindow()
        self.mdiArea.addSubWindow(self.gpswin)
        self.gpswin.show()

    def showDataWindow(self):
        if Utils.haveGRASS_:
            self.datawin =  DataWindow()
            self.mdiArea.addSubWindow(self.datawin)
            self.datawin.show()
        else:
            print "I can't do it. You don't have pygrass"
            from gui.datawindow import DataWindow
            self.datawin =  DataWindow()
            self.mdiArea.addSubWindow(self.datawin)
            self.datawin.show()

    def showImportWindow(self):
        self.impwin =  ImportWindow(self.mdiArea)
        #self.impwin.setAttribute(Qt.WA_DeleteOnClose, True)
        self.mdiArea.addSubWindow(self.impwin)
        #self.mdiArea.resize(752,497)
        self.impwin.show()
         
    def showPrefsWindow(self):
        self.prefwin =  PreferencesWindow()
        self.mdiArea.addSubWindow(self.prefwin)
        self.prefwin.show()

    def showMapWindow(self):
        self.mapwin =  MapWindow()
        self.mdiArea.addSubWindow(self.mapwin)
        self.mapwin.show()
        
    def showOssimWindow(self):
        self.osmwin =  OssimWindow()
        self.mdiArea.addSubWindow(self.osmwin)
        self.osmwin.show()
        
#    def showExportWindow(self):
#        self.expwin =  KmlWindow()
#        self.mdiArea.addSubWindow(self.expwin)
#        self.expwin.show()            
                 
                 
    def initWidgets(self):           
                     
        if Utils.haveGRASS_ == 0:
            self.mainTabWidget.removeTab(1)
            self.actionGrass.setEnabled(False)
            self.actionData.setEnabled(False)
            self.actionGrass.setVisible(False)
            self.actionData.setVisible(False)
            self.actionGrassshell.setEnabled(False)
            self.actionGrassshell.setVisible(False)
        else:
            self.grasswin = GrassWindow()
            self.datawin  = DataWindow()
            

###FIXME REVIEW                         
###            self.vectors = VectorList()
###            self.rasters = RasterList()
###            vect = len(self.vectors)
###            rast = len(self.rasters)
###            numrow = max(vect,rast)
###            self.layerTable.setColumnCount(2)
###            self.layerTable.setRowCount(numrow)
###            self.layerTable.setEditTriggers(QTableWidget.NoEditTriggers)
###            for i in range(rast):
###                item = QTableWidgetItem(self.rasters[i])
###                item.setTextAlignment(Qt.AlignCenter)
###                item.setCheckState(Qt.Unchecked)
###                self.layerTable.setItem(i, 0, item)
###            for i in range(vect):
###                item = QTableWidgetItem(self.vectors[i])
###                item.setTextAlignment(Qt.AlignCenter)
###                item.setCheckState(Qt.Unchecked)
###                self.layerTable.setItem(i, 1, item)
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
#        self.connect(self.actionHideSlider, SIGNAL("triggered()"), self.hidetool)

        #self.connectZoomSignals()
        #self.connectPlaceSignals()
        #self.connectActionSignals()


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
        self.datawin.show()
    
    
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

    def addLayer(self):
        count = self.layerTable.rowCount()
        self.rasterCombo.clear()
        for j in xrange(1):
            for i in xrange(count):
                cell = self.layerTable.item(i,j)
                if cell and cell.checkState() == 2:
                
                    self.rasterCombo.addItem(cell.text())
        # cell = self.layerTable.item(i, 0)
#            if cell.checkState() == 2:
 #               while 1:
  #                  try:
   #                     s = read_command('r.what', input=cell.text(), east_north=lonlat)
    def addRasterLayer(self):
        try:
            pp = str(parseOutputconf()['pport'])
            dp = str(parseOutputconf()['dport'])
            host = str(parseOutputconf()['host']).split()
            #print host, dp, pp
            for item in self.layerTable.selectedItems():
                lname = item.text()
                #print host
                for i in host :
                    #print i
                    try:
                        run_command('./grass_script/r.planet.py', 
                                    flags = 'a', 
                                    map = lname, 
                                    host = str(i), 
                                    dport = dp, pport = pp )
                    except IOError:
                        time.sleep(0.1)

        except IOError:
            time.sleep(0.1)
        print 'add', lname
    
        
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

        inputR = self.rasterCombo.itemText(index)
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
            cell = self.layerTable.item(i, 0)
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
            cell = self.layerTable.item(i, 1)
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
    

    def hidetool(self):
        if self.actionHideSlider.isChecked():
            self.tabWidget.show()
        else :
            self.tabWidget.hide()    
    
            

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
    
    

    

        
                                                     
