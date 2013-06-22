#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gen.ui_warnmsgwindow import Ui_WarnMsgWindow

class WarnMsgWindow(QWidget, Ui_WarnMsgWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
       
