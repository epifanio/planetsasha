#!/usr/bin/env python
import os
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_gpswindow import Ui_GpsWindow

class GpsWindow(QWidget, Ui_GpsWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setLayout(self.verticalLayout)

