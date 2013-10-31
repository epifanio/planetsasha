# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sashamainwindow.ui'
#
# Created: Thu Oct 31 08:01:36 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SashaMainWindow(object):
    def setupUi(self, SashaMainWindow):
        SashaMainWindow.setObjectName(_fromUtf8("SashaMainWindow"))
        SashaMainWindow.setWindowModality(QtCore.Qt.NonModal)
        SashaMainWindow.resize(794, 652)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/epi.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SashaMainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(SashaMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(70, 20, 459, 439))
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        SashaMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SashaMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSasha = QtGui.QMenu(self.menubar)
        self.menuSasha.setObjectName(_fromUtf8("menuSasha"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        SashaMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SashaMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SashaMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(SashaMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        SashaMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionM_Navigation = QtGui.QAction(SashaMainWindow)
        self.actionM_Navigation.setObjectName(_fromUtf8("actionM_Navigation"))
        self.actionM_Query = QtGui.QAction(SashaMainWindow)
        self.actionM_Query.setObjectName(_fromUtf8("actionM_Query"))
        self.actionM_GPS = QtGui.QAction(SashaMainWindow)
        self.actionM_GPS.setEnabled(False)
        self.actionM_GPS.setVisible(True)
        self.actionM_GPS.setObjectName(_fromUtf8("actionM_GPS"))
        self.actionT_Model = QtGui.QAction(SashaMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/cubo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Model.setIcon(icon1)
        self.actionT_Model.setVisible(False)
        self.actionT_Model.setObjectName(_fromUtf8("actionT_Model"))
        self.actionT_Joystick = QtGui.QAction(SashaMainWindow)
        self.actionT_Joystick.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/joystick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Joystick.setIcon(icon2)
        self.actionT_Joystick.setVisible(False)
        self.actionT_Joystick.setObjectName(_fromUtf8("actionT_Joystick"))
        self.actionT_LonLat = QtGui.QAction(SashaMainWindow)
        self.actionT_LonLat.setCheckable(True)
        self.actionT_LonLat.setChecked(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/600px-Brosen_windrose.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_LonLat.setIcon(icon3)
        self.actionT_LonLat.setObjectName(_fromUtf8("actionT_LonLat"))
        self.actionT_Gt = QtGui.QAction(SashaMainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/gui-help.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Gt.setIcon(icon4)
        self.actionT_Gt.setObjectName(_fromUtf8("actionT_Gt"))
        self.actionDB_setting = QtGui.QAction(SashaMainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/db.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDB_setting.setIcon(icon5)
        self.actionDB_setting.setObjectName(_fromUtf8("actionDB_setting"))
        self.actionNMEA = QtGui.QAction(SashaMainWindow)
        self.actionNMEA.setObjectName(_fromUtf8("actionNMEA"))
        self.actionT_Data = QtGui.QAction(SashaMainWindow)
        self.actionT_Data.setCheckable(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/module-db.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Data.setIcon(icon6)
        self.actionT_Data.setObjectName(_fromUtf8("actionT_Data"))
        self.actionT_Savekml = QtGui.QAction(SashaMainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/saveinfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Savekml.setIcon(icon7)
        self.actionT_Savekml.setObjectName(_fromUtf8("actionT_Savekml"))
        self.actionEpsg = QtGui.QAction(SashaMainWindow)
        self.actionEpsg.setObjectName(_fromUtf8("actionEpsg"))
        self.actionHideSpinbox = QtGui.QAction(SashaMainWindow)
        self.actionHideSpinbox.setCheckable(True)
        self.actionHideSpinbox.setObjectName(_fromUtf8("actionHideSpinbox"))
        self.actionHideSlider = QtGui.QAction(SashaMainWindow)
        self.actionHideSlider.setCheckable(True)
        self.actionHideSlider.setObjectName(_fromUtf8("actionHideSlider"))
        self.actionT_Exit = QtGui.QAction(SashaMainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Exit.setIcon(icon8)
        self.actionT_Exit.setObjectName(_fromUtf8("actionT_Exit"))
        self.actionVrt = QtGui.QAction(SashaMainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ingranaggio_icona.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVrt.setIcon(icon9)
        self.actionVrt.setObjectName(_fromUtf8("actionVrt"))
        self.actionDataexp = QtGui.QAction(SashaMainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ingranaggi.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDataexp.setIcon(icon10)
        self.actionDataexp.setObjectName(_fromUtf8("actionDataexp"))
        self.actionJoystick_2 = QtGui.QAction(SashaMainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/joystick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJoystick_2.setIcon(icon11)
        self.actionJoystick_2.setObjectName(_fromUtf8("actionJoystick_2"))
        self.actionHideStepTool = QtGui.QAction(SashaMainWindow)
        self.actionHideStepTool.setCheckable(True)
        self.actionHideStepTool.setObjectName(_fromUtf8("actionHideStepTool"))
        self.actionHide_place_position = QtGui.QAction(SashaMainWindow)
        self.actionHide_place_position.setCheckable(True)
        self.actionHide_place_position.setObjectName(_fromUtf8("actionHide_place_position"))
        self.actionHidesliders = QtGui.QAction(SashaMainWindow)
        self.actionHidesliders.setCheckable(True)
        self.actionHidesliders.setObjectName(_fromUtf8("actionHidesliders"))
        self.actionT_Grassshell = QtGui.QAction(SashaMainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/512 Terminal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Grassshell.setIcon(icon12)
        self.actionT_Grassshell.setObjectName(_fromUtf8("actionT_Grassshell"))
        self.actionPref = QtGui.QAction(SashaMainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/tools.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPref.setIcon(icon13)
        self.actionPref.setShortcut(_fromUtf8(""))
        self.actionPref.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionPref.setObjectName(_fromUtf8("actionPref"))
        self.actionT_HW = QtGui.QAction(SashaMainWindow)
        self.actionT_HW.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/keyser-tux-wifi-logo-2300.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_HW.setIcon(icon14)
        self.actionT_HW.setVisible(False)
        self.actionT_HW.setObjectName(_fromUtf8("actionT_HW"))
        self.actionT_VectorOp = QtGui.QAction(SashaMainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/SquadraCompasso.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_VectorOp.setIcon(icon15)
        self.actionT_VectorOp.setVisible(False)
        self.actionT_VectorOp.setObjectName(_fromUtf8("actionT_VectorOp"))
        self.actionT_Broadcast = QtGui.QAction(SashaMainWindow)
        self.actionT_Broadcast.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/Ubuntu_connessione_Internet_.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Broadcast.setIcon(icon16)
        self.actionT_Broadcast.setObjectName(_fromUtf8("actionT_Broadcast"))
        self.actionCompass = QtGui.QAction(SashaMainWindow)
        self.actionCompass.setObjectName(_fromUtf8("actionCompass"))
        self.actionPan_Tool = QtGui.QAction(SashaMainWindow)
        self.actionPan_Tool.setObjectName(_fromUtf8("actionPan_Tool"))
        self.actionT_GVrt = QtGui.QAction(SashaMainWindow)
        self.actionT_GVrt.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/ingranaggio_icona.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_GVrt.setIcon(icon17)
        self.actionT_GVrt.setObjectName(_fromUtf8("actionT_GVrt"))
        self.actionT_Grass = QtGui.QAction(SashaMainWindow)
        self.actionT_Grass.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/grass_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_Grass.setIcon(icon18)
        self.actionT_Grass.setObjectName(_fromUtf8("actionT_Grass"))
        self.actionM_Preferences = QtGui.QAction(SashaMainWindow)
        self.actionM_Preferences.setObjectName(_fromUtf8("actionM_Preferences"))
        self.actionM_Exit = QtGui.QAction(SashaMainWindow)
        self.actionM_Exit.setObjectName(_fromUtf8("actionM_Exit"))
        self.actionView = QtGui.QAction(SashaMainWindow)
        self.actionView.setObjectName(_fromUtf8("actionView"))
        self.actionView_2 = QtGui.QAction(SashaMainWindow)
        self.actionView_2.setObjectName(_fromUtf8("actionView_2"))
        self.actionM_Data = QtGui.QAction(SashaMainWindow)
        self.actionM_Data.setObjectName(_fromUtf8("actionM_Data"))
        self.actionM_Ossim = QtGui.QAction(SashaMainWindow)
        self.actionM_Ossim.setObjectName(_fromUtf8("actionM_Ossim"))
        self.actionM_Import = QtGui.QAction(SashaMainWindow)
        self.actionM_Import.setObjectName(_fromUtf8("actionM_Import"))
        self.actionM_Map = QtGui.QAction(SashaMainWindow)
        self.actionM_Map.setObjectName(_fromUtf8("actionM_Map"))
        self.actionExport = QtGui.QAction(SashaMainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionT_GPS = QtGui.QAction(SashaMainWindow)
        self.actionT_GPS.setCheckable(True)
        self.actionT_GPS.setChecked(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/satellite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionT_GPS.setIcon(icon19)
        self.actionT_GPS.setObjectName(_fromUtf8("actionT_GPS"))
        self.menuSasha.addAction(self.actionM_Navigation)
        self.menuSasha.addAction(self.actionM_Query)
        self.menuSasha.addAction(self.actionM_GPS)
        self.menuSasha.addAction(self.actionM_Data)
        self.menuSasha.addSeparator()
        self.menuSasha.addAction(self.actionM_Preferences)
        self.menuSasha.addSeparator()
        self.menuSasha.addAction(self.actionM_Exit)
        self.menuTools.addAction(self.actionM_Ossim)
        self.menuData.addAction(self.actionM_Import)
        self.menuData.addAction(self.actionM_Map)
        self.menuData.addAction(self.actionExport)
        self.menubar.addAction(self.menuSasha.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.toolBar.addAction(self.actionT_LonLat)
        self.toolBar.addAction(self.actionT_Grass)
        self.toolBar.addAction(self.actionT_GPS)
        self.toolBar.addAction(self.actionT_Broadcast)
        self.toolBar.addAction(self.actionT_Joystick)
        self.toolBar.addAction(self.actionT_HW)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionT_Grassshell)
        self.toolBar.addAction(self.actionT_Data)
        self.toolBar.addAction(self.actionT_Savekml)
        self.toolBar.addAction(self.actionT_VectorOp)
        self.toolBar.addAction(self.actionT_Model)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionT_Gt)
        self.toolBar.addAction(self.actionT_GVrt)
        self.toolBar.addAction(self.actionT_Exit)

        self.retranslateUi(SashaMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SashaMainWindow)

    def retranslateUi(self, SashaMainWindow):
        SashaMainWindow.setWindowTitle(_translate("SashaMainWindow", "PlanetSasha", None))
        self.menuSasha.setTitle(_translate("SashaMainWindow", "Sasha", None))
        self.menuTools.setTitle(_translate("SashaMainWindow", "Tools", None))
        self.menuData.setTitle(_translate("SashaMainWindow", "Data", None))
        self.toolBar.setWindowTitle(_translate("SashaMainWindow", "toolBar", None))
        self.actionM_Navigation.setText(_translate("SashaMainWindow", "Navigation", None))
        self.actionM_Query.setText(_translate("SashaMainWindow", "Query", None))
        self.actionM_GPS.setText(_translate("SashaMainWindow", "GPS", None))
        self.actionT_Model.setText(_translate("SashaMainWindow", "model", None))
        self.actionT_Joystick.setText(_translate("SashaMainWindow", "Joystick", None))
        self.actionT_Joystick.setToolTip(_translate("SashaMainWindow", "Joystick", None))
        self.actionT_LonLat.setText(_translate("SashaMainWindow", "LonLat", None))
        self.actionT_LonLat.setToolTip(_translate("SashaMainWindow", "LonLat", None))
        self.actionT_Gt.setText(_translate("SashaMainWindow", "Gt", None))
        self.actionDB_setting.setText(_translate("SashaMainWindow", "DB-setting", None))
        self.actionNMEA.setText(_translate("SashaMainWindow", "NMEA", None))
        self.actionT_Data.setText(_translate("SashaMainWindow", "Data", None))
        self.actionT_Data.setToolTip(_translate("SashaMainWindow", "Data processing", None))
        self.actionT_Savekml.setText(_translate("SashaMainWindow", "savekml", None))
        self.actionEpsg.setText(_translate("SashaMainWindow", "Epsg", None))
        self.actionHideSpinbox.setText(_translate("SashaMainWindow", "Spinbox", None))
        self.actionHideSlider.setText(_translate("SashaMainWindow", "tabPosition", None))
        self.actionT_Exit.setText(_translate("SashaMainWindow", "Quit", None))
        self.actionVrt.setText(_translate("SashaMainWindow", "DataTools", None))
        self.actionDataexp.setText(_translate("SashaMainWindow", "Export", None))
        self.actionJoystick_2.setText(_translate("SashaMainWindow", "Joystick", None))
        self.actionHideStepTool.setText(_translate("SashaMainWindow", "StepTool", None))
        self.actionHide_place_position.setText(_translate("SashaMainWindow", "Place-Position", None))
        self.actionHidesliders.setText(_translate("SashaMainWindow", "hideslider", None))
        self.actionT_Grassshell.setText(_translate("SashaMainWindow", "grassshell", None))
        self.actionPref.setText(_translate("SashaMainWindow", "Preferences", None))
        self.actionPref.setToolTip(_translate("SashaMainWindow", "Preferences", None))
        self.actionT_HW.setText(_translate("SashaMainWindow", "HW", None))
        self.actionT_HW.setToolTip(_translate("SashaMainWindow", "Serial", None))
        self.actionT_VectorOp.setText(_translate("SashaMainWindow", "VectorOp", None))
        self.actionT_Broadcast.setText(_translate("SashaMainWindow", "actionBroadcast", None))
        self.actionCompass.setText(_translate("SashaMainWindow", "Compass", None))
        self.actionPan_Tool.setText(_translate("SashaMainWindow", "Pan-Tool", None))
        self.actionT_GVrt.setText(_translate("SashaMainWindow", "vrt", None))
        self.actionT_Grass.setText(_translate("SashaMainWindow", "Grass", None))
        self.actionT_Grass.setToolTip(_translate("SashaMainWindow", "Grass", None))
        self.actionM_Preferences.setText(_translate("SashaMainWindow", "Preferences", None))
        self.actionM_Exit.setText(_translate("SashaMainWindow", "Exit", None))
        self.actionView.setText(_translate("SashaMainWindow", "View", None))
        self.actionView_2.setText(_translate("SashaMainWindow", "View", None))
        self.actionM_Data.setText(_translate("SashaMainWindow", "Data", None))
        self.actionM_Ossim.setText(_translate("SashaMainWindow", "OSSIM App", None))
        self.actionM_Import.setText(_translate("SashaMainWindow", "Import", None))
        self.actionM_Map.setText(_translate("SashaMainWindow", "View", None))
        self.actionExport.setText(_translate("SashaMainWindow", "Export", None))
        self.actionT_GPS.setText(_translate("SashaMainWindow", "GPS", None))

import resources_rc
