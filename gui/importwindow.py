#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_importwindow import Ui_ImportWindow
import os
from episg import *
apppath = os.path.abspath(os.path.dirname(sys.argv[0]))
epsgfile = str(apppath)+'/epsg'

class ImportWindow(QWidget, Ui_ImportWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

   	#imgQ = ImageQt.ImageQt(img)
        pixMap = QPixmap.fromImage(QImage("gui/images/qgis_world.png"))

        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)
        #pixMap = pixMap.scaled(self.graphicsView.size())
        scene.addPixmap(pixMap)               
        self.graphicsView.repaint()
        self.graphicsView.show()
